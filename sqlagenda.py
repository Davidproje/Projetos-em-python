import sqlite3
import time
conectar = sqlite3.connect('C:/Users/david/OneDrive/Documentos/Py/agenda.db')
#funções
c = conectar.cursor()

def criar_db():
    c.execute("CREATE TABLE IF NOT EXISTS cadastro (Nome text, Telefone varchar, Email text, Data text)")
#criando o banco de dados
try:
    criar_db()
except:
    print("erro ao criar banco de dados.")
else:
    print("banco de dados criado com sucesso")

#função inserir
def inserir(n, t, e):
    d = time.strftime("%d/%m/%y")
    c.execute("INSERT INTO cadastro VALUES(?, ?, ?, ?)",(n, t, e, d))
    conectar.commit()

def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql,(p,)):
        print(row)

#variavel numerica:
fc = int(input("1- cadastrar \n 2- pesquisar \n selecione uma opção: "))

if fc == 1:
    
    try:
        print("cadastro de agenda. ")
        time.sleep(1)
        n = str(input("Informe seu nome: "))
        t = str(input("informe seu numero: "))
        e = str(input("informe seu email: "))
        inserir(n, t, e)

    except:
        print("erro ao efetuar o cadastro.")
    else:
        print("cadastro realizado.")
elif fc == 2:
    print("aguarde um momento. ")
    time.sleep(1)
    p = str(input("informe o nome a ser pesquisado: "))
    pesquisar(p)
    print(input("Aperte a tecla ENTER para finalizar. "))
else:
    print("opção invalida")

