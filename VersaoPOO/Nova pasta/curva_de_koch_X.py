import matplotlib.pyplot as plt
from propriedade_por_quadrados import *


def individualizasegmento(x, y):
    tamanho = len(x)
    novalistax, novalistay = [], []
    indice = 0
    for item in range(1, tamanho):
        novalistax.append([x[indice], x[item]])
        novalistay.append([y[indice], y[item]])
        indice += 1
    return novalistax, novalistay


def deliberador(x, y):
    x, y = individualizasegmento(x, y)
    novalistax, novalistay = [], []
    tamanho = len(x)
    for item in range(tamanho):
        a = x[item]
        b = y[item]
        if a[0] == a[1] and b[0] == b[1]:
            continue
        else:
            lista2, lista1 = fazcurvadekoch(x[item], y[item])
            for item in lista2:
                novalistax.append(item)
            for item in lista1:
                novalistay.append(item)
    return novalistax, novalistay


def fazcurvadekoch(x, y):
    horizontal = not x[0] == x[1] and y[0] == y[1]
    vertical = x[0] == x[1] and not y[0] == y[1]
    xinicial, xfinal = x[0], x[1]
    yinicial, yfinal = y[0], y[1]
    if horizontal:
        x1, y1 = (xfinal + (2 * xinicial)) / 3, yinicial
        x2, y2 = x1, yinicial + (x1 - xinicial)
        x3, y3 = (2 * xfinal + xinicial) / 3, y2
        x4, y4 = x3, y1
    if vertical:
        y1, x1 = (yfinal + 2 * yinicial) / 3, xinicial
        y2, x2 = y1, xinicial - (y1 - yinicial)
        y3, x3 = (2 * yfinal + yinicial) / 3, x2
        y4, x4 = y3, x1
    return([xinicial, x1, x2, x3, x4, xfinal], [yinicial, y1, y2, y3, y4, yfinal])


def fazkochx(vezes):
    x = [0, 0, 1, 1, 0]
    y = [1, 0, 0, 1, 1]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = deliberador(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def FazFractal(vezes):
    x, y = fazkochx(vezes)
    return x, y


def PropriedadeQuadrado(vezes):
    x, y = FazFractal(vezes)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def Begin(vezes = 9):
    x, y = FazFractal(vezes)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


if __name__ == "__main__":
    Begin(9)