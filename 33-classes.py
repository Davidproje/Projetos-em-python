#clases

class InstitutoTecmat:
    def incrementa(self, v, i):
        valor = v
        incremento = i 
        resultado = valor+incremento
        return resultado
a = InstitutoTecmat()
b = a.incrementa(10, 5)
print('o resultado da soma e',b)