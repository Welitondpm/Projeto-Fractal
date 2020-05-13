import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def organizaprafazer(x, y, z):
    nx, ny, nz = [], [], []
    for item in range(len(x)):
        x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4 = triangulodesierpinski(x[item], y[item], z[item])
        nx.extend((x1, x2, x3, x4))
        ny.extend((y1, y2, y3, y4))
        nz.extend((z1, z2, z3, z4))
    return nx, ny, nz


def triangulodesierpinski(x, y, z):
    x1 = x[0]
    x2 = x1+(x[1]-x[0])/2
    x3 = x[1]
    x4 = x3+(x[2]-x[1])/2
    x5 = x[2]
    x6 = x1+(x[2]-x[0])/2
    x7 = sum(x)/len(x)
    x8 = (x1+x[3])/2
    x9 = (x3+x[3])/2
    x10 = (x5+x[3])/2
    x11 = x[3]
    y1 = y[0]
    y2 = y1+(y[1]-y[0])/2
    y3 = y[1]
    y4 = y3+(y[2]-y[1])/2
    y5 = y[2]
    y6 = y1+(y[2]-y[0])/2
    y7 = sum(y)/len(y)
    y8 = (y1+y[3])/2
    y9 = (y3+y[3])/2
    y10 = (y5+y[3])/2
    y11 = y[3]
    z1 = z[0]
    z2 = z1+(z[1]-z[0])/2
    z3 = z[1]
    z4 = z3+(z[2]-z[1])/2
    z5 = z[2]
    z6 = z1+(z[2]-z[0])/2
    z7 = sum(z)/len(z)
    z8 = (z1+z[3])/2
    z9 = (z3+z[3])/2
    z10 = (z5+z[3])/2
    z11 = z[3]
    return [x1, x2, x6, x8], [x2, x3, x4, x9], [x6, x4, x5, x10], [x8, x9, x10, x11], [y1, y2, y6, y8], [y2, y3, y4, y9], [y6, y4, y5, y10], [y8, y9, y10, y11], [z1, z2, z6, z8], [z2, z3, z4, z9], [z6, z4, z5, z10], [z8, z9, z10, z11]


def fazcubo(x, y, z):
    x = [x[0], x[1], x[2], x[0], x[3], x[1], x[2], x[3]]
    y = [y[0], y[1], y[2], y[0], y[3], y[1], y[2], y[3]]
    z = [z[0], z[1], z[2], z[0], z[3], z[1], z[2], z[3]]
    return x, y, z


def montagrafico(novox, novoy, novoz):
    for item in range(len(novox)):
        print(item, " de ", len(novox))
        x, y, z = fazcubo(novox[item], novoy[item], novoz[item])
        plt.plot(x, y, z, color="black", linewidth=1)


def fazsierpinski(vezes, t):
    vez = 0
    x = [[-t / 2, 0, t / 2, 0]]
    y = [[0, t * 3 ** 0.5 / 2, 0, t * 3 ** 0.5 / 6]]
    z = [[0, 0, 0, t*3**.5/6]]
    while vez < vezes:
        vez += 1
        x, y, z = organizaprafazer(x, y, z)
        print("%d de %d" % (vez, vezes))
    return x, y, z


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho = 4, 50
    else:
        vezes = int(input("Digite quantas vezes (recomendado <= 7): "))
        tamanho = int(input("Digite o tamanho do lado do triângulo (recomendado 50): "))
    return vezes, tamanho


def FazFractal(vezes, tamanho):
    fig = plt.figure()
    sub = fig.add_subplot(1, 1, 1, projection='3d')
    x, y, z = fazsierpinski(vezes, tamanho)
    print("Montando o Gráfico")
    montagrafico(x, y, z)


def FazFractalComTempo(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    inicio = time.time()
    FazFractal(vezes, tamanho)
    fim = time.time()
    print(str(round(fim-inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    plt.show()


def criaunicalista(x):
    novox = []
    for i in x:
        for j in i:
            novox.append(j)
    return novox


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
    with PdfPages(r'triangulodesierpinski.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(xinput("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        '''ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: (!!INDIPONÍVEL!!"))
        if ExecutarPropriedade:
            PropriedadeQuadrado(Valores)
        else:'''
        MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
        if MostrarDesempenho:
            FazFractalComTempo(Valores)
        else:
            FazFractalSemTempo(Valores)


if __name__ == "__main__":
    # Begin()
    FazFractal(5, 81)
    plt.show()
