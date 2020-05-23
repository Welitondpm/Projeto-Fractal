import matplotlib.pyplot as plt
import math
import random
from matplotlib.backends.backend_pdf import PdfPages
import time
from propriedadeporquadrados import *


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


def VariaveisDeInput(Valores):
    if Valores:
        vezes, tamanho, theta, z, zimp, w, wimp = 12, 50, 15, 0, 0, 0, 0
    else:
        vezes = int(input("Número de iterações(Recomendado <= 13): "))
        barra()
        tamanho = int(input("Digite o tamanho: "))
        barra()
        theta = float(input("Ângulo(em graus): "))
        barra()
        z = float(input("Mudança no tamanho por iteração(% para + ou para -): "))
        zimp = float(input("Randomizar aspecto em quanto?: "))
        barra()
        w = float(input("Mudança no ângulo por iteração(% para + ou para -): "))
        wimp = float(input("Randomizar aspecto em quanto?: "))
        barra()
    return vezes, tamanho, theta, z, zimp, w, wimp


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


def FazFractalComTempo(Valores):
    vezes, tamanho, theta, z, zimp, w, wimp = VariaveisDeInput(Valores)
    inicio = time.time()
    FazFractal(vezes, tamanho, theta, z, zimp, w, wimp)
    fim = time.time()
    print(str(round(fim - inicio, 5)) + "s")
    plt.show()


def FazFractalSemTempo(Valores):
    vezes, tamanho, theta, z, zimp, w, wimp = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho, theta, z, zimp, w, wimp)
    plt.show()


def PropriedadeQuadrado(Valores):
    vezes, tamanho, theta, z, zimp, w, wimp = VariaveisDeInput(Valores)
    vezes, tamanho, theta, z, zimp, w, wimp, angulo, x, y = FazPreCalculos(vezes, tamanho, theta, z, zimp, w, wimp)
    for vez in range(vezes):
        x, y, angulo, tamanho = fazarvore(x, y, angulo, tamanho, z, w, wimp, zimp, theta)
        print("%d de %d" % (vez + 1, vezes))
    masterx, mastery = criaunicalistapropriedade(x, y)
    FazCalculo(masterx, mastery)
    print("Montando o Gráfico")
    plt.show()


def SalvarEmPDF(Valores):
    vezes, tamanho, theta, z, zimp, w, wimp = VariaveisDeInput(Valores)
    FazFractal(vezes, tamanho, theta, z, zimp, w, wimp)
    with PdfPages(r'arvore.pdf') as export_pdf:
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