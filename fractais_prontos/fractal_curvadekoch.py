import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# import time


def individualizasegmento(calc):
    tamanho = len(calc)
    novalista = []
    x = 0
    for item in range(1, tamanho):
        novalista.append([calc[x], calc[item]])
        x += 1
    return novalista


def deliberador(x, y):
    x = individualizasegmento(x)
    y = individualizasegmento(y)
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
    _60 = y[1] > y[0] and x[0] < x[1] or (y[1] < y[0] and x[0] > x[1])
    _120 = y[1] < y[0] and x[0] < x[1] or (y[1] > y[0] and x[0] > x[1])
    xinicial, xfinal = x[0], x[1]
    yinicial, yfinal = y[0], y[1]
    if horizontal:
        x1, y1 = (xfinal + (2 * xinicial)) / 3, yinicial
        x2, y2 = (xfinal - xinicial) / 2 + xinicial, yinicial + (0.75 ** 0.5) * (xfinal-xinicial) / 3
        x3, y3 = (2 * xfinal + xinicial) / 3, y1
    elif _60:
        x1, y1 = xinicial + (xfinal - xinicial) / 3, yinicial + (yfinal-yinicial) / 3
        x2, y2 = xinicial, yinicial + (yfinal - yinicial) * 2 / 3
        x3, y3 = xinicial + (xfinal - xinicial) * 2 / 3, y2
    elif _120:
        x1, y1 = xinicial + (xfinal - xinicial) / 3, yinicial + (yfinal - yinicial) / 3
        x2, y2 = xfinal, y1
        x3, y3 = xinicial + 2 * (xfinal - xinicial) / 3, yinicial + 2 * (yfinal - yinicial) / 3
    else:
        return x, y
    return([xinicial, x1, x2, x3, xfinal], [yinicial, y1, y2, y3, yfinal])


def fazfractal(vezes):
    x = [0, 3]
    y = [0, 0]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = deliberador(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


vezes = int(input("Quantidade de vezes ( <= 10): "))
# inicio = time.time()
x, y = fazfractal(vezes)


print("Montando o Gráfico")
# plt.scatter(x, y, color="black")
with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\curvadekoch(vezes12).pdf') as export_pdf:
    plt.plot(x, y, color="black")
    export_pdf.savefig()
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()
