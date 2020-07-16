import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def ExecutaNesseArquivo():
    listax = []
    listay = []
    listaz = []
    vez = 0
    vezes = 100
    maxx, maxy, maxz = 100, 150, 50
    while vez < vezes:
        listax.append(random.random() * maxx)
        listay.append(random.random() * maxy)
        listaz.append(random.random() * maxz)
        vez += 1
    return listax, listay, listaz

def CriaAsVariaveisASeremUsadas(listax, listay, listaz):
    valor = int(input("Digite um valor inteiro, essa é a quantidade de quadrados,\n(Atenção o valor será elevado ao cubo!!):\n\n >>> "))
    duplox = listax[::]
    duploy = listay[::]
    duploz = listaz[::]
    novox = []
    novoy = []
    novoz = []
    minimox = min(listax)
    minimoy = min(listay)
    minimoz = min(listaz)
    maximox = max(listax)
    maximoy = max(listay)
    maximoz = max(listaz)
    passox = (maximox - minimox) / valor
    passoy = (maximoy - minimoy) / valor
    passoz = (maximoz - minimoz) / valor
    xquadrado = minimox + passox
    xanterior = minimox
    yquadrado = minimoy + passoy
    yanterior = minimoy
    zquadrado = minimoz + passoz
    zanterior = minimoz
    vezes = valor * valor * valor
    contador = 0
    return (duplox, duploy, duploz, novox, novoy, novoz, minimox, minimoz,
             maximox, maximoy, maximoz, passox, passoy, passoz, xquadrado, xanterior,
             yquadrado, yanterior, zquadrado, zanterior, vezes, contador)


def RemovePontosNasExtremidades(duplox, duploy, duploz, seila, xanterior, xquadrado, yanterior, yquadrado, zanterior, zquadrado):
    listasobrandox = duplox[seila::]
    listasobrandoy = duploy[seila::]
    listasobrandoz = duploz[seila::]
    respx = []
    respy = []
    respz = []
    contador = 0
    for item in listasobrandox:
        if item >= xanterior and item <= xquadrado:
            if listasobrandoy[contador] >= yanterior and listasobrandoy[contador] <= yquadrado:
                if listasobrandoz[contador] >= zanterior and listasobrandoz[contador] <= zquadrado:
                    pass
                else:
                    respx.append(item)
                    respy.append(listasobrandoy[contador])
                    respz.append(listasobrandoz[contador])
            else:
                respx.append(item)
                respy.append(listasobrandoy[contador])
                respz.append(listasobrandoz[contador])
        else:
            respx.append(item)
            respy.append(listasobrandoy[contador])
            respz.append(listasobrandoz[contador])
        contador += 1
    return respx, respy, respz


def FazCalculo(listax, listay, listaz):
    duplox, duploy, duploz, novox, novoy, novoz, minimox, minimoz, maximox, maximoy, maximoz, passox, passoy, passoz, xquadrado, xanterior, yquadrado, yanterior, zquadrado, zanterior, vezes, contador = CriaAsVariaveisASeremUsadas(listax, listay, listaz)
    while yanterior < maximoy:
        if xanterior >= maximox:
            xanterior = minimox
            xquadrado = xanterior + passox
            zanterior = zquadrado
            zquadrado = zanterior + passoz
        elif zanterior >= maximoz:
            xanterior = minimox
            xquadrado = xanterior + passox
            zanterior = minimoz
            zquadrado = zanterior + passoz
            yanterior = yquadrado
            yquadrado = yanterior + passoy
        else:
            seila = 0
            for item in duplox:
                if item >= xanterior and item <= xquadrado:
                    if duploz[seila] >= zanterior and duploz[seila] <= zquadrado:
                        if duploy[seila] >= yanterior and duploy[seila] <= yquadrado:   
                            plt.plot([xanterior, xanterior, xquadrado, xquadrado, xanterior, xanterior, xquadrado, xquadrado, xquadrado, xquadrado, xanterior, xanterior, xanterior, xanterior, xanterior, xquadrado, xquadrado], [yanterior, yanterior, yanterior, yanterior, yanterior, yquadrado, yquadrado, yanterior, yanterior, yquadrado, yquadrado, yanterior, yquadrado, yquadrado, yquadrado, yquadrado, yquadrado], [zanterior, zquadrado, zquadrado, zanterior, zanterior, zanterior, zanterior, zanterior, zquadrado, zquadrado, zquadrado, zquadrado, zquadrado, zanterior, zanterior, zanterior, zquadrado], color="#ff5300")
                            contador += 1
                            respx, respy, respz = RemovePontosNasExtremidades(duplox, duploy, duploz, seila, xanterior, xquadrado, yanterior, yquadrado, zanterior, zquadrado)
                            novox.extend(respx[::])
                            novoy.extend(respy[::])
                            novoz.extend(respz[::])
                            break
                        else:
                            novox.append(item)
                            novoy.append(duploy[seila])
                            novoz.append(duploz[seila])
                    else:
                        novox.append(item)
                        novoy.append(duploy[seila])
                        novoz.append(duploz[seila])
                else:
                    novox.append(item)
                    novoy.append(duploy[seila])
                    novoz.append(duploz[seila])
                seila += 1
            duplox = novox[::]
            duploy = novoy[::]
            duploz = novoz[::]
            novox.clear()
            novoy.clear()
            novoz.clear()
            xanterior = xquadrado
            xquadrado = xanterior + passox
    print("Quantidade de Quadrados: ", vezes)
    print("Quadrados Pintados: ", contador)


if __name__ == "__main__":
    fig = plt.figure()
    sub = fig.add_subplot(1, 1, 1, projection='3d')
    listax, listay, listaz = ExecutaNesseArquivo()
    FazCalculo(listax, listay, listaz)
    sub.scatter(listax, listay, listaz)
    plt.show()