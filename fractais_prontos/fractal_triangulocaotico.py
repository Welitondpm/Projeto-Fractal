import matplotlib.pyplot as plt
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
# import time


def fazfractal(vezes, valor):
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


vezes = int(input("Digite a Quantidade de vezes(recomendado 100000 <= x <= 1000000): "))
valor = float(input("Valor(triangulo de sierpinski coloque 2): "))
# inicio = time.time()
x, y = fazfractal(vezes, valor)

print("Montando o gráfico")
with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\triangulocaotico(vezes100000).pdf') as export_pdf:
    plt.scatter(x, y, color="black", s=0.01)
    export_pdf.savefig()
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()