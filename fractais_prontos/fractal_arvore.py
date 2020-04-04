import matplotlib.pyplot as plt
import math
import random
# from matplotlib.backends.backend_pdf import PdfPages
# import time


def barra():
    print(40 * "-")


def adicionaproximosangulos(angulo):
    lista1, lista2 = [], []
    global theta
    for item in angulo:
        lista1.append(item + theta)
        lista2.append(item - theta)
    return lista1 + lista2


def criaunicalista(x, y):
    listadescartavel = []
    lx, l1x = [], []
    ly, l1y = [], []
    maxtam = len(x[-1])
    for item in x:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        l1x.append(item)
    for item in y:
        while len(item) < maxtam:
            for subitem in item:
                listadescartavel.append(subitem)
                listadescartavel.append(subitem)
            item = listadescartavel
            listadescartavel = []
        l1y.append(item)
    for item in range(maxtam - 1):
        for subitem in range(len(x) - 1):
            lx.append(l1x[subitem][item])
            ly.append(l1y[subitem][item])
        plt.plot(lx, ly, color="black")
        lx, ly = [], []


def imperfeiciona(x, imperfeicao):
    if type(x) == int or type(x) == float:
        return x * 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
    else:
        nx = []
        for i in x:
            if type(i) == int or type(i) == float:
                i *= 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
                nx.append(i)
            else:
                ni = []
                for j in i:
                    j *= 1 - imperfeicao / 200 + (random.random() * imperfeicao) / 100
                    ni.append(j)
                nx.append(ni)
        return nx


def fazarvore(x, y, ang, tamanho, z, w):
    nang = []
    for item in ang:
        item *= imperfeiciona(w, wimp)
        nang.append(item)
    ang = nang
    novox, novoy = [], []
    for item in range(len(x[-1])):
        novox.append(x[-1][item] + tamanho * imperfeiciona(z, zimp) * math.sin(ang[2 * item]))
        novox.append(x[-1][item] + tamanho * imperfeiciona(z, zimp) * math.sin(ang[2 * item + 1]))
    for item in range(len(y[-1])):
        novoy.append(y[-1][item] + tamanho * imperfeiciona(z, zimp) * math.cos(ang[2 * item]))
        novoy.append(y[-1][item] + tamanho * imperfeiciona(z, zimp) * math.cos(ang[2 * item + 1]))
    x.append(novox)
    y.append(novoy)
    angulo = adicionaproximosangulos(ang)
    return x, y, angulo, tamanho

vezes = int(input("Número de iterações(Recomendado <= 13): "))
barra()

tamanho = int(input("Digite o tamanho: "))
barra()

x, y = [[0], [0]], [[0], [tamanho]]

theta =float(input("Ângulo(em graus): "))
theta = (theta * math.pi) / 180
barra()
angulo = [theta, -theta]

z = float(input("Mudança no tamanho por iteração(% para + ou para -): "))
z = 1 - z / 100 + z / 50
zimp = float(input("Randomizar aspecto em quanto?: "))
barra()

w = float(input("Mudança no ângulo por iteração(% para + ou para -): "))
w = 1 - w / 100 + w / 50
wimp = float(input("Randomizar aspecto em quanto?: "))
barra()

# inicio = time.time()

for vez in range(vezes):
    x, y, angulo, tamanho = fazarvore(x, y, angulo, tamanho, z, w)
    print("%d de %d" % (vez + 1, vezes))

criaunicalista(x, y)


print("Montando o Gráfico")
# with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\arvorepasso3.pdf') as export_pdf:
#     export_pdf.savefig()
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()