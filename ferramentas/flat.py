import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
src,dst=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGBA'); a=np.array(im)
alpha=a[:,:,3]
bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im); out=bg.convert('RGB')
# área transparente grande = moldura da foto -> texto "Sua foto aqui"
from scipy import ndimage
mask=alpha<10
if mask.sum()<im.size[0]*im.size[1]*0.03:
    rgb=np.array(out); mask=(rgb.min(axis=2)>=250)
lab,n=ndimage.label(mask)
sizes=ndimage.sum(np.ones_like(alpha),lab,range(1,n+1))
d=ImageDraw.Draw(out)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',int(im.size[1]*0.055))
for i,s in enumerate(sizes,1):
    if s>im.size[0]*im.size[1]*0.03:
        ys,xs=np.where(lab==i); cx,cy=xs.mean(),ys.mean(); w=xs.max()-xs.min()
        sz=int(im.size[1]*0.055)
        while sz>20:
            ff=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz)
            if d.textlength("SUA FOTO",font=ff)<=0.7*w: break
            sz-=4
        d.multiline_text((cx,cy),"SUA FOTO\nAQUI",font=ff,fill=(170,170,170),anchor='mm',align='center',spacing=sz//3)
        print('moldura',int(s),int(cx),int(cy))
out.save(dst)
