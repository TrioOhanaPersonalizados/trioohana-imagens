"""Gera job da esteira para converter um produto duplicado: textos, SEO, link, tags e fotos novas."""
import json, re, sys, glob, os, shutil, unicodedata
sys.path.insert(0, "/home/claude/pack07")
from monta import BASE, C1, C2, CORES, slug
REPO = "/home/claude/trioohana-imagens"
def job(pid, d, pasta):
    link = slug(d["nome"]); base_slug = link.replace("-325ml", "")
    arqs = sorted(glob.glob(pasta + "/*.webp")); assert len(arqs) == 19
    dest = f"{REPO}/canecas/{base_slug}"; os.makedirs(dest, exist_ok=True)
    imgs = []
    for f in arqs:
        b = os.path.basename(f); assert b[3:].startswith(base_slug), b
        shutil.copyfile(f, f"{dest}/{b}"); k = int(b[:2])
        im = {"file": f"canecas/{base_slug}/{b}", "alt": d["nome"].replace(" 325ml", "")}
        if 5 <= k <= 18: im["variant_value"] = CORES[k - 5][0]
        imgs.append(im)
    ideal = "<h2>Ideal para</h2>\n<ul>\n" + "".join(f"<li>{x}</li>\n" for x in d["ideal"]) + "</ul>"
    desc = BASE.replace(C1, d["abertura"]).replace(C2, ideal).strip() + "\n"; assert "<!--" not in desc
    mt, md = d["meta_title"], d["meta_desc"]
    def blen(s): return len(s) + sum(1 for c in s if ord(c) > 127)
    assert blen(mt) <= 70 and blen(md) <= 160, (blen(mt), blen(md))
    prod = {"description": {"pt": desc}, "handle": {"pt": link}, "seo_title": {"pt": mt}, "seo_description": {"pt": md},
            "tags": ", ".join(d["tags"]), "published": True}
    if d.get("cats"): prod["categories"] = d["cats"]
    print(pid, d["nome"], "| mt", blen(mt), "md", blen(md))
    return [{"op": "update", "ref": f"{pid} textos", "product_id": pid, "product": prod},
            {"op": "replace_images", "ref": f"{pid} fotos", "product_id": pid, "images": imgs, "principal": imgs[0]["file"]}]
