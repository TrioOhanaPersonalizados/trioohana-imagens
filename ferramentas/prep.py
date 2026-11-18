import sys, numpy as np, cv2
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); a = np.array(im); h, w = a.shape[:2]
nh = round(w / (20.7 / 9.7)); extra = nh - h; top = extra // 2; bot = extra - top
b = cv2.copyMakeBorder(a, top, bot, 0, 0, cv2.BORDER_REFLECT)
Image.fromarray(b).save(dst, dpi=(300, 300)); print(src.split('/')[-1], (w, h), '->', b.shape[1::-1], 'top', top, 'bot', bot)
