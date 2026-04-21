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
#herança
class Calculos(InstitutoTecmat):
    pass 
c = Calculos()
c.incrementa()
print(c.valor)
#herança2
class Calculos(InstitutoTecmat):
    def decrementar(self):
        self.valor = self.valor - self.incremento
c = Calculos()
c.incrementa()
print(c.valor)
c.decrementar()
print(c.valor)
#metodoconstrutor __init__

class Calculos(InstitutoTecmat):
    def __init__(self, d = 5):
        super().__init__(v=10, i=1)
        self.divisor = d
    def decrementar(self):
        self.valor = self.valor - self.incremento
    def divide(self):
        self.valor = self.valor/self.divisor
c = Calculos()
c.incrementa()
print("a soma dos valores e ",c.valor)
c = Calculos()
c.decrementar()
print("a divisão dos valores é",c.valor)
c = Calculos()
c.divide()
print("a divisão dos valores e igual a ",c.valor)

        