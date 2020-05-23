import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time


def f(x, y, lados):
    somadosangint = 180 * (lados - 2)
    ang = somadosangint / lados * math.pi / 180
    oang = ang
    nxf, nyf = [], []
    for i in range(len(x) - 1):
        dx = x[i + 1] - x[i]
        dy = y[i + 1] - y[i]
        d = (dx ** 2 + dy ** 2) ** 0.5
        if dx < 0:
            d *= -1
        if dx != 0:
            angdado = math.atan(dy / dx)
        elif dy > 0:
            angdado = math.pi / 2
        elif dy < 0:
            angdado = 3 * math.pi / 2
        else:
            continue
        nx = [x[i] + dx / 3]
        ny = [y[i] + dy / 3]
        jj = 0
        while jj < lados - 2:
            nx += [nx[-1] + (d / 3) * math.cos(angdado + ang)]
            ny += [ny[-1] + (d / 3) * math.sin(angdado + ang)]
            ang -= (math.pi - oang)
            jj += 1
        ang = oang
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
    x = [0, tam]
    y = [0, 0]
    for i in range(3, lados + 1):
        i = lados + 1 - i
        print("Está fazendo o fractal do maior até o 3: ", i)
        x, y = monta(x, y, vezes, i)
        plt.plot(x, y)
        x = [0, tam]
        y = [0, 0]
    

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
    with PdfPages(r'progresaodageneralizacaodekoch.pdf') as export_pdf:
        export_pdf.savefig()
    

def MostrarTempo(Valores):
    MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
    if MostrarDesempenho:
        FazFractalComTempo(Valores)
    else:
        FazFractalSemTempo(Valores)


# def MostrarPropriedade(Valores):
#     ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
#     if ExecutarPropriedade:
#         PropriedadeQuadrado(Valores)
#     else:
#         MostrarTempo(Valores)


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        # MostrarPropriedade(Valores)
        MostrarTempo(Valores)


if __name__ == "__main__":
    Begin()