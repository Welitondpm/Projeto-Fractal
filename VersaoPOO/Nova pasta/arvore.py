import matplotlib.pyplot as plt
import math
import random
from propriedade_por_quadrados import *


def barra():
    print(40 * "-")


def adicionaproximosangulos(angulo, theta):
    lista1, lista2 = [], []
    for item in angulo:
        lista1.append(item + theta)
        lista2.append(item - theta)
    return lista1 + lista2


def criaunicalista(x, y):
    listadescartavel = []
    listax, listadelistax = [], []
    listay, listadelistay = [], []
    maxtam = len(x[-1])
    for item in x:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        listadelistax.append(item)
    for item in y:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        listadelistay.append(item)
    for item in range(maxtam - 1):
        for subitem in range(len(x) - 1):
            listax.append(listadelistax[subitem][item])
            listay.append(listadelistay[subitem][item])
        plt.plot(listax, listay, color="black")
        listax, listay = [], []

    
def criaunicalistapropriedade(x, y):
    listadescartavel = []
    listax, listadelistax = [], []
    listay, listadelistay = [], []
    masterx = []
    mastery = []
    maxtam = len(x[-1])
    for item in x:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        listadelistax.append(item)
    for item in y:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        listadelistay.append(item)
    for item in range(maxtam - 1):
        for subitem in range(len(x) - 1):
            listax.append(listadelistax[subitem][item])
            listay.append(listadelistay[subitem][item])
        plt.plot(listax, listay, color="black")
        masterx.extend(listax[::])
        mastery.extend(listay[::])
        listax, listay = [], []
    return masterx, mastery


def imperfeiciona(x, imperfeicao):
    if type(x) == int or type(x) == float:
        return x * 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
    else:
        novox = []
        for item in x:
            if type(item) == int or type(item) == float:
                item *= 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
                novox.append(item)
            else:
                novoxlista = []
                for subitem in item:
                    subitem *= 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
                    novoxlista.append(subitem)
                novox.append(novoxlista)
        return novox


def fazarvore(x, y, ang, tamanho, z, w, wimp, zimp, theta):
    nang = []
    for item in ang:
        item *= imperfeiciona(w, wimp)
        nang.append(item)
    ang = nang
    novox, novoy = [], []
    tamanhoultimoindice = len(x[-1])
    indice = 0
    while indice < tamanhoultimoindice:
        novox.append(x[-1][indice] + tamanho * imperfeiciona(z, zimp) * math.sin(ang[2 * indice]))
        novox.append(x[-1][indice] + tamanho * imperfeiciona(z, zimp) * math.sin(ang[2 * indice + 1]))
        novoy.append(y[-1][indice] + tamanho * imperfeiciona(z, zimp) * math.cos(ang[2 * indice]))
        novoy.append(y[-1][indice] + tamanho * imperfeiciona(z, zimp) * math.cos(ang[2 * indice + 1]))
        indice += 1
    x.append(novox)
    y.append(novoy)
    angulo = adicionaproximosangulos(ang, theta)
    return x, y, angulo, tamanho


def FazPreCalculos(vezes, tamanho, theta, z, zimp, w, wimp):
    x, y = [[0], [0]], [[0], [tamanho]]
    theta = (theta * math.pi) / 180
    angulo = [theta, -theta]
    z = 1 - z / 100 + z / 50
    w = 1 - w / 100 + w / 50
    return vezes, tamanho, theta, z, zimp, w, wimp, angulo, x, y


def FazFractal(vezes, tamanho, theta, z, zimp, w, wimp):
    vezes, tamanho, theta, z, zimp, w, wimp, angulo, x, y = FazPreCalculos(vezes, tamanho, theta, z, zimp, w, wimp)
    for vez in range(vezes):
        x, y, angulo, tamanho = fazarvore(x, y, angulo, tamanho, z, w, wimp, zimp, theta)
        print("%d de %d" % (vez + 1, vezes))
    criaunicalista(x, y)
    print("Montando o Gráfico")


def PropriedadeQuadrado(vezes, tamanho, theta, z, zimp, w, wimp):
    vezes, tamanho, theta, z, zimp, w, wimp, angulo, x, y = FazPreCalculos(vezes, tamanho, theta, z, zimp, w, wimp)
    for vez in range(vezes):
        x, y, angulo, tamanho = fazarvore(x, y, angulo, tamanho, z, w, wimp, zimp, theta)
        print("%d de %d" % (vez + 1, vezes))
    masterx, mastery = criaunicalistapropriedade(x, y)
    FazCalculo(masterx, mastery)
    print("Montando o Gráfico")
    plt.show()


def Begin(vezes = 12, tamanho = 50, theta = 15, z = 0, zimp = 0, w = 0, wimp = 0):
    ExecutarPropriedade = bool(input("(False) Para não mostrar propriedades e (True) Para Mostrar: "))
    if ExecutarPropriedade:
        PropriedadeQuadrado(vezes, tamanho, theta, z, zimp, w, wimp)
    else:
        FazFractal(vezes, tamanho, theta, z, zimp, w, wimp)
        plt.show()


if __name__ == "__main__":
    Begin(12, 50, 15, 0, 0, 0, 0)