import pandas as pd
tabela = pd.read_csv('C:/Users/david/Downloads/archive/athlete_events.csv')
tabela.head()
tabela.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'})
print(tabela)