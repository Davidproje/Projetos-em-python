
while True:
    nota = input("Digite uma nota: ")

    if nota.strip() == "":
        print('\033[31m', "Nenhuma nota foi inserida. \n Por favor, Insira uma nota.", '\033[0;0m')
        continue

    nota = float(nota)

    if nota == 10:
        print("Parabens,Você tirou nota maxima. ")
    elif 9 <= nota < 9.9:
        print("A nota foi excellent.")
    elif 8 <= nota < 8.9:
        print("A sua nota foi boa.")
    elif 7 <= nota < 7.9:
        print("A nota foi razoável.")
    elif 6 <= nota < 6.9:
        print("A nota pode melhorar.")
    elif 5 <= nota < 5.9:
        print("A nota precisará de recuperação.")
    elif 4 <= nota < 4.9:
        print("A nota Precisará de recuperação + trabalho.")
    elif 3 <= nota < 3.9:
        print("A nota esta reprovada.")
    elif 2 <= nota < 2.9:
        print("A {} nota sera reprovada.".format(nota))
    elif 1 > nota or nota > 10:
        print("{}  nota invalida".format(nota))
    else:
        print("Sua nota foi muito baixa para ter solução")
    break
