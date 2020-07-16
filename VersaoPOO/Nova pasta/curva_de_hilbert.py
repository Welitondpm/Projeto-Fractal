import matplotlib.pyplot as plt


def curvadehilbert(x, y, vez):
    tamanho = x[-1] - x[0]
    listadescartavel = []
    X, Y = [], []
    x = diminui(x, vez)
    y = diminui(y, vez)
    adicao = tamanho / (2 ** (vez + 1) - 1)
    x2, x3, x4 = x[::], x[::], x[::]
    y2, y3, y4 = y[::], y[::], y[::]
    x3, y3 = giraantihorario(x3, y3)
    x4, y4 = girahorario(x4, y4)
    for item in x2:
        listadescartavel.append(item + adicao + (x[-1] - x[0]))
    x2 = listadescartavel[::]
    listadescartavel = []
    for item in x4:
        listadescartavel.append(item + adicao + (x[-1] - x[0]))
    x4 = listadescartavel[::]
    listadescartavel = []
    for item in y3:
        listadescartavel.append(item + adicao)
    y3 = listadescartavel[::]
    listadescartavel = []
    for item in y4:
        listadescartavel.append(item + adicao)
    y4 = listadescartavel[::]
    listadescartavel = []
    for item in [x3[::-1], x, x2, x4]:
        X.extend(item)
    for item in [y3[::-1], y, y2, y4]:
        Y.extend(item)
    return X, Y


def diminui(n, vez):
    lista = []
    for item in n:
        lista.append(item / ((2 ** (vez + 1) - 1) / ((2 ** (vez + 1) - 2) / 2)))
    return lista


def giraantihorario(x, y):
    novox = [x[0]]
    novoy = [y[0]]
    for item in range(1, len(x)):
        novox.append(novox[-1] + y[-item] - y[-item - 1])
        novoy.append(novoy[-1] + x[-item] - x[-item - 1])
    return novox, novoy


def girahorario(x, y):
    novox = [x[-1]]
    novoy = [y[-1]]
    for item in range(1, len(x)):
        novox.append(novox[-1] + y[-item - 1] - y[-item])
        novoy.append(novoy[-1] - x[-item - 1] + x[-item])
    return novox, novoy


def fazhilbert(vezes, escala):
    x = [0, 0, escala, escala]
    y = [escala, 0, 0, escala]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = curvadehilbert(x, y, vez)
        print("%d de %d" % (vez, vezes))
    return x, y


if __name__ == "__main__":
    x, y = fazhilbert(5, 1)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()