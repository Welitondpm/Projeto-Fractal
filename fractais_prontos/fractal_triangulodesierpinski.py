import matplotlib.pyplot as plt


def organizaprafazer(x, y):
    for item in range(len(x)):
        x1, x2, x3, y1, y2, y3 = triangulodesierpinski(x[item], y[item])
        x.extend((x1, x2, x3))
        y.extend((y1, y2, y3))
    return x, y


def triangulodesierpinski(x, y):
    x1 = x[0]
    x2 = (x[0] + x[1]) / 2
    x3 = x[1]
    x4 = (x[1] + x[2]) / 2
    x5 = x[2]
    x6 = (x[2] + x[0]) / 2
    y1 = y[0]
    y2 = (y[0] + y[1]) / 2
    y3 = y[1]
    y4 = (y[1] + y[2]) / 2
    y5 = y[2]
    y6 = (y[2] + y[0]) / 2
    t1x = [x1, x6, x2]
    t1y = [y1, y6, y2]
    t2x = [x2, x3, x4]
    t2y = [y2, y3, y4]
    t3x = [x6, x4, x5]
    t3y = [y6, y4, y5]
    return t1x, t2x, t3x, t1y, t2y, t3y


def fazcadatriangulo(x, y):
    novox, novoy = [], []
    for item in x:
        novox.append([item[0], item[1], item[2], item[0]])
    for item in y:
        novoy.append([item[0], item[1], item[2], item[0]])
    return novox, novoy


def montagrafico(novox, novoy):
    for item in range(len(x)):
        plt.plot(novox[item], novoy[item], color="black", linewidth=1)


def fazfractal(vezes, t):
    vez = 0
    x = [[-t / 2, 0, t / 2]]
    y = [[-t * 3 ** 0.5 / 2, 0, -t * 3 ** 0.5 / 2]]
    while vez < vezes:
        vez += 1
        x, y = organizaprafazer(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


vezes = int(input("Digite quantas vezes (recomendado 6): "))
t = int(input("Digite o tamanho do lado do triângulo (recomendado 50): "))

x, y = fazfractal(vezes, t)
novox, novoy = fazcadatriangulo(x, y)

print("Montando o Gráfico")
montagrafico(novox, novoy)
plt.show()