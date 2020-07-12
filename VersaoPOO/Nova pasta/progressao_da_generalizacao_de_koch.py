import matplotlib.pyplot as plt
import math


def fazcalculo(x, y, lados):
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
        novox = [x[indice] + differencex / 3]
        novoy = [y[indice] + differencey / 3]
        contadorwhile = 0
        while contadorwhile < lados - 2:
            novox += [novox[-1] + (distanciaxy / 3) * math.cos(angdado + ang)]
            novoy += [novoy[-1] + (distanciaxy / 3) * math.sin(angdado + ang)]
            ang -= (math.pi - angulobackup)
            contadorwhile += 1
        ang = angulobackup
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


def FazFractal(vezes, lados, tamanho):
    x = [0, tamanho]
    y = [0, 0]
    for fractallados in range(3, lados + 1):
        fractallados = lados + 1 - fractallados
        print("Está fazendo o fractal do maior até o 3: ", fractallados)
        x, y = monta(x, y, vezes, fractallados)
        plt.plot(x, y)
        x = [0, tamanho]
        y = [0, 0]
    

if __name__ == "__main__":
    FazFractal(5, 7, 10)
    print("Montando Gráfico")
    plt.show()