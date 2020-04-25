import matplotlib.pyplot as plt
import math
# from matplotlib.backends.backend_pdf import PdfPages
# import time

vezes = int(input("Vezes: "))
lados = int(input("lados: "))
l = []
tam = int(input("Escala: "))
x = [0, tam]
y = [0, 0]
mudar = input("[s/n]Pra dentro?: ")
# inicio = time.time()

def f(x, y, lados, vez):
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

for vez in range(vezes):
    print(vez + 1, " de ", vezes)
    x, y = f(x, y, lados, vez)

print("Montando Gráfico")
# with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\generalizacaodacurvadekoch.pdf') as export_pdf:
plt.fill(x, y)
    # export_pdf.savefig()
# fim = time.time()
# print(str(round(fim - inicio, 5)) + "s")
plt.show()
