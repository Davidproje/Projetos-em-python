import pandas as pd
tabela = pd.read_csv('C:/Users/david/Downloads/archive/athlete_events.csv')
tabela.head()
tabela.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'})
tabela.drop('ID', axis=1, inplace=True)

print(tabela)