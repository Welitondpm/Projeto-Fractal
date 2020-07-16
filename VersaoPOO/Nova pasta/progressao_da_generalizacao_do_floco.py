import matplotlib.pyplot as plt
import math


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
        if vez == 1:
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
        if vez == 1:
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


def monta(x, y, vezes, lados, mudar):
    for vez in range(1, vezes + 1):
        print(vez, " de ", vezes)
        x, y = fazcalculo(x, y, lados, vez, mudar)
    return x, y


def FazFractal(vezes, lados, tamanho, mudar, estilo):
    desce = 0
    x = [0, tamanho]
    y = [desce, desce]
    for fractallados in range(3, lados + 1):
        fractallados = lados + 3 - fractallados
        print("Está fazendo o fractal do maior até o 3: ", fractallados)
        if estilo == "1":
            desce = - (tamanho / 2) / math.tan ((math.pi / fractallados))
            x = [0, tamanho]
            y = [desce, desce]
            x, y = monta(x, y, vezes, fractallados, mudar)
            plt.fill(x, y)
        elif estilo == "2":
            desce = (tamanho / 2) / math.tan ((math.pi / fractallados))
            x = [0, tamanho]
            y = [desce, desce]
            x, y = monta(x, y, vezes, fractallados, mudar)
            plt.fill(x, y)
        else:
            x, y = monta(x, y, vezes, fractallados, mudar)
            plt.fill(x, y)
            x = [0, tamanho]
            y = [0, 0]


if __name__ == "__main__":
    FazFractal(5, 6, 10, "n", 1)
    print("Montando Gráfico")
    plt.show()