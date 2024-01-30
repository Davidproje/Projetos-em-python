#Insira 3 números, que serão classificados como maior ou menor.
a = int(input('Digite o primeiro numero '))
b = int(input('Digite o segundo numero '))
c = int(input('Digite o terceiro numero '))
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor Digitado foi {} '.format(menor))

maior = a

if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c

print('O maior valor digita foi {} '.format(maior))