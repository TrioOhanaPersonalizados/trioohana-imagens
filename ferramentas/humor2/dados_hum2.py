import sys; sys.path.insert(0,'/home/claude/hum2d')
from nomes_hum2 import N
C, CER, TEM, HUM, FRA, CAFE = 42081740, 42081751, 42081747, 42081776, 42081816, 42081778
def blen(s): return len(s)+sum(1 for c in s if ord(c)>127)
STOP = {'o','a','e','de','do','da','um','uma','que','com','por','pra','para','sua','à','é','você','meu','minha','só','mas','aí','se','eu','não','nós','ela','já','sem','hoje','ninguém','tem','era','em','me','mim','igual','tô','nem','estou'}
def titulo(nome):
    sh = nome.replace('Caneca ','').replace(' 325ml','')
    mt = f"Caneca {sh} | Trio Ohana"
    while blen(mt) > 70 or sh.split(' ')[-1].lower().rstrip(',') in STOP:
        sh = ' '.join(sh.split(' ')[:-1]).rstrip(','); mt = f"Caneca {sh} | Trio Ohana"
    return mt
def P(k):
    nome, cor, b, desc, frase = N[k]; n = nome.replace(' 325ml','')
    cafe = 'café' in frase.lower() or 'cafeinada' in frase.lower()
    ab = (f"<p>A <strong>{n}</strong> é para quem leva a rotina com bom humor. A estampa traz {desc} e a frase <em>{frase}</em></p>\n"
          "<p>O desenho é fofo, de traço simples e cores alegres, sobre fundo branco, e aparece de frente dos dois lados da caneca, para quem é destro ou canhoto.</p>\n"
          f"<p>Um <strong>presente divertido</strong> que serve para amigo, colega de trabalho, irmão, mãe ou para você mesmo{', especialmente se o dia só começa depois do café' if cafe else ''}.</p>")
    ideal = ["Amigo secreto e lembrança de fim de ano", "Presente divertido para qualquer idade", "Mesa do escritório ou home office", "Quem se identifica com a frase (todo mundo)"]
    fr = frase.rstrip('.'); fr = fr.replace(' ✓',''); fr = fr + ('' if fr[-1] in '?!' else '.')
    md = f"Caneca de humor com {b} e a frase {fr} Cerâmica 325ml, presente divertido."
    if blen(md) > 160: md = f"Caneca de humor com {b} e a frase {fr} Cerâmica 325ml."
    if blen(md) > 160: md = f"Caneca de humor com {b}: {fr} Cerâmica 325ml."
    tags = ["caneca engraçada", "caneca de humor", "caneca com frase", "caneca fofa", "presente divertido", "amigo secreto", "caneca 325ml", "trio ohana", b] + (["caneca de café"] if cafe else [])
    cats = [C, CER, TEM, HUM, FRA] + ([CAFE] if cafe else [])
    mt = titulo(nome)
    assert blen(mt) <= 70 and blen(md) <= 160, (k, blen(mt), blen(md))
    return dict(abertura=ab, meta_title=mt, meta_desc=md, tags=tags, ideal=ideal, cats=cats)
DADOS = {k: P(k) for k in N}
if __name__ == '__main__':
    for k, d in DADOS.items(): print(k, blen(d['meta_title']), d['meta_title'], '||', blen(d['meta_desc']), d['meta_desc'])
