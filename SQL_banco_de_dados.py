#bibliotecas
import tkinter as tk
import sqlite3
import pandas as pd

#criar banco de dados e tabela
conexão = sqlite3.connect('C:/Users/david/OneDrive/Documentos/Py/BD/banco_de_dados.db')
c = conexão.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS clientes(NOME TEXT, SOBRENOME TEXT, EMAIL TEXT, TELEFONE TEXT)''')
conexão.commit()
conexão.close()

#criar cadastros
def cadastrar_cliente():
    conexão = sqlite3.connect('C:/Users/david/OneDrive/Documentos/Py/BD/banco_de_dados.db')
    c = conexão.cursor()
    c.execute("INSERT INTO clientes VALUES(:nome, :sobrenome, :email, :telefone)", 
              {
                  'nome':entry_nome.get(),
                  'sobrenome':entry_sobrenome.get(),
                  'email':entry_email.get(),
                  'telefone':entry_telefone.get()
              })
#deletar os campos apos dados inseridos
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')

    conexão.commit()
    conexão.close()

#expotar clientes para excel
def exporta_clientes():
    conexão = sqlite3.connect('C:/Users/david/OneDrive/Documentos/Py/BD/banco_de_dados.db')
    c = conexão.cursor()
    c.execute("SELECT *, oid FROM clientes")

    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')

    print(clientes_cadastrados)

    conexão.commit()
    conexão.close()

#criar titulo da janela
janela = tk.Tk()
janela.title('ferramenta de cadastro de cliente')
#criar as etiquetas = label
label_nome = tk.Label(janela, text = 'nome', width=30)
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text = 'sobrenome', width=30)
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text = 'email', width=30)
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text = 'telefone', width=30)
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#criar campos para inserir texto
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

#criar botoes
botao_cadastrar = tk.Button(janela, text = 'Cadastrar Cliente', command= cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text = 'exportar base de Cliente', command= exporta_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

janela.mainloop()
