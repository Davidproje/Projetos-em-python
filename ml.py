import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

x = np.array([6, 8, 10, 14, 18])
y = np.array([7, 9, 13, 17.5, 18])

#visualizar os dados e graficos
plt.scatter(x, y)#cria o grafico
plt.xlabel ("diametro em polegadas")#adicionar o rotulo do eixo x
plt.ylabel ("preço em reais")#adiciona o rotulo do eixo y
plt.title ("preço de pizza em razão de seu diametro")#adiciona o titulo do grafico
plt.show()#mostrar o grafico

#criar e treinar um modelo
model = LinearRegression() #instanciar o modelo
x = x.reshape(-1, 1)#transforma o array x em uma matriz de coluna
model.fit(x, y)

#avaliar o desempenho do modelo
y_pred = model.predict(x) #fazer previsoes
mse = mean_squared_error(y, y_pred)#calcular o erro quadratico medio
r2 = r2_score(y, y_pred)#calcular o coeficiente
print("MSE ="f'{mse:.2f}\n R2 = {r2:.2f}')

#fazer previsao para nova pizza
x_new = np.array([12])#diametro da nova pizza em polegadas
y_new = model.predict(x_new.reshape(-1, 1))
print(f"O valor da pizza será ${y_new[0]:.2f} para diâmetro de {x_new[0]} polegadas")