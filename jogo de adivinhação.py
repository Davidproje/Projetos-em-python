#Aqui foi utilizado a biblioteca random para sortear um numero de 0 a 5
#Se o número escolhido for igual ao da máquina, voce ganha.


import random
numero = int(input('Escolha um numero inteiro no intervalo de 0 a 5. '))
escolha = random.randint(0, 5)

if numero == escolha:
    print('você ganhou!!!.')
else:
    print('Você perdeu!!!')
    print('fim de jogo!! \n o numero escolhido foi {}'.format(escolha))
