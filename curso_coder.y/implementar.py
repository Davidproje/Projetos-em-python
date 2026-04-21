import time
def mapear(funcao, lista):
    for elemento in lista:
        print('passando por aqui.')
        time.sleep(1)
        print('passando por aqui..')
        time.sleep(1)
        print('passando por aqui...')
        time.sleep(1)
        yield funcao(elemento)

print(list(mapear(lambda x: x **2, [2, 3, 4])))
print('fim')