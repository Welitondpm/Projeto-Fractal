import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *
from progressaopropriedadeporquadrados import *


def organizaprafazer(x, y):
    novox, novoy = [], []
    for item in range(len(x)):
        x1, x2, x3, x4, x5, x6, x7, x8, y1, y2, y3, y4, y5, y6, y7, y8 = tapetedesierpinski(x[item], y[item])
        novox.extend((x1, x2, x3, x4, x5, x6, x7, x8))
        novoy.extend((y1, y2, y3, y4, y5, y6, y7, y8))
    return novox, novoy


def tapetedesierpinski(x, y):
    x1 = x[0]
    x2 = x1 + (x[3] - x[0]) / 3
    x3 = x1 + (x[3] - x[0]) * 2 / 3
    x4 = x[3]
    y1 = y[0]
    y2 = y1 + (y[2] - y[0]) / 3
    y3 = y1 + (y[2] - y[0]) * 2 / 3
    y4 = y[2]
    xquadrado1 = [x1, x1, x2, x2]
    yquadrado1 = [y1, y2, y2, y1]
    xquadrado2 = [x2, x2, x3, x3]
    yquadrado2 = [y1, y2, y2, y1]
    xquadrado3 = [x3, x3, x4, x4]
    yquadrado3 = [y1, y2, y2, y1]
    xquadrado4 = [x1, x1, x2, x2]
    yquadrado4 = [y2, y3, y3, y2]
    xquadrado5 = [x3, x3, x4, x4]
    yquadrado5 = [y2, y3, y3, y2]
    xquadrado6 = [x1, x1, x2, x2]
    yquadrado6 = [y3, y4, y4, y3]
    xquadrado7 = [x2, x2, x3, x3]
    yquadrado7 = [y3, y4, y4, y3]
    xquadrado8 = [x3, x3, x4, x4]
    yquadrado8 = [y3, y4, y4, y3]
    return xquadrado1, xquadrado2, xquadrado3, xquadrado4, xquadrado5, xquadrado6, xquadrado7, xquadrado8, yquadrado1, yquadrado2, yquadrado3, yquadrado4, yquadrado5, yquadrado6, yquadrado7, yquadrado8


def progressaodapropriedade():
    vezes, tamanho = 7, 50
    valor = int(input("Digite um valor inteiro, essa é a quantidade de quadrados,\n(Atenção o valor será elevado ao quadrado!!):\n\n >>> "))
    vez = 0
    x = [[0, 0, tamanho, tamanho]]
    y = [[0, tamanho, tamanho, 0]]
    novox = []
    novoy = []
    masterx = []
    mastery = []
    while vez < vezes:
        novox, novoy = criaunicalista(x), criaunicalista(y)
        quadradospintados = progressaoFazCalculo(novox, novoy, valor)
        masterx.append(vez)
        mastery.append(quadradospintados)
        vez += 1
        x, y = organizaprafazer(x, y)
    novox, novoy = criaunicalista(x), criaunicalista(y)
    quadradospintados = progressaoFazCalculo(novox, novoy, valor)
    masterx.append(vez)
    mastery.append(quadradospintados)
    plt.plot(masterx, mastery)
    plt.scatter(masterx, mastery)
    plt.title("Progressão da Propriedade por quadrados\nFractal Tapete de sierpinski")
    plt.xlabel("vezes")
    plt.ylabel("Quadrados Pintados")
    print("Montando o Gráfico")
    plt.show()


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
        vezes = int(input("Digite quantas vezes (recomendado <= 4): "))
        tamanho = int(input("Digite o tamanho do lado do quadrado (recomendado 50): "))
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
    x, y = criaunicalista(x), criaunicalista(y)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, tamanho = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho)
    with PdfPages(r'tapetedesierpinski.pdf') as export_pdf:
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
    # progressaodapropriedade()