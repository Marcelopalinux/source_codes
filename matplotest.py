import matplotlib.pyplot as plt


y = [1,3,5,7,9,10]
x = [1,3,5,7,9,11]

y1 = [2,4,6,8,10,11]
x1 = [0,2,4,6,8,10]


titulo = "Meu Grafico em Python Barras Comparação"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x,y,label="Grupo 1")
plt.bar(x1,y1,label="Grupo 2")
plt.legend()
plt.show()