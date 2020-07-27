import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


def curvadodragao(x, y):
    novox = [x[-1]]
    novoy = [y[-1]]
    for item in range(1, len(x)):
        novox.append(novox[-1] - (y[-item] - y[-item - 1]))
        novoy.append(novoy[-1] + (x[-item] - x[-item - 1]))
    x = x + novox
    y = y + novoy
    return x, y


def fazdragao(vezes, escalonar):
    x = [0, 1]
    y = [0, 0]
    vez = 0
    while vez < vezes:
        vez += 1
        x, y = curvadodragao(x, y)
        if escalonar and vez > 2:
            x, y = arruma_escala(x, y)
        print("%d de %d" % (vez, vezes))
    return x, y


def arruma_escala(x, y):
    novox, novoy = [], []
    indice = 0
    limite = len(x)
    while indice < limite:
        novox.append(x[indice] / (2 ** 0.5))
        novoy.append(y[indice] / (2 ** 0.5))
        indice += 1
    return novox, novoy


def VariaveisDeInput(Valores):
    if Valores:
        vezes, escalonar = 20, False
    else:
        vezes = int(input("Digite a quantidade de vezes(recomendado <= 20): "))
        escalonar = bool(input("(False) Para não escalonar e (True) Para escalonar: "))
    return vezes, escalonar


def FazFractal(vezes, escalonar):
    x, y = fazdragao(vezes, escalonar)
    return x, y


def FazFractalComTempo(Valores):
    vezes, escalonar = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes, escalonar)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, escalonar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escalonar)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes, escalonar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escalonar)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, escalonar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, escalonar)
    plt.plot(x, y, color="black")
    with PdfPages(r'curvadodragao.pdf') as export_pdf:
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