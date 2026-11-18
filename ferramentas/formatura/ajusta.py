"""Empurra os motivos de cada lado para a frente da caneca (18,9% e 81,1% da largura).
Translada o bloco esquerdo em dl e o direito em dr; o vão central é esticado/encolhido; o que passa da borda (lado da alça) é descartado."""
import numpy as np, cv2, sys, json
from PIL import Image
def ajusta(a, b, c, dl, dr):
    h, W = a.shape[:2]
    L = a[:, -dl:b] if dl < 0 else np.concatenate([cv2.flip(a[:, :dl], 1), a[:, :b]], 1) if dl > 0 else a[:, :b]
    R = a[:, c:W - dr] if dr > 0 else np.concatenate([a[:, c:], cv2.flip(a[:, W + dr:], 1)], 1) if dr < 0 else a[:, c:]
    g = W - L.shape[1] - R.shape[1]
    G = cv2.resize(a[:, b:c], (g, h), interpolation=cv2.INTER_CUBIC)
    return np.concatenate([L, G, R], 1)
if __name__ == '__main__':
    src, dst, b, c, dl, dr = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:7])
    a = np.array(Image.open(src).convert('RGB')); W = a.shape[1]
    b, c = int(b * W), int(c * W); dl, dr = int(dl), int(dr)
    out = ajusta(a, b, c, dl, dr); assert out.shape == a.shape
    Image.fromarray(out).save(dst, dpi=(300, 300)); print(json.dumps({"b": b, "c": c, "dl": dl, "dr": dr}))
