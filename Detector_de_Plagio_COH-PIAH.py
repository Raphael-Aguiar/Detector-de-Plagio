# Código-Esqueleto fornecido junto com o exercício

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    frase = str(frase)
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        palavra = str(palavra)
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        palavra = str(palavra)
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_da_sentença(sentenca):
    media_caracteres_por_sentença = 0
    palavra1 = []
    frases_temp = separa_frases(sentenca)
    for frase in frases_temp:
            palavra1.extend(separa_palavras(frase))
            for palavra in palavra1:
                media_caracteres_por_sentença = media_caracteres_por_sentença + len(palavra)
            palavra1 = []
    return media_caracteres_por_sentença

def tamanho_medio_da_frase(frase):
    media_caracteres_por_frase = 0
    palavras_temp = separa_palavras(frase)
    for palavra in palavras_temp:
        media_caracteres_por_frase = media_caracteres_por_frase + len(palavra)
    return media_caracteres_por_frase

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    #Declaração de variáveis:
    lista_de_frases = []
    lista_de_palavras = []
    total_caracteres = 0
    media_caracteres_por_sentença = 0
    tamanho_medio_sentenca = 0
    tms = 0
    tmf = 0
    # Separação das sentenças do texto:
    lista_de_sentencas = separa_sentencas(texto)
    # Loopings para popular listas de frases e de palavras:
    for sentenca in lista_de_sentencas:
        lista_de_frases.extend(separa_frases(sentenca))
    for frase in lista_de_frases:
        lista_de_palavras.extend(separa_palavras(frase))
    # Contagem dos caracteres totais sem espaço:
    for palavra in lista_de_palavras:
        total_caracteres = total_caracteres + len(palavra)
    # Cálculos:
    ## 0. Número total de palavras:
    total_palavras = len(lista_de_palavras)
    ## 1. Tamanho médio de palavra: soma dos tamanhos das palavras dividida pelo número total de palavras (Média simples do número de caracteres por palavra).
    tamanho_medio_palavras = total_caracteres / total_palavras
    ## 2. Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    type_token = n_palavras_diferentes(lista_de_palavras) / total_palavras
    ## 3. Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras
    hapax_legomana = n_palavras_unicas(lista_de_palavras) / total_palavras
    ## 4. Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    for sentenca in lista_de_sentencas:
        tms = tms + tamanho_medio_da_sentença(sentenca)
    tamanho_medio_sentenca = tms / len(lista_de_sentencas)
        # tamanho_medio_sentenca = total_caracteres / len(lista_de_sentencas)
                # Soma de todos os caracteres de todas as sentenças / No de sentenças
                # (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença)
    ## 5. Complexidade de sentença: Média simples do número de frases por sentença (Número total de frases divido pelo número de sentenças)
    complexidade_de_sentença = len(lista_de_frases) / len(lista_de_sentencas)
    ## 6. Tamanho médio de frase: Média simples do número de caracteres por frase (Soma do número de caracteres em cada frase dividida pelo número de frases no texto)
    for frase in lista_de_frases:
        tmf = tmf + tamanho_medio_da_frase(frase)
    tamanho_medio_frase = tmf / len(lista_de_frases)
            # (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
                # Soma do No total de caracteres / len(lista_de_frases)
    # Retorno do resultado final
    assinatura = [tamanho_medio_palavras, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_de_sentença, tamanho_medio_frase]
    return assinatura

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
print(calcula_assinatura(texto))


# [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]