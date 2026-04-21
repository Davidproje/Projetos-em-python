#clases
class InstitutoTecmat:
    def incrementa(self, v, i):
       self.valor = v
       self.incremento = i
       self.resultado = self.valor+self.incremento
       return self.resultado
a = InstitutoTecmat()
b = a.incrementa(10, 5)
print(a.valor)
#metodo
class InstitutoTecmat:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print('ultrapassou o valor')
        else:
            print('o valor e aceitavel')
    def exponencial (self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)
a = InstitutoTecmat()
a.incrementa()
print(a.valor)
a.verifica()
a.exponencial(3)
print(a.valor_exponencial)
