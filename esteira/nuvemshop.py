"""Esteira de catálogo Trio Ohana -> Nuvemshop (API REST).

Lê um arquivo de job (JSON) em jobs/ e executa as operações descritas.
O token vem do secret NUVEMSHOP_TOKEN e NUNCA é impresso.

Operações suportadas (campo "op" de cada item):
  - check            : confere acesso lendo um produto (product_id)
  - set_alts         : grava texto alternativo nas imagens de um produto
                       {"product_id": 1, "alts": {"<image_id>": "texto"}}
  - link_variants    : vincula foto a variação
                       {"product_id": 1, "links": {"<variant_id>": <image_id>}}
  - create_product   : cria produto completo a partir de arquivos do repositório
                       {"product": {...payload da API sem images...},
                        "images": [{"file": "natal/x.jpg", "alt": "...", "variant_value": "Alça e Interior Verde"}],
                        "principal": "natal/x.jpg"}
Cada execução grava um relatório em relatorios/<job>.json (sem dados sensíveis).
"""
import base64, json, os, sys, time, pathlib, urllib.request, urllib.error

TOKEN = os.environ.get("NUVEMSHOP_TOKEN", "").strip()
STORE = os.environ.get("NUVEMSHOP_STORE_ID", "6361192").strip()
UA = os.environ.get("NUVEMSHOP_USER_AGENT", "Trio Ohana Esteira de Catalogo (app 52655)")
BASE = f"https://api.nuvemshop.com.br/v1/{STORE}"
ALT_FMT = os.environ.get("ALT_FMT", "seo")
ROOT = pathlib.Path(__file__).resolve().parent.parent


def api(method, path, body=None, tries=4, base=None):
    data = None if body is None else json.dumps(body).encode()
    for i in range(tries):
        req = urllib.request.Request((base or BASE) + path, data=data, method=method, headers={
            "Authentication": f"bearer {TOKEN}",
            "User-Agent": UA,
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                txt = r.read().decode() or "{}"
                return json.loads(txt)
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:500]
            if e.code == 429 or e.code >= 500:
                time.sleep(2 * (i + 1)); continue
            raise RuntimeError(f"{method} {path} -> HTTP {e.code}: {msg}")
    raise RuntimeError(f"{method} {path} falhou após {tries} tentativas")


def op_check(it):
    p = api("GET", f"/products/{it['product_id']}")
    return {"ok": True, "produto": p["name"].get("pt"), "variacoes": len(p["variants"]), "imagens": len(p["images"]),
            "vinculos": {str(v["id"]): v.get("image_id") for v in p["variants"]},
            "alts": {str(i["id"]): (i.get("alt") or {}).get("pt") if isinstance(i.get("alt"), dict) else i.get("alt") for i in p["images"]}}


def alt_body(alt, fmt="seo"):
    if fmt == "seo": return {"seo": {"pt": {"alt": alt}}}
    if fmt == "pt": return {"alt": {"pt": alt}}
    if fmt == "list": return {"alt": [{"pt": alt}]}
    if fmt == "str": return {"alt": alt}
    return {"alt": {"pt_BR": alt}}


def op_set_alts(it):
    pid = it["product_id"]; n = 0
    fmts = it.get("formatos", {})
    for img_id, alt in it["alts"].items():
        api("PUT", f"/products/{pid}/images/{img_id}", alt_body(alt, fmts.get(img_id, it.get("formato", "pt_BR")))); n += 1
    return {"ok": True, "imagens_atualizadas": n}


def op_link_variants(it):
    pid = it["product_id"]; n = 0
    for var_id, img_id in it["links"].items():
        api("PUT", f"/products/{pid}/variants/{var_id}", {"image_id": int(img_id)}); n += 1
    return {"ok": True, "variacoes_vinculadas": n}


def upload_image(pid, file, alt, position, fmt=None):
    raw = (ROOT / file).read_bytes()
    body = {"attachment": base64.b64encode(raw).decode(), "filename": pathlib.Path(file).name, "position": position}
    if alt:
        body.update(alt_body(alt, fmt or ALT_FMT))   # o texto alternativo só grava no envio da foto
    img = api("POST", f"/products/{pid}/images", body)
    return img["id"]


def op_replace_images(it):
    """Substitui todas as fotos de um produto: envia as novas (com texto alternativo),
    vincula cada variação à sua foto e apaga as antigas."""
    pid = it["product_id"]
    antes = api("GET", f"/products/{pid}")
    old_ids = [i["id"] for i in antes["images"]]
    imgs = sorted(it["images"], key=lambda x: x["file"] != it.get("principal", it["images"][0]["file"]))
    ids = {}
    for pos, im in enumerate(imgs, 1):
        ids[im["file"]] = upload_image(pid, im["file"], im.get("alt"), len(old_ids) + pos, it.get("formato_alt"))
    by_value = {im["variant_value"]: ids[im["file"]] for im in imgs if im.get("variant_value")}
    linked = 0
    for v in antes["variants"]:
        val = (v.get("values") or [{}])[0].get("pt")
        if val in by_value:
            api("PUT", f"/products/{pid}/variants/{v['id']}", {"image_id": by_value[val]}); linked += 1
    for oid in old_ids:
        api("DELETE", f"/products/{pid}/images/{oid}")
    # reordena: principal primeiro
    for pos, im in enumerate(imgs, 1):
        api("PUT", f"/products/{pid}/images/{ids[im['file']]}", {"position": pos})
    return {"ok": True, "novas": len(ids), "apagadas": len(old_ids), "variacoes_vinculadas": linked}


def op_create_product(it):
    prod = api("POST", "/products", it["product"])
    pid = prod["id"]
    imgs = it["images"]
    principal = it.get("principal") or imgs[0]["file"]
    imgs = sorted(imgs, key=lambda x: x["file"] != principal)
    ids = {}
    for pos, im in enumerate(imgs, 1):
        ids[im["file"]] = upload_image(pid, im["file"], im.get("alt"), pos)
    by_value = {im["variant_value"]: ids[im["file"]] for im in imgs if im.get("variant_value")}
    linked = 0
    for v in prod["variants"]:
        val = (v.get("values") or [{}])[0].get("pt")
        if val in by_value:
            api("PUT", f"/products/{pid}/variants/{v['id']}", {"image_id": by_value[val]}); linked += 1
    check = api("GET", f"/products/{pid}")
    return {"ok": True, "product_id": pid, "handle": check["handle"].get("pt"), "imagens": len(check["images"]),
            "variacoes": len(check["variants"]), "variacoes_vinculadas": linked, "published": check["published"]}


def op_dump(it):
    """Grava o JSON completo de um produto (para conferir campos da API)."""
    p = api("GET", f"/products/{it['product_id']}")
    v = p["variants"][:2]
    return {"ok": True, "chaves_produto": sorted(p.keys()), "handle": p.get("handle"),
            "variantes_exemplo": v, "imagem_exemplo": p["images"][:1],
            "outros": {k: p[k] for k in p if k not in ("variants", "images", "description")}}


def op_update(it):
    """PUT parcial em produto e, opcionalmente, nas variações (lista de {id, ...campos})."""
    pid = it["product_id"]; res = {}
    if it.get("product"):
        r = api("PUT", f"/products/{pid}", it["product"]); res["handle"] = r.get("handle"); res["published"] = r.get("published")
    n = 0
    for v in it.get("variants", []):
        vid = v.pop("id"); api("PUT", f"/products/{pid}/variants/{vid}", v); n += 1
    res["variacoes_atualizadas"] = n
    if it.get("echo_variant"):
        res["variante"] = api("GET", f"/products/{pid}/variants/{it['echo_variant']}")
    return {"ok": True, **res}


def op_padrao_variantes(it):
    """Aplica os dados fixos de caneca a todas as variações (custo, peso, medidas, MPN, Google Shopping)."""
    pid = it["product_id"]; p = api("GET", f"/products/{pid}"); n = 0
    for v in p["variants"]:
        cor = (v.get("values") or [{}])[0].get("pt")
        body = {"cost": "13.00" if cor == "Branca" else "15.00", "weight": "0.200", "width": "10.00", "height": "10.00",
                "depth": "10.00", "mpn": "3000", "age_group": "adult", "gender": "unisex"}
        api("PUT", f"/products/{pid}/variants/{v['id']}", body); n += 1
    v = api("GET", f"/products/{pid}/variants/{p['variants'][0]['id']}")
    return {"ok": True, "variacoes": n, "exemplo": {k: v.get(k) for k in ("cost", "weight", "width", "mpn", "age_group", "gender", "sku", "image_id")}}


def op_probe_alt(it):
    """Envia uma foto temporária em cada formato de alt, lê o que gravou e apaga."""
    pid = it["product_id"]; res = {}
    for fmt in it["formatos"]:
        base = None
        if fmt.endswith("@2025-03"):
            fmt0 = fmt.split("@")[0]; base = f"https://api.nuvemshop.com.br/2025-03/{STORE}"
        else:
            fmt0 = fmt
        try:
            if it.get("src"):
                body = {"src": it["src"], "position": 99}
            else:
                raw = (ROOT / it["file"]).read_bytes()
                body = {"attachment": base64.b64encode(raw).decode(), "filename": "teste-alt.jpg", "position": 99}
            body.update(alt_body("teste " + fmt, fmt0))
            iid = api("POST", f"/products/{pid}/images", body, base=base)["id"]
            got = [i for i in api("GET", f"/products/{pid}")["images"] if i["id"] == iid][0].get("alt")
            res[fmt] = got
            api("DELETE", f"/products/{pid}/images/{iid}")
        except Exception as e:
            res[fmt] = "ERRO: " + str(e)[:200]
    return {"ok": True, "resultado": res}


OPS = {"padrao_variantes": op_padrao_variantes, "dump": op_dump, "update": op_update, "probe_alt": op_probe_alt, "replace_images": op_replace_images, "check": op_check, "set_alts": op_set_alts, "link_variants": op_link_variants, "create_product": op_create_product}


def main(job_path):
    if not TOKEN:
        sys.exit("NUVEMSHOP_TOKEN não configurado nos secrets do repositório.")
    job = json.loads(pathlib.Path(job_path).read_text())
    out = []
    for it in job["itens"]:
        try:
            res = OPS[it["op"]](it)
        except Exception as e:
            res = {"ok": False, "erro": str(e)}
        res = {"op": it["op"], "ref": it.get("ref"), **res}
        print(json.dumps(res, ensure_ascii=False))
        out.append(res)
    rep = ROOT / "relatorios" / (pathlib.Path(job_path).stem + ".json")
    rep.parent.mkdir(exist_ok=True)
    rep.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    if not all(r["ok"] for r in out):
        sys.exit(1)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
