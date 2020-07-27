import matplotlib.pyplot as plt
import time
from matplotlib.backends.backend_pdf import PdfPages
from propriedadeporquadrados import *


def é_primo(valor):
    for item in range(2, int(valor ** 0.5) + 1):
        if valor % item == 0:
            return False
    return True


def binario(valor):
    lista = []
    while valor >= 2:
        resto = valor % 2
        valor //= 2
        lista.append(resto)
    if valor == 1:
        lista.append(valor)
    lista.reverse()
    return lista


def decimal(valor):
    indice = 0
    soma = 0
    for item in valor:
        soma += (item * (2 ** indice))
        indice += 1
    return soma


def fazbinario(fim, contagem):
    x, y = [], []
    if contagem:
        for item in range(fim):
            print("%d de %d" % (item, fim))
            ycalculado = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                ycalculado = item - deci
            x.append(item)
            y.append(ycalculado)
    else:
        for item in range(fim):
            ycalculado = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                ycalculado = item - deci
            x.append(item)
            y.append(ycalculado)
    return x, y


def VariaveisDeInput(Valores):
    if Valores:
        fim, contagem = 262144, False
    else:
        fim = int(input("Fim (recomendado <= 262144): "))
        contagem = bool(input("Deseja ver o valor atual? (True/False): "))
    return fim, contagem


def FazFractal(fim, contagem):
    x, y = fazbinario(fim, contagem)
    return x, y


def FazFractalComTempo(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    inicio = time.time()
    x, y = FazFractal(fim, contagem)
    print("Montando o Gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    x, y = FazFractal(fim, contagem)
    print("Montando o Gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    plt.show()


def PropriedadeQuadrado(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    x, y = FazFractal(fim, contagem)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    plt.show()


def SalvarEmPDF(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    x, y = FazFractal(fim, contagem)
    plt.scatter(x, y, color="black", s=0.01)
    with PdfPages(r'binario.pdf') as export_pdf:
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