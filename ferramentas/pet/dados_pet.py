import sys; sys.path.insert(0,'/home/claude/petd')
from nomes_pet import N
C, CER, TEM, PET, GATOS, CAES = 42081740, 42081751, 42081747, 42081769, 42081804, 42081805
def blen(s): return len(s)+sum(1 for c in s if ord(c)>127)
RACA = {'p9_01':'pastor-alemão','p9_02':'poodle','p9_03':'dálmata','p9_04':'pit bull','p9_05':'buldogue francês','p9_06':'border collie','p9_07':'shiba inu','p9_08':'dachshund','p9_09':'golden retriever','p9_10':'jack russell','p9_11':'maltês','p9_12':'lhasa apso','p9_13':'boxer','p9_14':'shih tzu','p9_15':'cocker spaniel','p9_16':'rottweiler','p9_17':'pug','p9_18':'yorkshire','p9_19':'vira-lata',
 'p8_01':'weimaraner','p8_02':'pinscher','p8_03':'yorkshire','p8_04':'pastora-alemã','p8_05':'boxer','p8_06':'jack russell','p8_07':'pug','p8_08':'schnauzer','p8_09':'basset hound','p8_18':'rottweiler','p8_20':'rottweiler','dn_golden':'golden retriever',
 'p8_13':'persa','p8_14':'devon rex','p8_16':'ragdoll','gn_02':'persa','gn_03':'siamês','gn_06':'sphynx','gn_10':'bengal'}
def curto(nome):
    s = nome.replace('Caneca ','').replace(' 325ml','')
    return s
def P(k):
    nome, cor, an, desc, frase = N[k]; fam = k[:2]; raca = RACA.get(k)
    cao = an == 'c'
    bicho = 'cachorro' if cao else 'gato'
    if fam == 'p9':
        ab = (f"<p>A <strong>{nome.replace(" 325ml","")}</strong> é para quem conhece bem o temperamento do próprio cachorro. De um lado, {desc} em ilustração realista, cercado de pinceladas coloridas, coroa, corações e patinhas.</p>\n"
              f"<p>Do outro, a frase <em>{frase}</em> em letras grandes, no estilo de pincel e caneta, com fundo de tinta em rosa, amarelo, azul e laranja.</p>\n"
              f"<p>Um <strong>presente para tutor de {raca}</strong> que ri das manias do pet e gosta de começar o dia com bom humor.</p>")
        ideal = [f"Tutores de {raca}" if raca!='vira-lata' else "Tutores de vira-lata, os famosos SRD", "Amigo secreto e lembrança de fim de ano", "Quem ama humor de pet no café da manhã", "Presente para veterinários, banhistas e tosadores"]
    elif fam == 'p8':
        ab = (f"<p>A <strong>{nome.replace(" 325ml","")}</strong> traz a frase <em>{frase}</em> em letras de caligrafia coloridas, cercada de corações, patinhas e estrelinhas.</p>\n"
              f"<p>Do outro lado, {desc} em ilustração detalhada, sobre um fundo branco com manchas de aquarela em tons pastel.</p>\n"
              f"<p>É um <strong>presente para quem ama {'cachorro' if cao else 'gato'}</strong> e trata o pet como parte da família.</p>")
        ideal = [f"Tutores de {raca}" if raca else ("Mães e pais de gato" if not cao else "Mães e pais de cachorro"), "Presente de aniversário ou Natal para quem ama pets", "Amigo secreto e lembrança de fim de ano", "Clínicas veterinárias e pet shops"]
    elif fam in ('gn','dn'):
        ab = (f"<p>A <strong>{nome.replace(" 325ml","")}</strong> tem {desc}, em ilustração cheia de detalhes nos pelos e no olhar, repetida nos dois lados da caneca.</p>\n"
              f"<p>O fundo preto faz as cores vibrarem: rosa, azul, verde, amarelo e laranja em respingos de tinta, com acabamento de pincel nas bordas.</p>\n"
              f"<p>Um <strong>presente para quem ama {'cachorro' if cao else 'gato'}</strong> e gosta de peças coloridas e marcantes.</p>")
        ideal = [f"Tutores de {raca}" if raca else ("Mães e pais de gato" if not cao else "Tutores de golden retriever"), "Quem gosta de arte colorida e estilo neon", "Presente de aniversário ou Natal para quem ama pets", "Decorar a mesa do escritório com personalidade"]
    else:
        ab = (f"<p>A <strong>{nome.replace(" 325ml","")}</strong> tem {desc} em ilustração fofa e a frase <em>{frase}</em> em letras bem marcadas.</p>\n"
              f"<p>O fundo claro e delicado deixa o gatinho e a frase em destaque, cada um de frente em um lado da caneca.</p>\n"
              f"<p>Um <strong>presente para quem ama gatos</strong> e não esconde isso de ninguém.</p>")
        ideal = ["Mães e pais de gato", "Presente de aniversário ou Natal para quem ama gatos", "Amigo secreto e lembrança de fim de ano", "Café ou chá com companhia felina"]
    base_t = ["caneca pet", "caneca de cachorro" if cao else "caneca de gato", "presente para tutor", "presente para quem ama " + ("cachorro" if cao else "gatos"), "caneca 325ml", "trio ohana"]
    if raca: base_t.append(raca)
    if fam in ('gn','dn'): base_t.append("neon")
    if fam in ('p9',): base_t.append("caneca divertida")
    if not cao: base_t += ["mae de gato", "gateira"] if fam!='p9' else []
    sh = curto(nome)
    mt = f"Caneca {sh} | Trio Ohana"
    STOP = {'o','a','e','de','do','da','um','uma','que','com','por','pra','sua','à','é','você','meu','minha','a sua'}
    while blen(mt) > 70 or sh.split(' ')[-1].lower().rstrip(',') in STOP:
        sh = ' '.join(sh.split(' ')[:-1]).rstrip(','); mt = f"Caneca {sh} | Trio Ohana"
    if frase:
        art = desc.split(' ')[0]; quem = f"{art} {raca}" if raca else {'g':'um gatinho','c':'um cachorro'}[an]
        if not raca and 'laranja' in desc: quem = 'um gatinho laranja'
        if not raca and 'tigrado' in desc: quem = 'um gato tigrado'
        if not raca and 'ruivo' in desc: quem = 'um gato ruivo'
        if not raca and 'preto' in desc: quem = 'um gatinho preto'
        md = f"Caneca de {bicho} com {quem} e a frase {frase.rstrip('.')}{'' if frase.rstrip('.')[-1] in '?!' else '.'} Cerâmica 325ml, presente para tutor."
    else:
        md = f"Caneca com {desc}. Cerâmica 325ml com cores vibrantes, presente para quem ama {'cachorro' if cao else 'gatos'}."
    if blen(md) > 160:
        md = f"Caneca de {bicho} com a frase {frase.rstrip('.')}{'' if frase.rstrip('.')[-1] in '?!' else '.'} Cerâmica 325ml, presente para tutor."
    if blen(md) > 160:
        md = md[:150].rsplit(' ',1)[0] + '.'
    cats = [C, CER, TEM, PET, CAES if cao else GATOS]
    return dict(abertura=ab, meta_title=mt, meta_desc=md, tags=base_t, ideal=ideal, cats=cats)
DADOS = {k: P(k) for k in N}
if __name__ == '__main__':
    for k, d in DADOS.items(): print(k, blen(d['meta_title']), d['meta_title'], '||', blen(d['meta_desc']), d['meta_desc'])
