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

 
def fazdragao(vezes, escalonar):
    x = [0, 1]
    y = [0, 0]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = curvadodragao(x, y)
        if escalonar and vez > 2:
            x, y = arruma_escala(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def arruma_escala(x, y):
    novox, novoy = [], []
    indice = 0
    limite = len(x)
    while indice < limite:
        novox.append(x[indice] / (2 ** 0.5))
        novoy.append(y[indice] / (2 ** 0.5))
        indice += 1
    return novox, novoy


if __name__ == "__main__":
    x, y = fazdragao(20, False)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()