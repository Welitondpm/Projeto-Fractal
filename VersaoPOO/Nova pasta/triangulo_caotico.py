import matplotlib.pyplot as plt
from random import randint


def fazcaotico(vezes, valor):
    contador = 0
    x1 = [0, 50, -50]
    y1 = [7500 ** 0.5, 0, 0]
    x = [sum(x1) / len(x1)]
    y = [sum(y1) / len(y1)]
    while contador <= vezes:
        # print("%d de %d" % (contador, vezes))
        contador += 1
        indice = randint(0, len(x1) - 1)
        x.append((x1[indice] + x[-1]) / valor)
        y.append((y1[indice] + y[-1]) / valor)
    return x, y


if __name__ == "__main__":
    x, y = fazcaotico(1000000, 2)
    print("Montando o gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    plt.show()