import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def curvadehilbert(x, y, vez):
    tamanho = x[-1] - x[0]
    listadescartavel = []
    X, Y = [], []
    x = diminui(x, vez)
    y = diminui(y, vez)
    adicao = tamanho / (2 ** (vez + 1) - 1)
    x2 = x[::]
    x3 = x[::]
    x4 = x[::]
    y2 = y[::]
    y3 = y[::]
    y4 = y[::]
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
        for subitem in item:
            X.append(subitem)
    for item in [y3[::-1], y, y2, y4]:
        for subitem in item:
            Y.append(subitem)
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


def VariaveisDeInput(Valores):
    if Valores:
        vezes, escala = 5, 10
    else:
        vezes = int(input("Escolha quantas vezes ( <= 5): "))
        escala = int(input("Escolha a Escala (recomendado 1): "))
    return vezes, escala


def FazFractal(vezes, escala):
    x, y = fazhilbert(vezes, escala)
    return x, y


def FazFractalComTempo(Valores):
    vezes, escala = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes, escala)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, escala = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escala)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes, escala = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escala)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, escala = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escala)
    plt.plot(x, y, color="black")
    with PdfPages(r'curvadehilbert.pdf') as export_pdf:
        export_pdf.savefig()


def MostrarTempo(Valores):
    MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
    if MostrarDesempenho:
        FazFractalComTempo(Valores)
    else:
        FazFractalSemTempo(Valores)


def MostrarPropriedade(Valores):
    ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
    if ExecutarPropriedade:
        PropriedadeQuadrado(Valores)
    else:
        MostrarTempo(Valores)


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        MostrarPropriedade(Valores)


if __name__ == "__main__":
    Begin()