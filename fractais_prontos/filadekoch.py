import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time


def f(x, y, lados):
    somadosanguloint = 180 * (lados - 2)
    angulo = somadosanguloint / lados * math.pi / 180
    oangulo = angulo
    nxf, nyf = [], []
    for i in range(len(x) - 1):
        dx = x[i + 1] - x[i]
        dy = y[i + 1] - y[i]
        d = (dx ** 2 + dy ** 2) ** 0.5
        if dx < 0:
            d *= -1
        if dx != 0:
            angulodado = math.atan(dy / dx)
        elif dy > 0:
            angulodado = math.pi / 2
        elif dy < 0:
            angulodado = 3 * math.pi / 2
        else:
            continue
        nx = [x[i] + dx / 3]
        ny = [y[i] + dy / 3]
        jj = 0
        while jj < lados - 2:
            nx += [nx[-1] + (d / 3) * math.cos(angulodado + angulo)]
            ny += [ny[-1] + (d / 3) * math.sin(angulodado + angulo)]
            angulo -= (math.pi - oangulo)
            jj += 1
        angulo = oangulo
        nx += [x[i] + 2 * dx / 3]
        ny += [y[i] + 2 * dy / 3]
        nx = [x[i]] + nx + [x[i + 1]]
        ny = [y[i]] + ny + [y[i + 1]]
        nxf += nx
        nyf += ny
    return nxf, nyf


def monta(x, y, vezes, lados):
    for vez in range(1, vezes + 1):
        print(vez, " de ", vezes)
        x, y = f(x, y, lados)
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, lados, tam = 5, 7, 10
    else:
        vezes = int(input("Vezes: "))
        lados = int(input("lados: "))
        tam = int(input("Escala: "))
    return vezes, lados, tam


def FazFractal(vezes, lados, tam):
    for i in range(3, lados+1):
        x = [tam * i, tam * (i + 1)]
        y = [0, 0]
        i = lados + 3 - i
        print("\n", i, ' lados de ', lados)
        x, y = monta(x, y, vezes, i)
        plt.plot(x, y)


def FazFractalComTempo(Valores):
    vezes, lados, tam = VariaveisDeInput(Valores)
    inicio = time.time()
    FazFractal(vezes, lados, tam)
    print("Montando Gráfico")
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, lados, tam = VariaveisDeInput(Valores)
    FazFractal(vezes, lados, tam)
    print("Montando Gráfico")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, lados, tam = VariaveisDeInput(Valores)
    FazFractal(vezes, lados, tam)
    with PdfPages(r'filadekoch.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
        if MostrarDesempenho:
            FazFractalComTempo(Valores)
        else:
            FazFractalSemTempo(Valores)


if __name__ == "__main__":
    Begin()