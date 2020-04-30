import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


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


def VariaveisDeInput(Valores):
    if Valores:
        vezes = 9
    else:
        vezes = int(input("Quantidade de vezes ( <= 9): "))
    return vezes


def FazFractal(vezes):
    x, y = fazkochx(vezes)
    return x, y


def FazFractalComTempo(Valores):
    vezes = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    fim = time.time()
    print(str(round(fim-inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def SalvarEmPDF(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    plt.plot(x, y, color="black")
    with PdfPages(r'curvadekochX.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
        if ExecutarPropriedade:
            PropriedadeQuadrado(Valores)
        else:
            MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
            if MostrarDesempenho:
                FazFractalComTempo(Valores)
            else:
                FazFractalSemTempo(Valores)


if __name__ == "__main__":
    Begin()