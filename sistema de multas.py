#Calculo de valor a pagar em uma multa, levando em consideração 80 km o permitido.

velocidade=int(input('Digite a velocidade do veiculo. '))
#km=str('velocidade'+'km/h')
if velocidade >= 80:
    print('você foi multado em {} Reais'.format((velocidade-80)*7))
else:
    print('você esta dentro do limite de velocidade da rodovia')

print('Tenha um bom dia')


