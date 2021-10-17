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
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
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
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    # lista_de_sentencas = separa_sentencas(texto)
    # lista_de_frases = separa_frases(sentenca) # Para cada sentença devolvida pela função anterior, essa gera uma nova lista, dessa vez de frases.
    #lista_de_palavras = separa_palavras(frase) # Para cada frase devolvida pela função anterior, essa gera uma nova lista, dessa vez de palavras.
    
    # Concatenar uma única lista de palavras e repassar às duas próximas funções:
        # n_palavras_unicas(lista_de_palavras)
        # n_palavras_diferentes(lista_de_palavras)


       # separa_sentencas(texto)
            # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    
        # separa_frases(sentenca)
            # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca

        # separa_palavras(frase)
            # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase

        # n_palavras_unicas(lista_palavras)
            # Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez

        # n_palavras_diferentes(lista_palavras)
            # Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas

    # Cálculos:

        # 0. Número total de palavras:
            # variável contendo len(lista_de_palavras)

        # lista_de_palavras = 

        # 1. Tamanho médio de palavra: Média simples do número de caracteres por palavra
                    # para cada palavra in lista .... len(palavra)
                         # somatória de todos os len(palavra)
                    # Cálculo da média de caracteres por palavra: Soma total de caracteres / número total de palavras.

        
        # 2. Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
                    # n_palavras_diferentes(lista_concatenada_de_palavras) / número total de palavras


        # 3. Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras
                    # n_palavras_diferentes(lista_concatenada_de_palavras) / número total de palavras


        # 4. Tamanho médio de sentença: Média simples do número de caracteres por sentença.
                 # Soma de todos os caracteres de todas as sentenças / No de sentenças  (len(lista_de_sentencas))
            # (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença)


        # 5. Complexidade de sentença: Média simples do número de frases por sentença (Número total de frases divido pelo número de sentenças)
                # len(lista_de_frases) / len(lista_de_sentenças)
        


        # 6. Tamanho médio de frase: Média simples do número de caracteres por frase (Soma do número de caracteres em cada frase dividida pelo número de frases no texto)
            # (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
                # Soma do No total de caracteres / len(lista_de_frases)


        # Emitir lista simples com cada um dos cálculos em ordem.




     


    

    
    
    
    
    
    
    pass