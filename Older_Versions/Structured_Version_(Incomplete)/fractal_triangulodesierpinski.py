import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def organizaprafazer(x, y):
    novox, novoy = [], []
    for item in range(len(x)):
        x1, x2, x3, y1, y2, y3 = triangulodesierpinski(x[item], y[item])
        novox.extend((x1, x2, x3))
        novoy.extend((y1, y2, y3))
    return novox, novoy


def triangulodesierpinski(x, y):
    x1 = x[0]
    x2 = (x[0] + x[1]) / 2
    x3 = x[1]
    x4 = (x[1] + x[2]) / 2
    x5 = x[2]
    x6 = (x[2] + x[0]) / 2
    y1 = y[0]
    y2 = (y[0] + y[1]) / 2
    y3 = y[1]
    y4 = (y[1] + y[2]) / 2
    y5 = y[2]
    y6 = (y[2] + y[0]) / 2
    xtriangulo1 = [x1, x6, x2]
    ytriangulo1 = [y1, y6, y2]
    xtriangulo2 = [x2, x3, x4]
    ytriangulo2 = [y2, y3, y4]
    xtriangulo3 = [x6, x4, x5]
    ytriangulo3 = [y6, y4, y5]
    return xtriangulo1, xtriangulo2, xtriangulo3, ytriangulo1, ytriangulo2, ytriangulo3


def fazcadatriangulo(x, y):
    novox, novoy = [], []
    indice = 0
    limite = len(x)
    while indice < limite:
        novox.append([x[indice][0], x[indice][1], x[indice][2]])
        novoy.append([y[indice][0], y[indice][1], y[indice][2]])
        indice += 1
    return novox, novoy


def montagrafico(novox, novoy):
    for item in range(len(novox)):
        plt.fill(novox[item], novoy[item], color="black", linewidth=1)


def fazsierpinski(vezes, t):
    vez = 0
    x = [[-t / 2, 0, t / 2]]
    y = [[-t * 3 ** 0.5 / 2, 0, -t * 3 ** 0.5 / 2]]
    while vez < vezes:
        vez += 1
        x, y = organizaprafazer(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho = 8, 50
    else:
        vezes = int(input("Digite quantas vezes (recomendado <= 8): "))
        tamanho = int(input("Digite o tamanho do lado do triângulo (recomendado 50): "))
    return vezes, tamanho


def FazFractal(vezes, tamanho):
    x, y = fazsierpinski(vezes, tamanho)
    novox, novoy = fazcadatriangulo(x, y)
    print("Montando o Gráfico")
    montagrafico(novox, novoy)


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

def criaunicalista(x):
    novox = []
    for item in x:
        novox.extend(item)
    return novox

def PropriedadeQuadrado(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    x, y = fazsierpinski(vezes, tamanho)
    novox, novoy= fazcadatriangulo(x,y)
    x, y = criaunicalista(x), criaunicalista(y)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    montagrafico(novox, novoy)
    plt.show()


def SalvarEmPDF(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    with PdfPages(r'triangulodesierpinski.pdf') as export_pdf:
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