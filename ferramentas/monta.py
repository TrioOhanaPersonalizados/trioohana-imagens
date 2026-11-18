"""Monta pastas no repositório e o job da esteira para os produtos do PACK 07."""
import json, re, os, glob, shutil, unicodedata, sys
sys.path.insert(0, "/home/claude/pack07")
from dados import P

REPO = "/home/claude/trioohana-imagens"
BASE = open("/home/claude/work/base_instrucao.html").read()
C1 = "<!-- ABERTURA: texto específico desta caneca (arte, para quem, ocasião). Substituir este comentário. -->"
C2 = "<!-- IDEAL PARA (opcional): ocasiões e pessoas que combinam com esta arte. Substituir ou apagar este comentário. -->"
assert BASE.count(C1) == 1 and BASE.count(C2) == 1

CORES = [  # (nome na loja, sufixo do arquivo do motor, texto do alt, slug sku)
    ("Branca", "branca", "toda branca", "branca"),
    ("Alça e Interior Amarelo", "amarelo", "com alça e interior amarelo", "amarelo"),
    ("Alça e Interior Azul Claro", "azul-claro", "com alça e interior azul claro", "azul-claro"),
    ("Alça e Interior Azul Médio", "azul-medio", "com alça e interior azul médio", "azul-medio"),
    ("Alça e Interior Azul Escuro", "azul-escuro", "com alça e interior azul escuro", "azul-escuro"),
    ("Alça e Interior Cinza", "cinza", "com alça e interior cinza", "cinza"),
    ("Alça e Interior Laranja", "laranja", "com alça e interior laranja", "laranja"),
    ("Alça e Interior Lilás", "lilas", "com alça e interior lilás", "lilas"),
    ("Alça e Interior Marrom", "marrom", "com alça e interior marrom", "marrom"),
    ("Alça e Interior Preto", "preta", "com alça e interior preto", "preto"),
    ("Alça e Interior Rosa", "rosa", "com alça e interior rosa", "rosa"),
    ("Alça e Interior Verde Claro", "verde-claro", "com alça e interior verde claro", "verde-claro"),
    ("Alça e Interior Verde Escuro", "verde-escuro", "com alça e interior verde escuro", "verde-escuro"),
    ("Alça e Interior Vermelho", "vermelho", "com alça e interior vermelho", "vermelho"),
]
EMB = [("Sem Embalagem", "49.90"), ("Hoje é o Seu Dia", "54.90"),
       ("Pra você todo o Amor do Mundo", "54.90"), ("Natalina", "54.90")]
COR_ALT = {"Vermelho": "vermelho", "Verde Escuro": "verde escuro", "Verde Claro": "verde claro", "Branca": "branca"}


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def monta(n):
    d = P[n]
    link = slug(d["nome"]); base_slug = link.replace("-325ml", "")
    assert link.endswith("-325ml")
    saida = f"/home/claude/pack07/a{n}/saida"
    arqs = sorted(glob.glob(saida + "/*.webp")); assert len(arqs) == 19, (n, len(arqs))
    destino = f"{REPO}/canecas/{base_slug}"; os.makedirs(destino, exist_ok=True)
    nomes = {}
    for f in arqs:
        b = os.path.basename(f); num = b[:2]
        resto = re.sub(r"^\d\d-[a-z0-9-]+?-(principal-[a-z-]+|lado-esquerdo|centro|lado-direito|branca|amarelo|azul-claro|azul-medio|azul-escuro|cinza|laranja|lilas|marrom|preta|rosa|verde-claro|verde-escuro|vermelho|embalagem[a-z-]*)\.webp$", r"\1", b)
        assert resto != b, b
        novo = f"{num}-{base_slug}-{resto}.webp"
        shutil.copyfile(f, f"{destino}/{novo}"); nomes[num] = novo
    c = COR_ALT.get(d["cor"], d["cor"].lower())
    curto = d["curto"]
    alts = {"01": f"{curto} com alça e interior {c}, vista dos dois lados, e arte completa com {d['elementos']}" if d["cor"] != "Branca"
            else f"{curto} toda branca, vista dos dois lados, e arte completa com {d['elementos']}",
            "02": f"{curto} {d['alt02']}", "03": f"{curto} {d['alt03']}", "04": f"{curto} {d['alt04']}",
            "19": "Opções de embalagem para presente da caneca: Todo Amor do Mundo, Natalina, Hoje é o Seu Dia ou sem embalagem"}
    for i, (loja, arq, altcor, s) in enumerate(CORES, start=5):
        alts["%02d" % i] = f"{curto} {altcor}, vista dos dois lados, e arte completa"
        assert nomes["%02d" % i].endswith(f"-{arq}.webp"), (nomes["%02d" % i], arq)
    ideal = "<h2>Ideal para</h2>\n<ul>\n" + "".join(f"<li>{x}</li>\n" for x in d["ideal"]) + "</ul>"
    desc = BASE.replace(C1, d["abertura"]).replace(C2, ideal).strip() + "\n"
    assert "<!--" not in desc
    variants = []; pos = 1
    for loja, arq, altcor, s in CORES:
        for emb, preco in EMB:
            variants.append({"price": preco, "cost": "13.00" if loja == "Branca" else "15.00",
                             "weight": "0.200", "width": "10.00", "height": "10.00", "depth": "10.00",
                             "stock_management": False, "stock": None, "mpn": "3000",
                             "age_group": "adult", "gender": "unisex",
                             "sku": f"{base_slug}-{s}-{slug(emb)}", "position": pos,
                             "values": [{"pt": loja}, {"pt": emb}]})
            pos += 1
    product = {"name": {"pt": d["nome"]}, "description": {"pt": desc}, "handle": {"pt": link},
               "attributes": [{"pt": "Cor da Caneca"}, {"pt": "Embalagem para Presente"}],
               "brand": "Trio Ohana", "published": False, "free_shipping": False, "requires_shipping": True,
               "seo_title": {"pt": d["meta_title"]}, "seo_description": {"pt": d["meta_desc"]},
               "tags": ", ".join(d["tags"]), "categories": d["cats"], "variants": variants}
    images = []
    for num in sorted(nomes):
        im = {"file": f"canecas/{base_slug}/{nomes[num]}", "alt": alts[num]}
        k = int(num)
        if 5 <= k <= 18: im["variant_value"] = CORES[k - 5][0]
        images.append(im)
    # checagens
    assert len(d["meta_title"]) <= 70, (n, len(d["meta_title"]))
    assert len(d["meta_desc"]) <= 160, (n, len(d["meta_desc"]))
    assert 5 <= len(d["tags"]) <= 10
    assert len({v["sku"] for v in variants}) == 56
    ab = len(re.sub("<[^>]+>", " ", d["abertura"]).split())
    print(f"a{n} | {d['nome']} ({len(d['nome'])}) | mt {len(d['meta_title'])} md {len(d['meta_desc'])} | abertura {ab} palavras | maior sku {max(len(v['sku']) for v in variants)} | maior alt {max(len(a) for a in alts.values())}")
    return {"op": "create_product", "ref": f"a{n} {base_slug}", "product": product, "images": images,
            "principal": images[0]["file"]}


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[2:]]
    itens = [monta(n) for n in ns]
    json.dump({"itens": itens}, open(f"{REPO}/jobs/{sys.argv[1]}.json", "w"), ensure_ascii=False, indent=1)
