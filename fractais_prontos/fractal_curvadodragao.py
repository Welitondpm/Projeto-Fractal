import matplotlib.pyplot as plt


def curvadodragao(x, y):
    novox = [x[-1]]
    novoy = [y[-1]]
    for item in range(1, len(x)):
        novox.append(novox[-1] - (y[-item] - y[-item - 1]))
        novoy.append(novoy[-1] + (x[-item] - x[-item - 1]))
    x = x + novox
    y = y + novoy
    return x, y


vezes = int(input("Digite a quantidade de vezes(recomendado 20): "))
x = [0, 1]
y = [0, 0]
vez = 0
while vez < vezes:
    vez += 1
    x, y = curvadodragao(x, y)

print("Montando o Gráfico")
plt.plot(x, y, color="black")
plt.show()