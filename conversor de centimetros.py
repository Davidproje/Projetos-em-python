#Este converte um numero em metros,centímetros e milímetros.

n1 = float(input('Digite o valor que gostaria de conveter: '))
#variaveis
cm = n1*100

mm = n1*1000
print('O valor {} em Metros \n é equivalente a {:.2f} centimetros \n {:.2f} milimetros'.format(n1,cm,mm))