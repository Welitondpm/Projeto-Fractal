import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def fazcalculo(x, y, lados):
    somadosanguloint = 180 * (lados - 2)
    angulo = somadosanguloint / lados * math.pi / 180
    angulobackup = angulo
    novoxfinal, novoyfinal = [], []
    for indice in range(len(x) - 1):
        differencex = x[indice + 1] - x[indice]
        differencey = y[indice + 1] - y[indice]
        distanciaxy = (differencex ** 2 + differencey ** 2) ** 0.5
        if differencex < 0:
            distanciaxy *= -1
        if differencex != 0:
            angulodado = math.atan(differencey / differencex)
        elif differencey > 0:
            angulodado = math.pi / 2
        elif differencey < 0:
            angulodado = 3 * math.pi / 2
        else:
            continue
        novox = [x[indice] + differencex / 3]
        novoy = [y[indice] + differencey / 3]
        contadorwhile = 0
        while contadorwhile < lados - 2:
            novox += [novox[-1] + (distanciaxy / 3) * math.cos(angulodado + angulo)]
            novoy += [novoy[-1] + (distanciaxy / 3) * math.sin(angulodado + angulo)]
            angulo -= (math.pi - angulobackup)
            contadorwhile += 1
        angulo = angulobackup
        novox += [x[indice] + 2 * differencex / 3]
        novoy += [y[indice] + 2 * differencey / 3]
        novox = [x[indice]] + novox + [x[indice + 1]]
        novoy = [y[indice]] + novoy + [y[indice + 1]]
        novoxfinal += novox
        novoyfinal += novoy
    return novoxfinal, novoyfinal


def monta(x, y, vezes, lados):
    for vez in range(1, vezes + 1):
        print(vez, " de ", vezes)
        x, y = fazcalculo(x, y, lados)
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, lados, escala = 5, 7, 10
    else:
        vezes = int(input("Vezes: "))
        lados = int(input("lados: "))
        escala = int(input("Escala: "))
    return vezes, lados, escala


def FazFractal(vezes, lados, escala):
    for fractallados in range(3, lados + 1):
        x = [escala * fractallados, escala * (fractallados + 1)]
        y = [0, 0]
        fractallados = lados + 3 - fractallados
        print("\n", fractallados, ' lados de ', lados)
        x, y = monta(x, y, vezes, fractallados)
        plt.plot(x, y)


def FazFractalComTempo(Valores):
    vezes, lados, escala = VariaveisDeInput(Valores)
    inicio = time.time()
    FazFractal(vezes, lados, escala)
    print("Montando Gráfico")
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, lados, escala = VariaveisDeInput(Valores)
    FazFractal(vezes, lados, escala)
    print("Montando Gráfico")
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes, lados, escala = VariaveisDeInput(Valores)
    masterx = []
    mastery = []
    for fractallados in range(3, lados + 1):
        x = [escala * fractallados, escala * (fractallados + 1)]
        y = [0, 0]
        fractallados = lados + 3 - fractallados
        print("\n", fractallados, ' lados de ', lados)
        x, y = monta(x, y, vezes, fractallados)
        masterx.extend(x[::])
        mastery.extend(y[::])
        plt.plot(x, y)
    FazCalculo(masterx, mastery)
    print("Montando Gráfico")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, lados, escala = VariaveisDeInput(Valores)
    FazFractal(vezes, lados, escala)
    with PdfPages(r'filadekoch.pdf') as export_pdf:
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