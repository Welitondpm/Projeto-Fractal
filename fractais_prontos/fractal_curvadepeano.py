import matplotlib.pyplot as plt


def curvadehilbert(x, y, vez):
    tam = x[-1] - x[0]
    o = []
    X, Y = [], []
    x = diminui(x, vez)
    y = diminui(y, vez)
    adicao = tam / (2 ** (vez + 1) - 1)
    x2 = x[::]
    x3 = x[::]
    x4 = x[::]
    y2 = y[::]
    y3 = y[::]
    y4 = y[::]
    x3, y3 = giraantihorario(x3, y3)
    x4, y4 = girahorario(x4, y4)
    for item in x2:
        o.append(item + adicao + (x[-1] - x[0]))
    x2 = o[::]
    o = []
    for item in x4:
        o.append(item + adicao + (x[-1] - x[0]))
    x4 = o[::]
    o = []
    for item in y3:
        o.append(item + adicao)
    y3 = o[::]
    o = []
    for item in y4:
        o.append(item + adicao)
    y4 = o[::]
    o = []
    for item in [x3[::-1], x, x2, x4]:
        for subitem in item:
            X.append(subitem)
    for item in [y3[::-1], y, y2, y4]:
        for subitem in item:
            Y.append(subitem)
    return X, Y


def diminui(n, vez):
    l = []
    for item in n:
        l.append(item / (((2 ** (vez + 1)) - 1) / ((((2 ** (vez + 1)) - 1) - 1) / 2)))
    return l


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


vezes = int(input("Escolha quantas vezes: "))
escala = int(input("Escolha a Escala: "))
x = [0, 0, escala, escala]
y = [escala, 0, 0, escala]
vez = 0
while vez < vezes:
    vez += 1
    x, y = curvadehilbert(x, y, vez)


print("Montando o Gráfico")
plt.plot(x, y, "k")
plt.show()