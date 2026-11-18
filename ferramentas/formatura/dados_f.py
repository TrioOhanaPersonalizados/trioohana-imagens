B = [42081740, 42081751, 42081747, 42081770, 42081779]
T = ["caneca de formatura", "formatura abc", "formatura infantil", "lembrança de formatura", "presente de formatura", "caneca 325ml", "trio ohana"]
TF = T + ["caneca com foto e nome", "caneca personalizada com foto"]
TN = T + ["caneca com nome", "caneca personalizada com nome"]
FOTO_NOTA = "A foto e o nome da imagem são ilustrativos: na caneca entram a foto e o nome que você enviar."
NOME_NOTA = "O nome da imagem é só um exemplo: na caneca entra o nome que você enviar."
IDEAL_A = ["Lembrança de formatura do ABC e da educação infantil", "Presente dos pais, avós e padrinhos para o formando", "Kit de formatura da turma, com o nome de cada criança", "Presente da escola ou da professora para os alunos"]

def A(frase, quem, mt, md, extra_tags):
    ab = (f"<p>A <strong>@@NOME@@</strong> é a lembrança da formatura do ABC com a foto e o nome {quem}. "
          "De um lado, uma moldura em azul ou rosa com fita de washi tape e o selo <em>Formatura 2026</em> recebe a foto; embaixo, uma faixa amarela leva o nome.</p>\n"
          f"<p>Do outro lado, a frase <em>{frase}</em> vem em letras coloridas, com capelo, livros e lápis, sobre um fundo branco com respingos de cor.</p>\n"
          f"<p>É um <strong>presente de formatura</strong> para guardar o dia em que tudo começou. {FOTO_NOTA}</p>")
    return dict(abertura=ab, meta_title=mt, meta_desc=md, tags=TF + extra_tags, ideal=IDEAL_A)

P = {
'a01': A("Um pequeno formando com sonhos gigantes!", "do formando", "Caneca Formatura ABC Pequeno Formando com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome do formando e a frase Um pequeno formando com sonhos gigantes. Lembrança e presente de formatura.", ["formando"]),
'a02': A("Somos eternos aprendizes, e esse é só o primeiro passo!", "da criança", "Caneca Formatura ABC Eternos Aprendizes com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Somos eternos aprendizes, e esse é só o primeiro passo. Lembrança de formatura.", ["primeiro passo"]),
'a03': A("Que o sucesso acompanhe cada novo passo da sua caminhada!", "da criança", "Caneca Formatura ABC Sucesso a Cada Passo com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Que o sucesso acompanhe cada novo passo da sua caminhada. Presente de formatura.", ["sucesso"]),
'a04': A("Pequenos passos, grandes conquistas!", "da criança", "Caneca Formatura ABC Pequenos Passos com Foto e Nome | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Pequenos passos, grandes conquistas. Lembrança da formatura da educação infantil.", ["grandes conquistas"]),
'a05': A("Pequenos começos criam grandes histórias.", "da criança", "Caneca Formatura ABC Grandes Histórias com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Pequenos começos criam grandes histórias. Presente e lembrança de formatura.", ["grandes historias"]),
'a06': A("O primeiro passo para um futuro brilhante começa aqui.", "da criança", "Caneca Formatura ABC Futuro Brilhante com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase O primeiro passo para um futuro brilhante começa aqui. Lembrança de formatura.", ["futuro brilhante"]),
'a07': A("Minhas primeiras letras, meu primeiro diploma!", "da criança", "Caneca Formatura ABC Meu Primeiro Diploma com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Minhas primeiras letras, meu primeiro diploma. Presente de formatura infantil.", ["primeiro diploma"]),
'a08': A("Minha primeira formatura!", "da criança", "Caneca Minha Primeira Formatura ABC com Foto e Nome | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Minha primeira formatura. Lembrança da formatura do ABC e da educação infantil.", ["minha primeira formatura"]),
'a09': A("Formatura ABC: o primeiro de muitos diplomas.", "da criança", "Caneca Formatura ABC Primeiro de Muitos Diplomas | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Formatura ABC: o primeiro de muitos diplomas. Presente e lembrança de formatura.", ["diploma"]),
'a10': A("Do rabisco às primeiras letras: missão cumprida!", "da criança", "Caneca Formatura ABC Do Rabisco às Letras com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Do rabisco às primeiras letras: missão cumprida. Lembrança de formatura.", ["missao cumprida"]),
'a11': A("Cresci, aprendi e agora vou para o 1º ano!", "da criança", "Caneca Formatura ABC Agora Vou para o 1º Ano | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Cresci, aprendi e agora vou para o 1º ano. Presente de formatura infantil.", ["primeiro ano"]),
'a12': A("Festejamos o fim. O recomeço já bate à porta!", "da criança", "Caneca Formatura ABC O Recomeço Já Bate à Porta | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Festejamos o fim. O recomeço já bate à porta. Lembrança de formatura.", ["recomeço"]),
'a13': A("Cada letra aprendida foi uma grande conquista.", "da criança", "Caneca Formatura ABC Cada Letra uma Conquista | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Cada letra aprendida foi uma grande conquista. Presente de formatura.", ["alfabetizacao"]),
'a14': A("Aprender a ler é descobrir que o mundo é um livro aberto.", "da criança", "Caneca Formatura ABC Aprender a Ler com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Aprender a ler é descobrir que o mundo é um livro aberto. Lembrança de formatura.", ["aprender a ler"]),
'a15': A("ABC: aventuras, brincadeiras, conquistas!", "da criança", "Caneca Formatura ABC Aventuras e Conquistas com Foto | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase ABC: aventuras, brincadeiras, conquistas. Presente e lembrança de formatura.", ["aventuras"]),
'a16': A("Meu pequeno grande orgulho!", "do formando", "Caneca Formatura ABC Meu Pequeno Grande Orgulho | Trio Ohana",
         "Caneca de formatura ABC com foto e nome e a frase Meu pequeno grande orgulho. Presente dos pais e avós para o formando.", ["orgulho", "formando"]),
'a17': A("Minha pequena, meu grande orgulho!", "da formanda", "Caneca Formatura ABC Minha Pequena, Meu Orgulho | Trio Ohana",
         "Caneca de formatura ABC rosa com foto e nome e a frase Minha pequena, meu grande orgulho. Presente dos pais e avós para a formanda.", ["orgulho", "formanda"]),
'a18': A("Uma pequena formanda com sonhos gigantes!", "da formanda", "Caneca Formatura ABC Pequena Formanda com Foto | Trio Ohana",
         "Caneca de formatura ABC rosa com foto e nome e a frase Uma pequena formanda com sonhos gigantes. Lembrança e presente de formatura.", ["formanda"]),
}

def S(ab, mt, md, tags, ideal):
    return dict(abertura=ab, meta_title=mt, meta_desc=md, tags=tags, ideal=ideal)

IDEAL_B = ["Lembrança de formatura do ABC para a turma", "Presente dos pais, avós e padrinhos", "Professoras e escolas de educação infantil", "Primeira caneca da criança, para leite ou achocolatado"]
P.update({
'b01': S(f"<p>A <strong>Caneca Formatura ABC do Menino com Trenzinho e Dinossauro com Nome</strong> traz <em>ABC do</em> e o nome da criança em letra cursiva, com números coloridos, estrelas, mãozinhas pintadas e um dinossauro de lápis na mão.</p>\n<p>Embaixo, um trenzinho leva os vagões A, B e C, e capelos de formatura aparecem pela caneca toda, sobre um fundo branco com desenhos escolares bem suaves.</p>\n<p>É uma <strong>lembrança de formatura</strong> alegre para a turma do ABC. {NOME_NOTA}</p>",
         "Caneca Formatura ABC com Trenzinho e Nome | Trio Ohana", "Caneca de formatura ABC com o nome da criança, trenzinho do ABC, dinossauro, estrelas e mãozinhas. Lembrança de formatura infantil.", TN + ["trenzinho", "dinossauro"], IDEAL_B),
'b02': S(f"<p>A <strong>Caneca Formatura ABC com Tigre, Leão e Lapisinhos com Nome</strong> tem <em>ABC do</em> e o nome da criança em letras coloridas, com um tigrinho, um leão lendo e lapisinhos de carinha sorridente.</p>\n<p>O fundo quadriculado lembra o caderno de escola, com abelhinhas, corações e letrinhas espalhadas.</p>\n<p>É uma <strong>lembrança de formatura</strong> divertida para meninos e meninas. {NOME_NOTA}</p>",
         "Caneca Formatura ABC Tigre e Leão com Nome | Trio Ohana", "Caneca de formatura ABC com o nome da criança, tigrinho, leão lendo e lapisinhos sobre fundo de caderno. Lembrança de formatura.", TN + ["tigre", "leao"], IDEAL_B),
'b03': S(f"<p>A <strong>Caneca Formatura do ABC Quadriculado Verde com Ursinho e Foto</strong> traz <em>Formatura do ABC</em> com um capelo, um ursinho lendo, um leão no carrinho e um globo terrestre, sobre fundo quadriculado verde.</p>\n<p>Do outro lado, uma moldura estilo polaroide com fita adesiva recebe a foto da criança.</p>\n<p>É uma <strong>lembrança de formatura com foto</strong> para guardar o fim da educação infantil. A imagem dentro da moldura é ilustrativa: na caneca entra a foto que você enviar.</p>",
         "Caneca Formatura do ABC Quadriculado com Foto | Trio Ohana", "Caneca de formatura do ABC com foto em moldura polaroide, ursinho, leão e globo sobre quadriculado verde. Lembrança de formatura.", TF + ["ursinho"], IDEAL_B),
'b04': S(f"<p>A <strong>Caneca Formatura ABC com Bandeirinhas e Mãozinhas com Nome</strong> tem bandeirinhas com A, B e C, o texto <em>ABC do</em> e o nome da criança, com mãozinhas pintadas, capelos e números.</p>\n<p>O fundo branco tem letrinhas coloridas bem clarinhas, e um globo com livros e lápis completa a arte.</p>\n<p>É uma <strong>lembrança de formatura</strong> leve e colorida. {NOME_NOTA}</p>",
         "Caneca Formatura ABC Bandeirinhas com Nome | Trio Ohana", "Caneca de formatura ABC com o nome da criança, bandeirinhas ABC, mãozinhas pintadas e capelos. Lembrança de formatura infantil.", TN + ["bandeirinhas"], IDEAL_B),
'b05': S("<p>A <strong>Caneca Formatura ABC Caderno Pautado com Ursinho e Foto</strong> imita uma folha de caderno com linhas azuis e um varal colorido no alto, com um ursinho lendo, lapisinhos, uma banana e uma lagarta de óculos.</p>\n<p>Uma moldura estilo polaroide presa com clipe recebe a foto da criança.</p>\n<p>É uma <strong>lembrança de formatura com foto</strong> para a turma do ABC. A imagem dentro da moldura é ilustrativa: na caneca entra a foto que você enviar.</p>",
         "Caneca Formatura ABC Caderno com Foto | Trio Ohana", "Caneca de formatura ABC com foto, folha de caderno pautado, ursinho lendo e lapisinhos. Lembrança de formatura da educação infantil.", TF + ["caderno"], IDEAL_B),
'b06': S("<p>A <strong>Caneca Formatura ABC Menina Rabiscos e Capelos Rosa</strong> tem traço de rabisco infantil: menininhas desenhadas, capelos e mãozinhas rosa, lousas com ABC e um varal de bolinhas coloridas no alto.</p>\n<p>O fundo branco leva letrinhas bem clarinhas e corações.</p>\n<p>É uma <strong>lembrança de formatura</strong> delicada para meninas. Se quiser, a gente inclui o nome da formanda.</p>",
         "Caneca Formatura ABC Menina Rabiscos Rosa | Trio Ohana", "Caneca de formatura ABC com menininhas em rabisco, capelos e mãozinhas rosa e lousas com ABC. Lembrança de formatura para meninas.", T + ["formanda", "rosa"], IDEAL_B),
'b07': S("<p>A <strong>Caneca Formatura ABC Arco-Íris e Bandeirinhas com Foto</strong> tem bandeirinhas com A, B e C e uma moldura estilo polaroide presa com fita rosa para a foto da criança.</p>\n<p>Arco-íris, flores, abelhinhas, corações e letrinhas em tons pastel se espalham pela caneca.</p>\n<p>É uma <strong>lembrança de formatura com foto</strong> em cores suaves. A imagem dentro da moldura é ilustrativa: na caneca entra a foto que você enviar.</p>",
         "Caneca Formatura ABC Arco-Íris com Foto | Trio Ohana", "Caneca de formatura ABC com foto, bandeirinhas, arco-íris, flores e abelhinhas em tons pastel. Lembrança de formatura infantil.", TF + ["arco-iris"], IDEAL_B),
'b08': S("<p>A <strong>Caneca Formatura do ABC Rosa com Ursinhas e Capelos</strong> traz <em>Formatura do ABC</em> com capelos rosa, ursinhas lendo, lapisinhos e uma bonequinha voando de lápis, sobre quadriculado rosa.</p>\n<p>Do outro lado, letras ABC penduradas e mais capelos completam a arte.</p>\n<p>É uma <strong>lembrança de formatura</strong> fofa para meninas. Se quiser, a gente inclui o nome da formanda.</p>",
         "Caneca Formatura do ABC Rosa com Ursinhas | Trio Ohana", "Caneca de formatura do ABC rosa com ursinhas lendo, capelos e lapisinhos sobre quadriculado. Lembrança de formatura para meninas.", T + ["formanda", "rosa", "ursinha"], IDEAL_B),
'b09': S("<p>A <strong>Caneca Formatura ABC Caderno Rosa com Ursinha</strong> imita uma folha de caderno com linhas rosa, com um bloquinho quadriculado escrito ABC, uma ursinha de mochila e capelos rosa.</p>\n<p>Florzinhas, abelhinhas, coraçõezinhos e mais ABC se espalham pela caneca.</p>\n<p>É uma <strong>lembrança de formatura</strong> delicada. Se quiser, a gente inclui o nome da formanda.</p>",
         "Caneca Formatura ABC Caderno Rosa | Trio Ohana", "Caneca de formatura ABC com folha de caderno rosa, ursinha de mochila, capelos e florzinhas. Lembrança de formatura para meninas.", T + ["formanda", "rosa", "caderno"], IDEAL_B),
'b10': S("<p>A <strong>Caneca Formatura do ABC com Solzinhos e Livros</strong> tem <em>Formatura do ABC</em> em letras amarelas e rosa, com solzinhos sorridentes, livros abertos, lousinhas, cubos de letras e lápis.</p>\n<p>O fundo branco tem estrelinhas e desenhos escolares bem suaves.</p>\n<p>É uma <strong>lembrança de formatura</strong> alegre para a turma inteira. Se quiser, a gente inclui o nome da criança.</p>",
         "Caneca Formatura do ABC Solzinhos e Livros | Trio Ohana", "Caneca de formatura do ABC com solzinhos sorridentes, livros abertos, lousinhas e cubos de letras. Lembrança de formatura da turma.", T + ["livros"], IDEAL_B),
'c01': S(f"<p>A <strong>Caneca Minha Primeira Formatura ABC com Foto e Nome</strong> tem uma moldura verde com fita rosa para a foto do formando, um lápis gigante e uma estrela lilás.</p>\n<p>Do outro lado, <em>Minha primeira Formatura</em> em letras coloridas, com as letrinhas A, B e C de carinha feliz e o nome da criança na faixa verde.</p>\n<p>É um <strong>presente de formatura</strong> para guardar a primeira conquista. {FOTO_NOTA}</p>",
         "Caneca Minha Primeira Formatura ABC Foto e Nome | Trio Ohana", "Caneca Minha Primeira Formatura ABC com foto e nome da criança, letrinhas ABC de carinha feliz e lápis gigante. Presente de formatura.", TF + ["minha primeira formatura"], IDEAL_A),
'c03': S(f"<p>A <strong>Caneca Lembrança da Minha Formatura ABC com Foto e Nome</strong> traz uma lousa com <em>Lembrança da minha Formatura</em> em letras coloridas, com livros, lápis, uma caneca e uma maçã de carinha feliz.</p>\n<p>Do outro lado, uma moldura amarela com borda verde recebe a foto, com as letrinhas ABC, um arco-íris, um livro sorridente e o nome da criança.</p>\n<p>É um <strong>presente de formatura</strong> delicado, em tons pastel. {FOTO_NOTA}</p>",
         "Caneca Lembrança da Minha Formatura com Foto | Trio Ohana", "Caneca Lembrança da Minha Formatura ABC com foto e nome, lousa, livros, arco-íris e letrinhas ABC em tons pastel. Presente de formatura.", TF + ["lembranca"], IDEAL_A),
'c04': S(f"<p>A <strong>Caneca Formatura ABC com 2 Fotos e Nome</strong> tem duas molduras coloridas de borda ondulada: uma em pé, para a foto da criança, e outra deitada, para a foto da turma ou da família.</p>\n<p>As letrinhas ABC de carinha feliz, um arco-íris, livros, lápis e flores completam a arte, com o nome da criança numa faixa amarela.</p>\n<p>É um <strong>presente de formatura</strong> para guardar as duas lembranças do dia. {FOTO_NOTA}</p>",
         "Caneca Formatura ABC com 2 Fotos e Nome | Trio Ohana", "Caneca de formatura ABC com 2 fotos e nome: a da criança e a da turma ou da família, com letrinhas ABC e arco-íris. Presente de formatura.", TF + ["2 fotos", "foto da turma"], IDEAL_A),
})
for k, d in P.items():
    d['cats'] = B
