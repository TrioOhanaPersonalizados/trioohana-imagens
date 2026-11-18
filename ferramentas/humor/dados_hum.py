import sys; sys.path.insert(0,'/home/claude/humd')
from nomes_hum import N
C, CER, TEM, HUM, FRA, PROF, DAT, DPROF, PET, CAPI = 42081740, 42081751, 42081747, 42081776, 42081816, 42081772, 42081779, 42081829, 42081769, 42081806
def blen(s): return len(s)+sum(1 for c in s if ord(c)>127)
BICHO = {'a02':'galinha','a03':'gata','a04':'guaxinim','a05':'gansa','a06':'capivara','a07':'vaquinha','a08':'raposa','a09':'lhama','a10':'pomba'}
STOP = {'o','a','e','de','do','da','um','uma','que','com','por','pra','para','sua','à','é','você','meu','minha','só','mas','aí','se','eu','não','nós','ela','já','sem','hoje','ninguém','tem','era'}
def titulo(nome):
    sh = nome.replace('Caneca ','').replace(' 325ml','')
    mt = f"Caneca {sh} | Trio Ohana"
    while blen(mt) > 70 or sh.split(' ')[-1].lower().rstrip(',') in STOP:
        sh = ' '.join(sh.split(' ')[:-1]).rstrip(','); mt = f"Caneca {sh} | Trio Ohana"
    return mt
def P(k):
    nome, cor, g, desc, f1, f2 = N[k]; n = nome.replace(' 325ml','')
    if g == 'a':
        b = BICHO[k]
        ab = (f"<p>A <strong>{n}</strong> fala por quem tem resposta pronta pra tudo. De um lado, {desc} chega com a frase <em>{f1}</em></p>\n"
              f"<p>Do outro, a mesma {b} completa: <em>{f2}</em> As ilustrações são cheias de detalhe, com margaridas, coraçõezinhos e um fio de linha colorida passando pela caneca.</p>\n"
              f"<p>É um <strong>presente divertido</strong> para quem leva a vida com ironia e estilo, e para aquela pessoa que sempre tem a última palavra.</p>")
        ideal = ["Amigo secreto e lembrança de fim de ano", "Aquela amiga irônica que tem resposta pra tudo", "Mesa do escritório e café com bom humor", "Presente de aniversário divertido"]
        md = f"Caneca de humor com {b} {'estiloso' if b=='guaxinim' else 'estilosa'} e a frase {f1.rstrip('…')}, {f2.lstrip('…').rstrip('.')}. Cerâmica 325ml, presente divertido."
        if blen(md) > 160: md = f"Caneca de humor com {b} e a frase {f1.rstrip('…')}, {f2.lstrip('…').rstrip('.')}. Cerâmica 325ml."
        if blen(md) > 160: md = f"Caneca de humor com {b} e a frase {f1.rstrip('…')}… Cerâmica 325ml, presente divertido."
        tags = ["caneca engraçada", "caneca de humor", "caneca com frase", "frases irônicas", "presente divertido", "amigo secreto", "caneca 325ml", "trio ohana", b]
        cats = [C, CER, TEM, HUM, FRA] + ([PET, CAPI] if k == 'a06' else [])
    else:
        ab = (f"<p>A <strong>{n}</strong> é para a professora que ama o que faz, mas já ouviu de tudo na sala de aula. A frase <em>{f1}</em> aparece em letras coloridas e fofinhas, nos dois lados da caneca.</p>\n"
              "<p>Em volta, lápis, maçã sorridente, livros empilhados, quadro-negro e estrelinhas, sobre um fundo de folha de caderno com furinhos de fichário.</p>\n"
              "<p>Um <strong>presente para professora</strong> que rende risada na sala dos professores, no Dia dos Professores ou no fim do ano letivo.</p>")
        ideal = ["Dia dos Professores e fim do ano letivo", "Lembrança da turma ou da escola para a professora", "Amigo secreto da sala dos professores", "Café com bom humor antes da aula"]
        fr = f1.replace('“','').replace('”','').rstrip('.'); fr = fr + ('' if fr[-1] in '?!' else '.')
        md = f"Caneca para professora com a frase {fr} Cerâmica 325ml, presente divertido para professora."
        if blen(md) > 160: md = f"Caneca para professora com a frase {fr} Cerâmica 325ml."
        tags = ["caneca para professora", "presente para professora", "dia dos professores", "caneca engraçada", "caneca de humor", "caneca com frase", "caneca 325ml", "trio ohana"]
        cats = [C, CER, TEM, HUM, FRA, PROF, DAT, DPROF]
    mt = titulo(nome)
    assert blen(mt) <= 70 and blen(md) <= 160, (k, blen(mt), blen(md))
    return dict(abertura=ab, meta_title=mt, meta_desc=md, tags=tags, ideal=ideal, cats=cats)
DADOS = {k: P(k) for k in N}
if __name__ == '__main__':
    for k, d in DADOS.items(): print(k, blen(d['meta_title']), d['meta_title'], '||', blen(d['meta_desc']), d['meta_desc'])
