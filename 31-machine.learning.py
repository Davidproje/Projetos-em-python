import pandas as pd
import sklearn
arquivo = pd.read_csv('C:/Users/david/Downloads/wine_dataset.csv')
print(arquivo)

#substituição de dados

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)
print(arquivo)

#variaveis

y = arquivo['style']
x = arquivo.drop('style', axis = 1)
print(y)

#criando treino e teste

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)
x_teste.shape
y_teste.shape
print(x_teste)
print(y_teste)
from sklearn.ensemble import ExtraTreesClassifier
#criando modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)
#imprimindo resultado
resultado = modelo.score(x_teste, y_teste)
print('Probabilidade',resultado)