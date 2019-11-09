"""tirar aspa no fim"""

def atualiza(x,y,xizes,ipsulons):
    xizes.append(x)
    ipsulons.append(y)
def printtudo(xizes, ipsulons):
    print(xizes)
    print(ipsulons)

import math
vezes = int(input("Vezes: "))
contador = 0
tamanho = 1 # colocar input depois
x = []
y = []
angulo = 60
angulocerto = (angulo * (2 * math.pi)) / 360
adicaodex = tamanho * math.cos(angulocerto)
adicaodey = tamanho * math.sin(angulocerto)
xizes = []
ipsulons = []
while contador <= vezes:
    contador+=1
    atualiza(x, y, xizes, ipsulons)
   
printtudo(xizes, ipsulons)
