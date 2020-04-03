import matplotlib.pyplot as plt
# import time


def curvadodragao(x, y):
    novox = [x[-1]]
    novoy = [y[-1]]
    for item in range(1, len(x)):
        novox.append(novox[-1] - (y[-item] - y[-item - 1]))
        novoy.append(novoy[-1] + (x[-item] - x[-item - 1]))
    x = x + novox
    y = y + novoy
    return x, y


def fazfractal(vezes):
    x = [0, 1]
    y = [0, 0]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = curvadodragao(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


vezes = int(input("Digite a quantidade de vezes(recomendado <= 20): "))
# inicio = time.time()
x, y = fazfractal(vezes)

print("Montando o Gráfico")
plt.plot(x, y, color="black")
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()