import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time


def fazcalculo(x, y, lados, vez, mudar):
    somadosangint = 180 * (lados - 2)
    ang = somadosangint / lados * math.pi / 180
    angulobackup = ang
    novoxfinal, novoyfinal = [], []
    for indice in range(len(x) - 1):
        differencex = x[indice + 1] - x[indice]
        differencey = y[indice + 1] - y[indice]
        distanciaxy = (differencex ** 2 + differencey ** 2) ** 0.5
        if differencex < 0:
            distanciaxy *= -1
        if differencex != 0:
            angdado = math.atan(differencey / differencex)
        elif differencey > 0:
            angdado = math.pi / 2
        elif differencey < 0:
            angdado = 3 * math.pi / 2
        else:
            continue
        if vez == 0:
            distanciaxy = 3 * distanciaxy
            novox = [x[indice]]
            novoy = [y[indice]]
        else:
            novox = [x[indice] + differencex / 3]
            novoy = [y[indice] + differencey / 3]
        contadorwhile = 0
        while contadorwhile < lados - 2:
            novox += [novox[-1] + (distanciaxy / 3) * math.cos(angdado + ang)]
            novoy += [novoy[-1] + (distanciaxy / 3) * math.sin(angdado + ang)]
            ang -= (math.pi - angulobackup)
            contadorwhile += 1
        ang = angulobackup
        if vez == 0:
            novox += [x[indice + 1]]
            novoy += [y[indice + 1]]
            novox += [x[indice]]
            novoy += [y[indice]]
            if mudar == 's' or mudar == 'S':
                novox = novox[::-1]
                novoy = novoy[::-1]
        else:
            novox += [x[indice] + 2 * differencex / 3]
            novoy += [y[indice] + 2 * differencey / 3]
            novox = [x[indice]] + novox + [x[indice + 1]]
            novoy = [y[indice]] + novoy + [y[indice + 1]]
        novoxfinal += novox
        novoyfinal += novoy
    return novoxfinal, novoyfinal


def VariaveisDeInput(Valores):
    if Valores:
        vezes, lados, tam, mudar = 5, 7, 10, "n"
    else:
        vezes = int(input("Vezes: "))
        lados = int(input("lados: "))
        tam = int(input("Escala: "))
        mudar = str(input("[s/n]Pra dentro?: "))
    return vezes, lados, tam, mudar


def FazFractal(vezes, lados, tam, mudar):
    x = [0, tam]
    y = [0, 0]
    for vez in range(vezes):
        print(vez + 1, " de ", vezes)
        x, y = fazcalculo(x, y, lados, vez, mudar)
    return x, y


def FazFractalComTempo(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes, lados, tam, mudar)
    print("Montando Gráfico")
    plt.fill(x, y)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, lados, tam, mudar)
    print("Montando Gráfico")
    plt.fill(x, y)
    plt.show()


def SalvarEmPDF(Valores):
    vezes, lados, tam, mudar = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, lados, tam, mudar)
    plt.fill(x, y, color="black")
    with PdfPages(r'generalizacaodofloco.pdf') as export_pdf:
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