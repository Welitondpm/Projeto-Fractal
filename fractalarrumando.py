import matplotlib.pyplot as plt
from math import sqrt

def calculalista(xant, yant):
    x = []
    y = []
    for item in xant:
        for item1 in xant:
            x.append((item + item1) / 2)
    for item in yant:
        for item1 in yant:
            y.append((item + item1) / 2)
    return x, y


x = [0, -50, 50]
y = [0, -86.60254037844386, -86.60254037844386]
xant = [0, -50, 50]
yant = [0, -86.60254037844386, -86.60254037844386]
vez = 0
vezes = 4
while vez < vezes:
    vez += 1
    x2, y2 = calculalista(xant, yant)
    for item in x2:
        xant.append(item)
    for item in y2:
        yant.append(item)
plt.scatter(x, y)
plt.show()
