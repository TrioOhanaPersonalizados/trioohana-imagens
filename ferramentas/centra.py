"""Centraliza o motivo de cada lado da arte na frente da caneca (vista do lado esquerdo e do direito).
Uso: python3 -I centra.py <arte_pronta.png> <saida.png>
Frente da caneca no motor: 18,9% (alça à esquerda) e 81,1% (alça à direita) da largura da arte."""
import sys, json, math, numpy as np, cv2
from PIL import Image
GRAUS = 360 * 20.7 / (math.pi * 8.2)
ALVO_E = ((0 - (-90 + (360 - GRAUS) / 2)) % 360) / GRAUS
ALVO_D = ((0 - (90 + (360 - GRAUS) / 2)) % 360) / GRAUS
def tinta(a):
    h, w = a.shape[:2]
    fundo = np.median(a.reshape(-1, 3), 0)
    d = np.abs(a.astype(np.int16) - fundo).max(2) > 40
    n, lab, st, _ = cv2.connectedComponentsWithStats(d.astype(np.uint8), 8)
    m = np.zeros_like(d)
    minarea = h * w * 0.00025; padrao = 0; moldura = np.zeros_like(d)
    for i in range(1, n):
        if st[i, 4] < minarea: continue
        if st[i, 2] >= w * 0.6:  # cruza a arte: moldura fina (ignorar) ou estampa de fundo (xadrez, listras)
            dentro = int((lab[int(h*.06):int(h*.94), int(w*.03):int(w*.97)] == i).sum())
            if dentro < h * w * 0.002: moldura |= (lab == i)
            padrao += dentro
            continue
        m[lab == i] = True
    return m, padrao > h * w * 0.002, moldura, fundo
def faixas(col, minimo):
    """intervalos com tinta (colunas)."""
    on = col > minimo; r = []; i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]: j += 1
            r.append((i, j)); i = j
        else: i += 1
    return r
def main(src, dst):
    a = np.array(Image.open(src).convert('RGB')); h, w = a.shape[:2]
    m, padrao, moldura, fundo = tinta(a); col = m.sum(0)
    if moldura.any():  # contorno-guia do arquivo do designer: não imprime, apaga
        a = a.copy(); a[cv2.dilate(moldura.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0] = fundo.astype(np.uint8)
    if padrao:
        Image.fromarray(a).save(dst, dpi=(300, 300)); print(json.dumps({"centrado": False, "motivo": "fundo estampado"})); return
    # junta motivos próximos (vão < 3% da largura)
    fx = faixas(col, 2); g = []
    for f in fx:
        if g and f[0] - g[-1][1] < w * 0.03: g[-1] = (g[-1][0], f[1])
        else: g.append(f)
    # maior vão entre 30% e 70% separa os dois lados
    best = None
    for (a0, a1), (b0, b1) in zip(g, g[1:]):
        meio = (a1 + b0) / 2
        if 0.3 * w < meio < 0.7 * w and (best is None or b0 - a1 > best[1] - best[0]): best = (a1, b0)
    if best is None:
        Image.fromarray(a).save(dst, dpi=(300, 300)); print(json.dumps({"centrado": False, "motivo": "sem vão entre os lados (estampa contínua)"})); return
    split = (best[0] + best[1]) // 2
    out = a.copy(); info = {"centrado": True}
    for lado, (x0, x1, alvo) in {"esq": (0, split, ALVO_E), "dir": (split, w, ALVO_D)}.items():
        cs = np.nonzero(col[x0:x1] > 2)[0]
        if len(cs) == 0: continue
        c0, c1 = cs[0] + x0, cs[-1] + x0
        d = int(round(alvo * w - (int(c0) + int(c1)) / 2))
        d = int(max(x0 - c0 + 2, min(x1 - 1 - c1 - 2, d)))  # o motivo não sai do próprio lado
        out[:, x0:x1] = np.roll(a[:, x0:x1], d, axis=1)
        c0, c1 = int(c0), int(c1)
        info[lado] = {"motivo": [round(c0 / w, 3), round(c1 / w, 3)], "centro_antes": round((c0 + c1) / 2 / w, 3), "deslocamento_px": d, "centro_depois": round(((c0 + c1) / 2 + d) / w, 3)}
    info["alvos"] = [round(ALVO_E, 3), round(ALVO_D, 3)]
    Image.fromarray(out).save(dst, dpi=(300, 300)); print(json.dumps(info))
if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
