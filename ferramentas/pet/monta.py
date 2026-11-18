import sys, glob, subprocess, os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
def run(f):
    k=os.path.basename(f).split('.')[0]; d=f'w/{k}'; os.makedirs(d,exist_ok=True)
    im=Image.open(f).convert('RGBA'); bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im); bg.convert('RGB').save(f'{d}/flat.png')
    subprocess.run(['python3','-I','/home/claude/prep.py',f'{d}/flat.png',f'{d}/prep.png'],check=True,capture_output=True)
    r=subprocess.run(['python3','-I','/home/claude/centra/centra.py',f'{d}/prep.png',f'{d}/arte_pronta.png'],capture_output=True,text=True)
    return k+' '+r.stdout.strip()[:200]+r.stderr[-200:]
fs=sorted(glob.glob('src/*'))
with ThreadPoolExecutor(6) as ex:
    for s in ex.map(run,fs): print(s)
