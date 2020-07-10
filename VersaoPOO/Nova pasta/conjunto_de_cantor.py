import matplotlib.pyplot as plt


def organizaprafazer(x, valordoy):
    novox, novoy = [], []
    for item in range(len(x)):
        x1, x2, y1, y2 = linhacantor(x[item], valordoy)
        novox.extend((x1, x2))
        novoy.extend((y1, y2))
    return novox, novoy


def linhacantor(x, valordoy):
    x1 = x[0]
    x2 = x1 + ((x[1] - x[0]) / 3)
    x3 = x[1]
    x4 = x3 - ((x[1] - x[0]) / 3)
    linha1 = [x1, x2]
    linha2 = [x3, x4]
    return linha1, linha2, [valordoy, valordoy], [valordoy, valordoy]


def fazcadalinha(x, y):
    novox, novoy = [], []
    indice = 0
    tamanho = len(x)
    while indice < tamanho:
        novox.append([x[indice][0], x[indice][1]])
        novoy.append([y[indice][0], y[indice][1]])
        indice += 1
    return novox, novoy


def montagrafico(novox, novoy):
    for item in range(len(novox)):
        plt.plot(novox[item], novoy[item], color="black", linewidth=1)


def fazcantor(vezes, t):
    vez = 0
    x = [[0, t]]
    y = [[0, 0]]
    while vez < vezes:
        vez += 1
        montagrafico(x, y)
        x, y = organizaprafazer(x, vez)
        print("%d de %d" % (vez, vezes))
    montagrafico(x, y)
    return x, y


def Begin(vezes = 10, tamanho = 50):
    x, y = fazcantor(vezes, tamanho)
    fazcadalinha(x, y)
    print("Montando o Gráfico")
    plt.show()


if __name__ == "__main__":
    Begin(10, 50)