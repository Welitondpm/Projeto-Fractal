import matplotlib.pyplot as plt


def organizaprafazer(x, y, z):
    nx, ny = [], []
    for item in range(len(x)):
        x1, x2, y1, y2 = triangulodesierpinski(x[item], y[item], z)
        nx.extend((x1, x2))
        ny.extend((y1, y2))
    return nx, ny


def triangulodesierpinski(x, y, z):
    x1 = x[0]
    x2 = x1 + ((x[1] - x[0]) / 3)
    x3 = x[1]
    x4 = x[1] - ((x[1] - x[0]) / 3)
    t1x = [x1, x2]
    t2x = [x3, x4]
    return t1x, t2x, [z, z], [z, z]


def fazcadatriangulo(x, y):
    novox, novoy = [], []
    for item in x:
        novox.append([item[0], item[1]])
    for item in y:
        novoy.append([item[0], item[1]])
    return novox, novoy


def montagrafico(novox, novoy):
    for item in range(len(novox)):
        plt.fill(novox[item], novoy[item], color="black", linewidth=1)


def fazsierpinski(vezes, t):
    vez = 0
    x = [[0, t]]
    y = [[0, 0]]
    while vez < vezes:
        vez += 1
        montagrafico(x, y)
        x, y = organizaprafazer(x, y, vez)
        print("%d de %d" % (vez, vezes))
    montagrafico(x, y)
    return x, y



def FazFractal(vezes, tamanho):
    x, y = fazsierpinski(vezes, tamanho)
    fazcadatriangulo(x, y)
    print("Montando o Gráfico")


def criaunicalista(x):
    novox = []
    for i in x:
        novox.extend(i)
    return novox


def Begin():
    vezes = 15
    tamanho = 50
    FazFractal(vezes, tamanho)
    plt.show()


if __name__ == "__main__":
    Begin()