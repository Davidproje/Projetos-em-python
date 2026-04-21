import pandas as pd


tabela = pd.read_csv('C:/Users/david/Downloads/archive/athlete_events.csv')
tabela.head(4)
tabela.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'})
print(tabela)

tabela2 = tabela.dropna()
tabela2.shape
print(tabela2)

dadosnulo = tabela.isnull()
dadosnulo.head(10)
print(dadosnulo)

NuN = tabela.isnull().sum()
print(NuN)

tabela['Medal'] = tabela[ 'Medal'].fillna('Zero')
tabela['Height'] = tabela['Height'].fillna(tabela['Height'].mean())
tabela.head(10)
print(tabela)