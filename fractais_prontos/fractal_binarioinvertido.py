import matplotlib.pyplot as plt
import time
from matplotlib.backends.backend_pdf import PdfPages


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


def decimal(lista):
    a = 0
    soma = 0
    for item in lista:
        soma += (item * (2 ** a))
        a += 1
    return soma


def fazbinario(fim, contagem):
    xs = []
    ys = []
    if contagem:
        for item in range(fim):
            print("%d de %d" % (item, fim))
            y = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                y = item - deci
            xs.append(item)
            ys.append(y)
    else:
        for item in range(fim):
            y = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                y = item - deci
            xs.append(item)
            ys.append(y)
    return xs, ys


def VariaveisDeInput(Valores):
    if Valores:
        fim, contagem = 262144, False
    else:
        fim = int(input("Fim (recomendado <= 262144): "))
        contagem = bool(input("Deseja ver o valor atual? (True/False): "))
    return fim, contagem


def FazFractal(fim, contagem):
    xs, ys = fazbinario(fim, contagem)
    return xs, ys


def FazFractalComTempo(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    inicio = time.time()
    xs, ys = FazFractal(fim, contagem)
    print("Montando o Gráfico")
    plt.scatter(xs, ys, color="black", s=0.01)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    xs, ys = FazFractal(fim, contagem)
    print("Montando o Gráfico")
    plt.scatter(xs, ys, color="black", s=0.01)
    plt.show()


def SalvarEmPDF(Valores):
    fim, contagem = VariaveisDeInput(Valores)
    xs, ys = FazFractal(fim, contagem)
    plt.scatter(xs, ys, color="black", s=0.01)
    with PdfPages(r'binario.pdf') as export_pdf:
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