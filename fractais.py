import matplotlib.pyplot as plt

import math
x=[0]
y=[0]
t=100
indice=0
vez=0
def triangulo_de_sierpinski(x,y,vez,t,indice):
    vez+=1
    for i in range(len(x)):
        x.append(x[indice+i]+t/2)
        x.append(x[indice+i]-t/2)
    for i in range(len(y)):
        y.append(y[indice+i]-t*((3/4)**0.5))
        y.append(y[-1])
    t=t/2
    indice=3**vez
    if vez < vezes:
        triangulo_de_sierpinski(x,y,vez,t,indice)
    plt.scatter(x, y)
    plt.show()


triangulo_de_sierpinski(x,y,vez,t,indice)