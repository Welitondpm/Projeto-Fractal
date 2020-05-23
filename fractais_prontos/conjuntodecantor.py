import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
# from propriedadeporquadrados import *


def organizaprafazer(x, valordoy):
    novox, novoy = [], []
    for item in range(len(x)):
        x1, x2, y1, y2 = linhacantor(x[item], valordoy)
        novox.extend((x1, x2))
        novoy.extend((y1, y2))
    return novox, novoy


def linhacantor(x, valordoy):
    x1 = x[0]
    x2 = x1 + ((x[1] - x[0]) / 3)
    x3 = x[1]
    x4 = x3 - ((x[1] - x[0]) / 3)
    linha1 = [x1, x2]
    linha2 = [x3, x4]
    return linha1, linha2, [valordoy, valordoy], [valordoy, valordoy]


def fazcadalinha(x, y):
    novox, novoy = [], []
    indice = 0
    tamanho = len(x)
    while indice < tamanho:
        novox.append([x[indice][0], x[indice][1]])
        novoy.append([y[indice][0], y[indice][1]])
        indice += 1
    return novox, novoy


def montagrafico(novox, novoy):
    for item in range(len(novox)):
        plt.plot(novox[item], novoy[item], color="black", linewidth=1)


def fazcantor(vezes, t):
    vez = 0
    x = [[0, t]]
    y = [[0, 0]]
    while vez < vezes:
        vez += 1
        montagrafico(x, y)
        x, y = organizaprafazer(x, vez)
        print("%d de %d" % (vez, vezes))
    montagrafico(x, y)
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho = 10, 50
    else:
        vezes = int(input("Digite quantas vezes (recomendado <= 12): "))
        tamanho = int(input("Digite o tamanho da Linha (recomendado 50): "))
    return vezes, tamanho


def FazFractal(vezes, tamanho):
    x, y = fazcantor(vezes, tamanho)
    fazcadalinha(x, y)
    print("Montando o Gráfico")


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


# def PropriedadeQuadrado(Valores):
#     vezes, tamanho = VariaveisDeInput(Valores)
#     x, y = fazsierpinski(vezes, tamanho)
#     novox, novoy= fazcadatriangulo(x,y)
#     x, y = criaunicalista(x), criaunicalista(y)
#     FazCalculo(x, y)
#     print("Montando o Gráfico")
#     montagrafico(novox, novoy)
#     plt.show()


def SalvarEmPDF(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    with PdfPages(r'conjuntodecantor.pdf') as export_pdf:
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