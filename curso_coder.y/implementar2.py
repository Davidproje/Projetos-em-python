
def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)
       

resultado = mapear(lambda x: x ** 2, [2, 3, 4])
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))