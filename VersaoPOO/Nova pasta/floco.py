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
        a, b = x[item], y[item]
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
    _60 = y[1] > y[0] and x[0] < x[1] or y[1] < y[0] and x[0] > x[1]
    _120 = y[1] < y[0] and x[0] < x[1] or y[1] > y[0] and x[0] > x[1]
    xinicial, xfinal = x[0], x[1]
    yinicial, yfinal = y[0], y[1]
    if horizontal:
        x1, y1 = (xfinal + (2 * xinicial)) / 3, yinicial
        x2, y2 = (xfinal - xinicial) / 2 + xinicial, yinicial + (0.75 ** 0.5) * (xfinal - xinicial) / 3
        x3, y3 = (2 * xfinal + xinicial) / 3, y1
    elif _60:
        x1, y1 = xinicial + (xfinal - xinicial) / 3, yinicial + (yfinal - yinicial) / 3
        x2, y2 = xinicial, yinicial + (yfinal - yinicial) * 2 / 3
        x3, y3 = xinicial + (xfinal - xinicial) * 2 / 3, y2
    elif _120:
        x1, y1 = xinicial + (xfinal - xinicial) / 3, yinicial + (yfinal - yinicial) / 3
        x2, y2 = xfinal, y1
        x3, y3 = xinicial + 2 * (xfinal - xinicial) / 3, yinicial + 2 * (yfinal - yinicial) / 3
    else:
        return x, y
    return([xinicial, x1, x2, x3, xfinal], [yinicial, y1, y2, y3, yfinal])


def fazfloco(vezes):
    x = [0, 3, 6, 0]
    y = [0, 27 ** 0.5, 0, 0]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = deliberador(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def FazFractal(vezes):
    x, y = fazfloco(vezes)
    return x, y


def PropriedadeQuadrado(vezes):
    x, y = FazFractal(vezes)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.fill(x, y, color="black")
    plt.show()


def Begin(vezes = 10):
    ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
    if ExecutarPropriedade:
        PropriedadeQuadrado(vezes)
    else:
        x, y = FazFractal(vezes)
        print("Montando o Gráfico")
        plt.fill(x, y, color="black")
        plt.show()


if __name__ == "__main__":
    Begin(10)