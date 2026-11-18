import sys,json;sys.path.insert(0,'/home/claude/hum2d');sys.path.insert(0,'/home/claude/comfoto');sys.path.insert(0,'/home/claude/pack07');sys.path.insert(0,'/home/claude/hum2d')
from converte import job; from dados_hum2 import DADOS; from nomes_hum2 import N
ids=json.load(open('/home/claude/hum2d/ids.json'))
nome=sys.argv[1]; itens=[]
for k in sys.argv[2:]:
    d=dict(DADOS[k]); d['nome']=N[k][0]
    ops=job(int(ids[k]),d,f'/home/claude/hum2/w/{k}/saida'); ops[-1]['padrao']=True; itens+=ops
json.dump({"itens":itens},open(f'/home/claude/trioohana-imagens/jobs/{nome}.json','w'),ensure_ascii=False); print(len(itens))
