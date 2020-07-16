import matplotlib.pyplot as plt
import math


def fazcalculo(x, y, lados):
    somadosangint = 180 * (lados - 2)
    ang = somadosangint / lados * math.pi / 180
    angulobackup = ang
    novoxfinal, novoyfinal = [], []
    for indice in range(len(x) - 1):
        diferrencex = x[indice + 1] - x[indice]
        diferrencey = y[indice + 1] - y[indice]
        distanciaxy = (diferrencex ** 2 + diferrencey ** 2) ** 0.5
        if diferrencex < 0:
            distanciaxy *= -1
        if diferrencex != 0:
            angdado = math.atan(diferrencey / diferrencex)
        elif diferrencey > 0:
            angdado = math.pi / 2
        elif diferrencey < 0:
            angdado = 3 * math.pi / 2
        else:
            continue
        novox = [x[indice] + diferrencex / 3]
        novoy = [y[indice] + diferrencey / 3]
        vez = 0
        while vez < lados - 2:
            novox += [novox[-1] + (distanciaxy / 3) * math.cos(angdado + ang)]
            novoy += [novoy[-1] + (distanciaxy / 3) * math.sin(angdado + ang)]
            ang -= (math.pi - angulobackup)
            vez += 1
        ang = angulobackup
        novox += [x[indice] + 2 * diferrencex / 3]
        novoy += [y[indice] + 2 * diferrencey / 3]
        novox = [x[indice]] + novox + [x[indice + 1]]
        novoy = [y[indice]] + novoy + [y[indice + 1]]
        novoxfinal += novox
        novoyfinal += novoy
    return novoxfinal, novoyfinal


def FazFractal(vezes, lados, tamanho):
    x = [0, tamanho]
    y = [0, 0]
    for vez in range(vezes):
        print(vez + 1, " de ", vezes)
        x, y = fazcalculo(x, y, lados)
    return x, y


if __name__ == "__main__":
    x, y = FazFractal(5, 4, 10)
    print("Montando Gráfico")
    plt.plot(x, y)
    plt.show()