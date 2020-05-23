import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
import time
# from propriedadeporquadrados import *


def organizaprafazer(x, y, z):
    novox, novoy, novoz = [], [], []
    for item in range(len(x)):
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20 = esponjademenger(x[item], y[item], z[item])
        novox.extend((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20))
        novoy.extend((y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20))
        novoz.extend((z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20))
    return novox, novoy, novoz


def esponjademenger(x, y, z):
    x1 = x[0]
    x2 = x1 + (x[3] - x[0]) / 3
    x3 = x1 + (x[3] - x[0]) * 2 / 3
    x4 = x[3]
    y1 = y[0]
    y2 = y1 + (y[2] - y[0]) / 3
    y3 = y1 + (y[2] - y[0]) * 2 / 3
    y4 = y[2]
    z1 = z[0]
    z2 = z1 + (z[4] - z[0]) / 3
    z3 = z1 + (z[4] - z[0]) * 2 / 3
    z4 = z[4]
    t1x = [x1, x1, x2, x2]
    t1x += t1x[::-1]
    t1y = [y1, y2, y2, y1]
    t1y += t1y[::-1]
    t2x = [x2, x2, x3, x3]
    t2x += t2x[::-1]
    t2y = [y1, y2, y2, y1]
    t2y += t2y[::-1]
    t3x = [x3, x3, x4, x4]
    t3x += t3x[::-1]
    t3y = [y1, y2, y2, y1]
    t3y += t3y[::-1]
    t4x = [x1, x1, x2, x2]
    t4x += t4x[::-1]
    t4y = [y2, y3, y3, y2]
    t4y += t4y[::-1]
    t6x = [x3, x3, x4, x4]
    t6x += t6x[::-1]
    t6y = [y2, y3, y3, y2]
    t6y += t6y[::-1]
    t7x = [x1, x1, x2, x2]
    t7x += t7x[::-1]
    t7y = [y3, y4, y4, y3]
    t7y += t7y[::-1]
    t8x = [x2, x2, x3, x3]
    t8x += t8x[::-1]
    t8y = [y3, y4, y4, y3]
    t8y += t8y[::-1]
    t9x = [x3, x3, x4, x4]
    t9x += t9x[::-1]
    t9y = [y3, y4, y4, y3]
    t9y += t9y[::-1]
    tz1 = [z1, z1, z1, z1, z2, z2, z2, z2]
    tz2 = [z2, z2, z2, z2, z3, z3, z3, z3]
    tz3 = [z3, z3, z3, z3, z4, z4, z4, z4]
    return t1x, t2x, t3x, t4x, t6x, t7x, t8x, t9x, t1x, t3x, t7x, t9x, t1x, t2x, t3x, t4x, t6x, t7x, t8x, t9x, t1y, t2y, t3y, t4y, t6y, t7y, t8y, t9y, t1y, t3y, t7y, t9y, t1y, t2y, t3y, t4y, t6y, t7y, t8y, t9y, tz1, tz1, tz1, tz1, tz1, tz1, tz1, tz1, tz2, tz2, tz2, tz2, tz3, tz3, tz3, tz3, tz3, tz3, tz3, tz3


def fazcubo(x, y, z):
    fig=plt.figure()
    sub=fig.add_subplot(1,1,1,projection='3d')
    xx, yy, zz = [x[0], x[0], x[1], x[1], x[2], x[2], x[3], x[3], x[0]], [y[0], y[0], y[1], y[1], y[2], y[2], y[3], y[3], y[0]], [z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1], z[0], z[0]]
    return xx + xx, yy + yy, zz + [z[0], z[0], z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1]]


def montagrafico(novox, novoy, novoz):
    for item in range(len(novox)):
        # print(item, " de ", len(novox))
        x, y, z = fazcubo(novox[item], novoy[item], novoz[item])
        plt.plot(x, y, z, color="black", linewidth=1)


def fazsierpinski(vezes, t):
    vez = 0
    x = [[0, 0, t, t, t, t, 0, 0]]
    y = [[0, t, t, 0, 0, t, t, 0]]
    z = [[0, 0, 0, 0, t, t, t, t]]
    while vez < vezes:
        vez += 1
        x, y, z = organizaprafazer(x, y, z)
        print("%d de %d" % (vez, vezes))
    return x, y, z


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho = 3, 50
    else:
        vezes = int(input("Digite quantas vezes (recomendado <= 3): "))
        tamanho = int(input("Digite o tamanho do lado do quadrado (recomendado 50): "))
    return vezes, tamanho


def FazFractal(vezes, tamanho):
    x, y, z = fazsierpinski(vezes, tamanho)
    print("Montando o Gráfico")
    montagrafico(x, y, z)


def FazFractalComTempo(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    inicio = time.time()
    FazFractal(vezes, tamanho)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    plt.show()


# def criaunicalista(x):
#     novox = []
#     for item in x:
#         novox.extend(item)
#     return novox


# def PropriedadeQuadrado(Valores):
#     vezes, tamanho = VariaveisDeInput(Valores)
#     x, y = fazsierpinski(vezes, tamanho)
#     novox, novoy = fazcadatriangulo(x, y)
#     x, y = criaunicalista(x), criaunicalista(y)
#     FazCalculo(x, y)
#     print("Montando o Gráfico")
#     montagrafico(novox, novoy)
#     plt.show()


def SalvarEmPDF(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    with PdfPages(r'esponjademenger.pdf') as export_pdf:
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
