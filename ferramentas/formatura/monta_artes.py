import sys, glob, subprocess, os
from PIL import Image, ImageDraw, ImageFont
T='/tmp/claude-tool-results/44fbacd1-6c49-5b9a-8c79-ff087943fd2b'
P13='70ypk3 1dxbkr 6g8rlb y5q4tu 2uyxmm pk0tsi zmjtda feyy33 jivn00 6up6py bz34hh jbg2v4 cx03rn iktcwn pd1yqf p7026l hcyj9i tiegay'.split()
P12='34dwrk 2g1qau ss5zsk pgystk wrxnk6 wc25gn 4mwwhy csf6zw 23w0ys wob7tl'.split()
P11={1:'ks735s',3:'hrs80m',4:'gpbqds'}
DS='/home/claude/fontes/dancing-script-latin-700-normal.ttf'
src={}
for i,c in enumerate(P13,1): src[f'a{i:02d}']=(c,'foto')
for i,c in enumerate(P12,1): src[f'b{i:02d}']=(c,'plain')
for i,c in P11.items(): src[f'c{i:02d}']=(c,'plain')
NOMES={'b01':('Miguel',(350,545),120,(20,20,20)),'b02':('Helena',(345,650),140,(20,20,20)),'b04':('Miguel',(335,505),105,(40,160,232))}
for k,(c,mode) in src.items():
    f=glob.glob(f'{T}/*-{c}-*')[0]; d=f'w/{k}'; os.makedirs(d,exist_ok=True)
    if mode=='foto':
        subprocess.run(['python3','-I','/home/claude/comfoto/flat.py',f,f'{d}/flat.png'],check=True,capture_output=True)
    else:
        im=Image.open(f).convert('RGBA'); bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im); bg=bg.convert('RGB')
        if k in NOMES:
            t,(x,y),s,cor=NOMES[k]; dr=ImageDraw.Draw(bg); dr.text((x,y),t,font=ImageFont.truetype(DS,s),fill=cor,anchor='mm')
        bg.save(f'{d}/flat.png')
    subprocess.run(['python3','-I','/home/claude/prep.py',f'{d}/flat.png',f'{d}/prep.png'],check=True,capture_output=True)
    r=subprocess.run(['python3','-I','/home/claude/centra/centra.py',f'{d}/prep.png',f'{d}/arte_pronta.png'],capture_output=True,text=True)
    print(k,r.stdout.strip()[:160],r.stderr[-200:])
