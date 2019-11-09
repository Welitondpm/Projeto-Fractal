# import matplotlib.pyplot as plt
# from math import sqrt

t = 100
x = [0, -t / 2, t / 2]
y = [0, -t * 3 ** 0.5 / 2, -t * 3 ** 0.5 / 2]
vez = 0
vezes = 3
xant = [0, -t / 2, t / 2]
yant = [0, -t * 3 ** 0.5 / 2, -t * 3 ** 0.5 / 2]
while vez < vezes:
    vez += 1
    for l in xant:
        for n in xant:
            print(len(xant)) # Usado pra verificar o loop
            x.append((l + n) / 2)
    for l in yant:
        for n in yant:
            y.append((l + n) / 2)
    xant = x
    yant = y
# plt.scatter(x, y)
# plt.show()