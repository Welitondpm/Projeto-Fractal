import math
vezes = int(input("Vezes: "))
contador = 0
h = 1 # colocar input depois
x = []
y = 0
angulo = 60
angulocerto = (angulo * (2 * math.pi)) / 360
adicaodex = h * math.cos(angulocerto)
xizes = []
ipsulons = []
while contador <= vezes:
    contador += 1
    y = h
    xizes.append(x)
    ipsulons.append(y)
    yanterior = y
    xanterior = x
    x.append(adicaodex)
    adicaodex *= -1
    x.append(adicaodex)
    angulocerto*=2
    for i in range(vezes):
        adicaodex=h*math.cos(90-angulocerto)
    print(xizes)
    print(ipsulons)