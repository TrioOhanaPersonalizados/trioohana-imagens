import sys,json;sys.path.insert(0,'/home/claude/comfoto');sys.path.insert(0,'/home/claude/pack07')
from converte import job; from dados_cf import P
ids={1:381843747,2:381857812,4:381857818,5:381857821,6:381857824,7:381857827,8:381857832,9:381857839,10:381857842,11:381857846,12:381857852}
nome=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]]
itens=[]
for n in ns:
    itens+=job(ids[n],P[n],f'/home/claude/comfoto/c{n}/saida')
    itens.append({"op":"padrao_variantes","ref":f"c{n}","product_id":ids[n]})
json.dump({"itens":itens},open(f'/home/claude/trioohana-imagens/jobs/{nome}.json','w'),ensure_ascii=False)
