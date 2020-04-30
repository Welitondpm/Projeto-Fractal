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


def fazdragao(vezes):
    x = [0, 1]
    y = [0, 0]
    vez = 0
    esc=bool(input("(False) Para não escalonar e (True) Para escalonar: "))
    while vez < vezes:
        vez += 1
        x, y = curvadodragao(x, y)
        if esc and vez > 2:
            x, y = arruma_escala(x), arruma_escala(y)
        print("%d de %d" % (vez, vezes))
    return x, y

def arruma_escala(x):
    novox=[]
    for i in x:
        novox.append(i/(2**.5))
    return novox


def VariaveisDeInput(Valores):
    if Valores:
        vezes = 20
    else:
        vezes = int(input("Digite a quantidade de vezes(recomendado <= 20): "))
    return vezes


def FazFractal(vezes):
    x, y = fazdragao(vezes)
    return x, y


def FazFractalComTempo(Valores):
    vezes = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    fim = time.time()
    print(str(round(fim-inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def SalvarEmPDF(Valores):
    vezes = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes)
    plt.plot(x, y, color="black")
    with PdfPages(r'curvadodragao.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
        if ExecutarPropriedade:
            PropriedadeQuadrado(Valores)
        else:
            MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
            if MostrarDesempenho:
                FazFractalComTempo(Valores)
            else:
                FazFractalSemTempo(Valores)


if __name__ == "__main__":
    Begin()