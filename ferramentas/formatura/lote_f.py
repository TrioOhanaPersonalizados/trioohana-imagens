import sys,json;sys.path.insert(0,'/home/claude/comfoto');sys.path.insert(0,'/home/claude/pack07');sys.path.insert(0,'/home/claude/form')
from converte import job; from dados_f import P; from nomesf import N
ids=json.load(open('/home/claude/form/ids.json'))
nome=sys.argv[1]; itens=[]
for k in sys.argv[2:]:
    d=dict(P[k]); d['nome']=N[k][0]; d['abertura']=d['abertura'].replace('@@NOME@@',N[k][0].replace(' 325ml',''))
    itens+=job(int(ids[k]),d,f'/home/claude/form/w/{k}/saida'); itens.append({"op":"padrao_variantes","ref":k,"product_id":int(ids[k])})
json.dump({"itens":itens},open(f'/home/claude/trioohana-imagens/jobs/{nome}.json','w'),ensure_ascii=False); print(len(itens))
