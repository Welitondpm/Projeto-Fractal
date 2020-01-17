import matplotlib.pyplot as plt
from random import randint


vezes = int(input("Digite a Quantidade de vezes: "))
valor = float(input("Valor(triangulodesier... 2): "))
contador = 0
x1 = [0, 50, -50]
y1 = [7500 ** 0.5, 0, 0]
x = [0]
y = [(7500 ** 0.5) / 2]
while contador <= vezes:
    contador += 1
    a = randint(0, 2)
    x.append((x1[a] + x[-1]) / valor)
    y.append((y1[a] + y[-1]) / valor)

print("Montando o gráfico")
plt.scatter(x, y, color = "black")
plt.show()