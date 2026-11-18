import sys,json;sys.path.insert(0,'/home/claude/petd');sys.path.insert(0,'/home/claude/comfoto');sys.path.insert(0,'/home/claude/pack07');sys.path.insert(0,'/home/claude/petd')
from converte import job; from dados_pet import DADOS; from nomes_pet import N
ids=json.load(open('/home/claude/petd/ids.json'))
nome=sys.argv[1]; itens=[]
for k in sys.argv[2:]:
    d=dict(DADOS[k]); d['nome']=N[k][0]
    ops=job(int(ids[k]),d,f'/home/claude/pet/w/{k}/saida'); ops[-1]['padrao']=True; itens+=ops
json.dump({"itens":itens},open(f'/home/claude/trioohana-imagens/jobs/{nome}.json','w'),ensure_ascii=False); print(len(itens))
