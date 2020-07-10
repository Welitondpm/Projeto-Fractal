import matplotlib.pyplot as plt
from propriedade_por_quadrados import *


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


def FazFractal(vezes, escalonar):
    x, y = fazdragao(vezes, escalonar)
    return x, y


def PropriedadeQuadrado(vezes, escalonar):
    x, y = FazFractal(vezes, escalonar)
    FazCalculo(x, y)
    print("Montando o Gráfico")
    plt.plot(x, y, color="black")
    plt.show()


def Begin(vezes = 20, escalonar = False):
    ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
    if ExecutarPropriedade:
        PropriedadeQuadrado(vezes, escalonar)
    else:
        x, y = FazFractal(vezes, escalonar)
        print("Montando o Gráfico")
        plt.plot(x, y, color="black")
        plt.show()
        

if __name__ == "__main__":
    Begin(20, False)