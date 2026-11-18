import json,importlib
N={}
for pre in ('p3','p2','p1'):
    M=importlib.import_module('nomes'+pre[1]).N
    for i,(n,c) in M.items(): N[f'{pre}_{i:02d}']=n
OLD={'gato':'Caneca de Natal Gatinho Noel 3D 325ml','neve':'Caneca de Natal Boneco de Neve Let it Snow 325ml',
'fe1':'Caneca de Natal Que o Natal Renove a sua Fé e a sua Esperança com Papai Noel 325ml',
'fe2':'Caneca de Natal Você é um Presente de Deus na Minha Vida com Laços Vermelhos 325ml',
'fe3':'Caneca de Natal Você é um Presente de Deus na Minha Vida com Foto 325ml',
'fe4':'Caneca de Natal Que o Natal Renove a sua Fé e a sua Esperança com Foto 325ml',
'f1':'Caneca Feliz Natal Querida Amiga com Foto 325ml','f2':'Caneca Feliz Natal com Papai Noel e Xadrez Vermelho com Foto 325ml',
'f3':'Caneca Feliz Fim de Ano com Muito Amor com 2 Fotos 325ml','f4':'Caneca Feliz Natal com Ramos de Pinheiro e Fita Vermelha com Foto 325ml',
'c1':'Caneca Feliz Natal Ho Ho Ho com Papai Noel e Árvore Enfeitada 325ml','c2':'Caneca Feliz Natal com Papai Noel e Xadrez Vermelho 325ml',
'c3':'Caneca Feliz Natal com Bolas de Natal Vermelhas e Pinheiro 325ml','c4':'Caneca Feliz Natal Querida Amiga com Papai Noel e Xadrez Verde 325ml',
'eq':'Caneca Uma Equipe Incrível Merece um Fim de Ano Incrível com Guirlanda de Natal 325ml'}
for k,v in OLD.items(): N[k]=v
G={
'noel':['p3_01','p3_02','p3_04','p3_06','p3_08','p3_09','p3_10','p2_03','p2_05','p2_06','c1','c2'],
'casal':['p3_03','p2_02','p2_07','p2_09','f3','p1_13'],
'fe':['p3_07','p2_01','p2_04','p2_08','p2_10','p1_07','p1_14','p1_12','fe1','fe2','fe3','fe4'],
'pet':['p3_05','gato','p1_08','p1_17','p2_09','p2_05','neve'],
'humor':['p1_21','p1_22','p1_23','p1_24','p1_25','p1_26','p3_06','p3_09','p2_05','p3_08'],
'foto':['p1_04','p1_06','p1_11','p1_13','f1','f2','f3','f4','fe3','fe4'],
'nome':['p1_15','p1_16','p1_18','p1_02','p1_01','p3_10'],
'classico':['p1_01','p1_02','p1_03','p1_08','p1_09','p1_10','p1_12','p1_17','p2_06','p2_09','p3_10','c3','c4','eq','neve'],
}
OF={'p3_01':'noel','p3_02':'noel','p3_03':'casal','p3_04':'noel','p3_05':'pet','p3_06':'humor','p3_07':'fe','p3_08':'noel','p3_09':'humor','p3_10':'noel',
'p2_01':'fe','p2_02':'casal','p2_03':'noel','p2_04':'fe','p2_05':'humor','p2_06':'classico','p2_07':'casal','p2_08':'fe','p2_09':'pet','p2_10':'fe',
'p1_01':'classico','p1_02':'classico','p1_03':'classico','p1_04':'foto','p1_06':'foto','p1_07':'fe','p1_08':'pet','p1_09':'classico','p1_10':'classico',
'p1_11':'foto','p1_12':'classico','p1_13':'foto','p1_14':'fe','p1_15':'nome','p1_16':'nome','p1_18':'nome','p1_17':'pet',
'p1_21':'humor','p1_22':'humor','p1_23':'humor','p1_24':'humor','p1_25':'humor','p1_26':'humor'}
SEC={'noel':'humor','casal':'foto','fe':'foto','pet':'classico','humor':'noel','foto':'nome','nome':'foto','classico':'noel'}
R={}
for idx,(k,g) in enumerate(OF.items()):
    pool=[x for x in G[g] if x!=k]; off=idx%max(1,len(pool)); pool=pool[off:]+pool[:off]
    sel=pool[:5]
    sec=[x for x in G[SEC[g]] if x!=k and x not in sel]; o2=idx%len(sec); sec=sec[o2:]+sec[:o2]
    sel+= sec[:6-len(sel)]
    R[k]=[N[x] for x in sel]
json.dump(R,open('rel.json','w'),ensure_ascii=False)
for k in ('p3_01','p3_02','p1_15'): print(k,[x[16:50] for x in R[k]])
