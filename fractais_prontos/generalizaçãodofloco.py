import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time


def f(x, y, lados, vez, mudar):
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
        if vez == 0:
            d = 3 * d
            nx = [x[i]]
            ny = [y[i]]
        else:
            nx = [x[i] + dx / 3]
            ny = [y[i] + dy / 3]
        jj = 0
        while jj < lados - 2:
            nx += [nx[-1] + (d / 3) * math.cos(angdado + ang)]
            ny += [ny[-1] + (d / 3) * math.sin(angdado + ang)]
            ang -= (math.pi - oang)
            jj += 1
        ang = oang
        if vez == 0:
            nx += [x[i + 1]]
            ny += [y[i + 1]]
            nx += [x[i]]
            ny += [y[i]]
            if mudar == 's' or mudar == 'S':
                nx = nx[::-1]
                ny = ny[::-1]
        else:
            nx += [x[i] + 2 * dx / 3]
            ny += [y[i] + 2 * dy / 3]
            nx = [x[i]] + nx + [x[i + 1]]
            ny = [y[i]] + ny + [y[i + 1]]
        nxf += nx
        nyf += ny
    return nxf, nyf


def VariaveisDeInput(Valores):
    if Valores:
        vezes, lados, tam, mudar = 5, 7, 10, "n"
    else:
        vezes = int(input("Vezes: "))
        lados = int(input("lados: "))
        tam = int(input("Escala: "))
        mudar = input("[s/n]Pra dentro?: ")
    return vezes, lados, tam, mudar


def FazFractal(vezes, lados, tam, mudar):
    x = [0, tam]
    y = [0, 0]
    for vez in range(vezes):
        print(vez + 1, " de ", vezes)
        x, y = f(x, y, lados, vez, mudar)
    return x, y


def FazFractalComTempo(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes, lados, tam, mudar)
    print("Montando Gráfico")
    plt.fill(x, y)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, lados, tam, mudar)
    print("Montando Gráfico")
    plt.fill(x, y)
    plt.show()


def SalvarEmPDF(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, lados, tam, mudar)
    plt.fill(x, y, color="black")
    with PdfPages(r'generalizacaodofloco.pdf') as export_pdf:
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