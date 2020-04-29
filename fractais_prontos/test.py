import matplotlib.pyplot as plt
from random import randint

listax = []
listay = []
vez = 0
vezes = 1
while vez <= vezes:
    listax.append(randint(0, 100))
    listay.append(randint(0, 100))
    vez += 1

minimox = min(listax)
maximox = max(listax)
minimoy = min(listay)
maximoy = max(listay)
valor = 2
tamanhodey = maximoy - minimoy
tamanhodex = maximox - minimox
passox = tamanhodex / valor
passoy = tamanhodey / valor
vezes = (valor + 1) * (valor + 1)
vezes2 = valor * valor
vez = 0
xquadrado = minimox
yquadrado = minimoy 
yanterior = minimoy - passoy
xanterior = minimox - passox
novox = []
novoy = []
contador = 0
contadordequadrados = 0
while yanterior < (maximoy + passoy):
    if xquadrado > (maximox + passox):
        xquadrado = minimox 
        xanterior = minimox - passox
        yanterior = yquadrado
        yquadrado += passoy
        contadordequadrados += 1
    else:
        seila = 0
        seila2 = 0
        if seila == 1:
            if  listax[0] == minimox and listay[0] == minimoy:
                novox.append(listax[seila])
                novoy.append(listay[seila])
                plt.fill([xanterior, xquadrado, xquadrado, xanterior], [yanterior, yanterior, yquadrado, yquadrado])
                contador += 1
        else:
            for item in listax:
                if item <= xquadrado and item > xanterior:
                    if listay[seila] <= yquadrado and listay[seila] > yanterior:
                        novox.append(item)
                        novoy.append(listay[seila])
                        plt.fill([xanterior, xanterior, xquadrado, xquadrado], [yanterior, yquadrado, yanterior, yquadrado])
                        contador += 1
                        seila2 = 1
                seila += 1
                if seila2 == 1:
                    break
        xanterior = xquadrado
        xquadrado += passox
        contadordequadrados += 1



plt.scatter(listax, listay)
print("Quantidade de Quadrados(vezes): ", vezes)
print("Quantidade de Quadrados(vezes2): ", vezes2)
print("Quantidade de Quadrados(contador): ", contadordequadrados)
print("Quadrados Preenchidos: ", contador)
plt.show()