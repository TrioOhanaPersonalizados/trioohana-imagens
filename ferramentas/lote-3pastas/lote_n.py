import sys,json,importlib;sys.path.insert(0,'/home/claude/comfoto');sys.path.insert(0,'/home/claude/pack07');sys.path.insert(0,'/home/claude/novas')
from converte import job
ids=json.load(open('/home/claude/novas/ids.json'))
nome=sys.argv[1]; keys=sys.argv[2:]
itens=[]
for k in keys:
    pre,n=k.split('_'); n=int(n)
    P=importlib.import_module('dados_'+pre).P; N=importlib.import_module('nomes'+pre[1]).N
    d=dict(P[n]); d['nome']=N[n][0]
    it=job(ids[k],d,f'/home/claude/novas/{k}/saida')
    if d.get('published') is False: it[0]['product']['published']=False
    itens+=it; itens.append({"op":"padrao_variantes","ref":k,"product_id":ids[k]})
json.dump({"itens":itens},open(f'/home/claude/trioohana-imagens/jobs/{nome}.json','w'),ensure_ascii=False)
print(len(itens))
