import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_csv('C:/Users/david/Downloads/archive/athlete_events.csv')
print('visualização de dados')
tabela.head()
tabela.hist(column='Height', bins = 10)
plt.show()
print(tabela)