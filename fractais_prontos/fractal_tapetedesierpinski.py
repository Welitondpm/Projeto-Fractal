import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def organizaprafazer(x, y):
    nx, ny = [], []
    for item in range(len(x)):
        x1, x2, x3, x4, x5, x6, x7, x8, y1, y2, y3, y4, y5, y6, y7, y8 = tapetedesierpinski(x[item], y[item])
        nx.extend((x1, x2, x3, x4, x5, x6, x7, x8))
        ny.extend((y1, y2, y3, y4, y5, y6, y7, y8))
    return nx, ny


def tapetedesierpinski(x, y):
    x1 = x[0]
    x2 = x1+(x[3] - x[0]) / 3
    x3 = x1+(x[3] - x[0]) * 2 / 3
    x4 = x[3]
    y1 = y[0]
    y2 = y1+(y[2] - y[0]) / 3
    y3 = y1+(y[2] - y[0]) * 2 / 3
    y4 = y[2]
    t1x = [x1, x1, x2, x2]
    t1y = [y1, y2, y2, y1]
    t2x = [x2, x2, x3, x3]
    t2y = [y1, y2, y2, y1]
    t3x = [x3, x3, x4, x4]
    t3y = [y1, y2, y2, y1]
    t4x = [x1, x1, x2, x2]
    t4y = [y2, y3, y3, y2]
    t5x = [x3, x3, x4, x4]
    t5y = [y2, y3, y3, y2]
    t6x = [x1, x1, x2, x2]
    t6y = [y3, y4, y4, y3]
    t7x = [x2, x2, x3, x3]
    t7y = [y3, y4, y4, y3]
    t8x = [x3, x3, x4, x4]
    t8y = [y3, y4, y4, y3]
    return t1x, t2x, t3x, t4x, t5x, t6x, t7x, t8x, t1y, t2y, t3y, t4y, t5y, t6y, t7y, t8y


def montagrafico(novox, novoy):
    for item in range(len(novox)):
        plt.fill(novox[item], novoy[item], color="black", linewidth=1)


def fazsierpinski(vezes, t):
    vez = 0
    x = [[0, 0, t, t]]
    y = [[0, t, t, 0]]
    while vez < vezes:
        vez += 1
        x, y = organizaprafazer(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho = 4, 50
    else:
        vezes = int(input("Digite quantas vezes (recomendado <= 7): "))
        tamanho = int(input("Digite o tamanho do lado do triângulo (recomendado 50): "))
    return vezes, tamanho


def FazFractal(vezes, tamanho):
    x, y = fazsierpinski(vezes, tamanho)
    print("Montando o Gráfico")
    montagrafico(x, y)


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
    with PdfPages(r'tapetedesierpinski.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        # ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: (!!INDIPONÍVEL!!"))
        # if ExecutarPropriedade:
        #     PropriedadeQuadrado(Valores)
        # else:
        MostrarDesempenho = bool(
            input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
        if MostrarDesempenho:
            FazFractalComTempo(Valores)
        else:
            FazFractalSemTempo(Valores)


if __name__ == "__main__":
    # Begin()
    FazFractal(4, 81)
    plt.show()
