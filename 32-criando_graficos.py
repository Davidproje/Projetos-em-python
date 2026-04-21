#bibliotecas
import matplotlib.pyplot as plt
import numpy as np


#funções
x = np.arange(-1000, 1000, 1)
y = x**2
plt.plot(x, y)
plt.show()

figura = plt.figure(figsize=(10, 10))
#primeiro grafico
y1 = x**2
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("y = x^2")

#segundo grafico
y2 = x**3
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("y = x^3")

#terceiro grafico
y3 = x**4
plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("y = x^4")

#imagem
from skimage.io import imread
imagem = imread("C:/Users/david/OneDrive/Imagens/shiny-black-windows-10-hd-lp0puofy8ei4adib.jpg")
plt.imshow(imagem)
plt.axis("off")
plt.title("imagem")

# tudo junto

plt.tight_layout()
plt.show()


#pasta de imagens

endereço = 'C:/Users/david/Downloads/Nova/'
imagens = []
for i in range(6):
    imagem = imread(endereço+"download"+str(i+1)+".jpg")
    imagens.append(imagem)   
figura = plt.figure(figsize=(5, 8 ))
for i in range(6):
    figura.add_subplot(3, 2, i+1)
    plt.imshow(imagens[i])
plt.show()