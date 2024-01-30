#Aqui sera calculado o valor que restará de um salario apos as despesas.

#variaveis :
#salario
#despesas
#resultado


salario = float(input("Digite o Salario que gostaria de calcular. "))
despesas = float(input("Digite o total das despesas a calcular. "))
resultado = salario-despesas


print('O valor restante e: {:.2f} Reais'.format(resultado))


