import matplotlib.pyplot as plt
import math
# from matplotlib.backends.backend_pdf import PdfPages
# import time

vezes = int(input("Vezes: "))
lados = int(input("lados: "))
l = []
tam = int(input("Escala: "))
# inicio = time.time()


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


for i in range(3, lados+1):
    x = [tam * i, tam * (i + 1)]
    y = [0, 0]
    i = lados + 3 - i
    print("\n", i, ' lados de ', lados)
    x, y = monta(x, y, vezes, i)
    # with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\generalizacaodacurvadekoch.pdf') as export_pdf:
    plt.plot(x, y)
        # export_pdf.savefig()

print("Montando Gráfico")
# fim = time.time()
# print(str(round(fim - inicio, 5)) + "s")
plt.show()
