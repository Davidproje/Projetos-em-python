from funcao_primeira import dobro, quadrado


def processar(titulo, lista, funcao):
    print('Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

    processar('dobro de 1 a 10', range(1, 11), dobro)
    processar('quadrado de 1 a 10', range(1, 11), quadrado)
