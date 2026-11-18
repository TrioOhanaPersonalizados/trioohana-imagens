"""Leva os motivos para a frente da caneca (18,9% e 81,1%).
modo move: o que sai pela borda (lado da alça) é reaproveitado no vão central, sem esticar; costuras suavizadas.
modo stretch: vão central esticado (fundos lisos/pretos)."""
import numpy as np, cv2
def feather(img, xs, r=14):
    out = img.copy(); bl = cv2.GaussianBlur(img, (0, 0), 6)
    for x in xs:
        for i in range(-r, r + 1):
            xx = x + i
            if 0 <= xx < img.shape[1]:
                t = 1 - abs(i) / (r + 1); out[:, xx] = (img[:, xx] * (1 - t) + bl[:, xx] * t).astype(img.dtype)
    return out
def ajusta(a, b, c, dl, dr, modo='move'):
    h, W = a.shape[:2]; b, c, dl, dr = int(b * W), int(c * W), int(dl * W), int(dr * W)
    if dl < 0: L = a[:, -dl:b]; Lc = a[:, :-dl]
    elif dl > 0: L = np.concatenate([cv2.flip(a[:, :dl], 1), a[:, :b]], 1); Lc = a[:, :0]
    else: L = a[:, :b]; Lc = a[:, :0]
    if dr > 0: R = a[:, c:W - dr]; Rc = a[:, W - dr:]
    elif dr < 0: R = np.concatenate([a[:, c:], cv2.flip(a[:, W + dr:], 1)], 1); Rc = a[:, :0]
    else: R = a[:, c:]; Rc = a[:, :0]
    g = W - L.shape[1] - R.shape[1]
    if modo == 'move':
        M = np.concatenate([Lc, a[:, b:c], Rc], 1)
        seams_rel = [Lc.shape[1], Lc.shape[1] + (c - b)]
        if M.shape[1] != g: M = cv2.resize(M, (g, h), interpolation=cv2.INTER_AREA); seams_rel = [int(s * g / max(1, Lc.shape[1] + c - b + Rc.shape[1])) for s in seams_rel]
    elif modo == 'white':
        M = cv2.resize(a[:, b:c], (g, h), interpolation=cv2.INTER_CUBIC).astype(np.float32)
        x = np.arange(g, dtype=np.float32); r = max(1.0, min(70.0, g / 3))
        t = np.clip(np.minimum(x, g - 1 - x) / r, 0, 1)[None, :, None]
        M = (M * (1 - t) + 255 * t).astype(np.uint8); seams_rel = []
    elif modo == 'tile':
        band = a[:, b:c]; parts = []; n = 0; i = 0; seams_rel = []
        while n < g:
            p = band if i % 2 == 0 else cv2.flip(band, 1); parts.append(p); n += p.shape[1]; i += 1; seams_rel.append(n)
        M = np.concatenate(parts, 1)[:, :g]; seams_rel = []
    else:
        M = cv2.resize(a[:, b:c], (g, h), interpolation=cv2.INTER_CUBIC); seams_rel = []
    out = np.concatenate([L, M, R], 1); x0 = L.shape[1]
    seams = [x0] + [x0 + s for s in seams_rel] + [x0 + g]
    return feather(out, seams) if modo in ('move','tile') else out
