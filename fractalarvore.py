import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

vezes = int(input("Digite quantas vezes: "))
tamanho = int(input("Digite o tamanho: "))
anguloinserido = int(input("Digite o angulo: "))
angulousado = (anguloinserido * math.pi) / 180
limite = 0
x = []
y = 0
xises = []
ipsulons = []
adicaodex = tamanho * math.cos(angulousado)
while limite <= vezes:
	limite += 1
	y = tamanho
	for item in x:
		xises.append(item)
	ipsulons.append(y)
	xanterior = x
	yanterior = y
	x.append(adicaodex)
	x.append(adicaodex * -1)
	angulousado *= 2
	for item in range(vezes):
		adicaodex = tamanho * math.cos(90 - angulousado)
plt.scatter(xises, ipsulons)
plt.show()
