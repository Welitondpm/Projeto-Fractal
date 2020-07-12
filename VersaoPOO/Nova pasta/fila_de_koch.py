import matplotlib.pyplot as plt
import math


def fazcalculo(x, y, lados):
    somadosanguloint = 180 * (lados - 2)
    angulo = somadosanguloint / lados * math.pi / 180
    angulobackup = angulo
    novoxfinal, novoyfinal = [], []
    for indice in range(len(x) - 1):
        differencex = x[indice + 1] - x[indice]
        differencey = y[indice + 1] - y[indice]
        distanciaxy = (differencex ** 2 + differencey ** 2) ** 0.5
        if differencex < 0:
            distanciaxy *= -1
        if differencex != 0:
            angulodado = math.atan(differencey / differencex)
        elif differencey > 0:
            angulodado = math.pi / 2
        elif differencey < 0:
            angulodado = 3 * math.pi / 2
        else:
            continue
        novox = [x[indice] + differencex / 3]
        novoy = [y[indice] + differencey / 3]
        contadorwhile = 0
        while contadorwhile < lados - 2:
            novox += [novox[-1] + (distanciaxy / 3) * math.cos(angulodado + angulo)]
            novoy += [novoy[-1] + (distanciaxy / 3) * math.sin(angulodado + angulo)]
            angulo -= (math.pi - angulobackup)
            contadorwhile += 1
        angulo = angulobackup
        novox += [x[indice] + 2 * differencex / 3]
        novoy += [y[indice] + 2 * differencey / 3]
        novox = [x[indice]] + novox + [x[indice + 1]]
        novoy = [y[indice]] + novoy + [y[indice + 1]]
        novoxfinal += novox
        novoyfinal += novoy
    return novoxfinal, novoyfinal


def monta(x, y, vezes, lados):
    for vez in range(1, vezes + 1):
        print(vez, " de ", vezes)
        x, y = fazcalculo(x, y, lados)
    return x, y


if __name__ == "__main__":
    for fractallados in range(3, 7 + 1):
        x = [10 * fractallados, 10 * (fractallados + 1)]
        y = [0, 0]
        fractallados = 7 + 3 - fractallados
        print("\n", fractallados, ' lados de ', 7)
        x, y = monta(x, y, 5, fractallados)
        plt.plot(x, y)

    print("Montando Gráfico")
    plt.show()