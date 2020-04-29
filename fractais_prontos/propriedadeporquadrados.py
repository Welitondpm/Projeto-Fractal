import matplotlib.pyplot as plt
from random import randint

listax = []
listay = []
vez = 0
vezes = 2
while vez <= vezes:
    listax.append(randint(0, 100))
    listay.append(randint(0, 100))
    vez += 1

valor = 10
duplox = listax[::]
duploy = listay[::]
novox = []
novoy = []
minimox = min(listax)
minimoy = min(listay)
maximox = max(listax)
maximoy = max(listay)
tamanhodex = maximox - minimox
tamanhodey = maximoy - minimoy
passox = tamanhodex / valor
passoy = tamanhodey / valor
xquadrado = minimox + passox
xanterior = minimox
yquadrado = minimoy + passoy
yanterior = minimoy
vezes = valor * valor
contador = 0
while yanterior < maximoy:
    if xanterior >= maximox:
        xanterior = minimox
        xquadrado = xanterior + passox
        yanterior = yquadrado
        yquadrado = yanterior + passoy
    else:
        seila = 0
        for item in duplox:
            if item >= xanterior and item <= xquadrado:
                if duploy[seila] >= yanterior and duploy[seila] <= yquadrado:
                    plt.fill([xanterior, xanterior, xquadrado, xquadrado], [yanterior, yquadrado, yquadrado, yanterior])
                    contador += 1
                    novox.extend(duplox[seila::])
                    novoy.extend(duploy[seila::])
                    break
                else:
                    novox.append(item)
                    novoy.append(duploy[seila])
            else:
                novox.append(item)
                novoy.append(duploy[seila])
            seila += 1
        duplox = novox[::]
        duploy = novoy[::]
        novox.clear()
        novoy.clear()
        xanterior = xquadrado
        xquadrado = xanterior + passox


print("Quadrados Pintados: ", contador)
print("Quantidade de Quadrados: ", vezes)
plt.scatter(listax, listay)
plt.show()