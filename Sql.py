import sqlite3
banco = sqlite3.connect('C:/Users/david/OneDrive/Documentos/Py/primeiro_banco_de_dados.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ALUNOS(NOME TEXT, IDADE INTEGER, EMAIL TEXT)")
cursor.execute("INSERT INTO ALUNOS VALUES('Luana', '16', 'anagmail.com')")
banco.commit()
cursor.execute("SELECT*FROM alunos")
print(cursor.fetchall())