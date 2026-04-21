def dobro(x):
    return x * 2
def quadrado(x):
    return x ** 2

funcs = [dobro, quadrado] * 5
for func, numero in zip(funcs, range(1, 11)):
    print(f'0 {func} de {numero} é {func(numero)}')
