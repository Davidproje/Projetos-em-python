#verificação de numeros pares e impares

numero=int(input('Digite o numero que gostaria de verificar. '))
r= numero % 2
#print('o resultado desse numero foi {}'.format(r))
if r == 0:
    print('Esse número e par.')
else:
    print('Esse número e inpar.')
print(' O numero digitado foi {} '.format(numero))