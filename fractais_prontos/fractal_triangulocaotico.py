import matplotlib.pyplot as plt
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
import time


def fazcaotico(vezes, valor):
    contador = 0
    x1 = [0, 50, -50]
    y1 = [7500 ** 0.5, 0, 0]
    x = [0]
    y = [(7500 ** 0.5) / 2]
    while contador <= vezes:
        # print("%d de %d" % (contador, vezes))
        contador += 1
        a = randint(0, 2)
        x.append((x1[a] + x[-1]) / valor)
        y.append((y1[a] + y[-1]) / valor)
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        vezes, valor = 1000000, 2
    else:
        vezes = int(input("Digite a Quantidade de vezes(recomendado 100000 <= x <= 1000000): "))
        valor = float(input("Valor(triangulo de sierpinski coloque 2): "))
    return vezes, valor


def FazFractal(vezes, valor):
    x, y = fazcaotico(vezes, valor)
    return x, y


def FazFractalComTempo(Valores):
    vezes, valor = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(vezes, valor)
    print("Montando o gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    fim = time.time()
    print(str(round(fim-inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, valor = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, valor)
    print("Montando o gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    plt.show()


def SalvarEmPDF(Valores):
    vezes, valor = VariaveisDeInput(Valores)
    x, y = FazFractal(vezes, valor)
    plt.scatter(x, y, color="black", s=0.01)
    with PdfPages(r'triangulocaotico.pdf') as export_pdf:
        export_pdf.savefig()


def Begin():
    SalvarPDF = bool(input("(False) Para não salvar em PDF e (True) Para salvar: "))
    Valores = bool(input("(False) para valores personalizados e (True) para usar os valores padrões: "))
    if SalvarPDF:
        SalvarEmPDF(Valores)
    else:
        MostrarDesempenho = bool(input("(False) Para não contar o tempo de Execução e (True) para mostra: "))
        if MostrarDesempenho:
            FazFractalComTempo(Valores)
        else:
            FazFractalSemTempo(Valores)


if __name__ == "__main__":
    Begin()