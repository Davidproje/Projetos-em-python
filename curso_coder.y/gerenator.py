def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'



generator = cores_arco_iris()
print(type(generator))
while True:
   print(next(generator))
   
