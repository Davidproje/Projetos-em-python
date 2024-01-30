from math import sin, cos, tan, radians

#tabela trigronometrica
n1=float(input('digite o angulo que deseja calcular: '))
angulo=radians(n1)
  #valor de entrada para radiano.

s= sin(angulo)
c= cos(angulo)
t= tan(angulo)

print('o resultado de seno é {:.2f}'.format(s))
print('o resultado de coseno é {:.2f}'.format(c))
print('o resultado da tangente é {:.2f}'.format(t))