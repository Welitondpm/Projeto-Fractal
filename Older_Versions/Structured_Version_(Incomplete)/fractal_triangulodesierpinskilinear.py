import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time


def faztriangulo(xrecebido, yrecebido):
    xdevolver, ydevolver = [], []
    for item in range(len(xrecebido)):
        x = xrecebido[item]
        y = yrecebido[item]
        if y[1] - y[0] == 0:
            x1 = x[0]
            x2 = x[0]+(x[1] - x[0]) / 4
            x3 = x[0]+(x[1] - x[0]) * 3 / 4
            x4 = x[1]
            y1 = y[0]
            y2 = y[0] + abs(x[1] - x[0]) / 4
            y3 = y2
            y4 = y[1]
        elif x[1] - x[0] == 0:
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 3
            y3 = y[0] + (y[1] - y[0]) * 2 / 3
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] + (y[1] - y[0]) / 3
            x3 = x2
            x4 = x[1]
        elif x[1] > x[0] and y[1] > y[0]:  # /^
            y1 = y[0]
            y2 = y1
            y3 = y[0] + (y[1] - y[0]) / 2
            y4 = y[1]
            x1 = x[0]
            x2 = x[1]
            x3 = x2 + (y[1] - y[0]) / 2
            x4 = x2
        elif x[1] < x[0] and y[1] > y[0]:  # ^\
            y1 = y[0]
            y2 = y1
            y3 = y[0] + (y[1] - y[0]) / 2
            y4 = y[1]
            x1 = x[0]
            x2 = x[1]
            x3 = x2 - (y[1] - y[0]) / 2
            x4 = x2
        elif x[1] < x[0] and y[1] < y[0]:  # _/
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 2
            y3 = y[1]
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] - (y[1] - y[0]) / 2
            x3 = x1
            x4 = x[1]
        elif x[1] > x[0] and y[1] < y[0]:  # \_
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 2
            y3 = y[1]
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] + (y[1] - y[0]) / 2
            x3 = x1
            x4 = x[1]
        xdevolver += [[x1, x2], [x2, x3], [x3, x4]]
        ydevolver += [[y1, y2], [y2, y3], [y3, y4]]
    return xdevolver, ydevolver


def VariaveisDeInput(Valores):
    if Valores:
        vezes = 12
    else:
        vezes = int(input("Digite a quantidade de vezes ( <= 12): "))
    x = [[0, 1]]
    y = [[0, 0]]
    return vezes, x, y


def FazFractal(vezes, x, y):
    for vez in range(vezes):
        x, y = faztriangulo(x, y)
        print("%d de %d" % (vez, vezes))
    listax, listay = [], []
    indice = 0
    limite = len(x)
    while indice < limite:
        listax.extend(x[indice])
        listay.extend(y[indice])
        indice += 1       
    return listax, listay


def FazFractalComTempo(Valores):
    vezes, x, y = VariaveisDeInput(Valores)
    inicio = time.time()
    listax, listay = FazFractal(vezes, x, y)
    print("Montando o Gráfico")
    plt.plot(listax, listay, color="black")
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, x, y = VariaveisDeInput(Valores)
    listax, listay = FazFractal(vezes, x, y)
    print("Montando o Gráfico")
    plt.plot(listax, listay, color="black")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, x, y = VariaveisDeInput(Valores)
    listax, listay = FazFractal(vezes, x, y)
    plt.plot(listax, listay, color="black")
    with PdfPages(r'triangulodesierpinklinear.pdf') as export_pdf:
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