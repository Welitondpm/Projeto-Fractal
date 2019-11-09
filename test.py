import matplotlib.pyplot as plt


def apeendlista(lista, b):
    listapradevolver = []
    a = 1
    for item in lista:
        listapradevolver.append(item)
    for posiçao in range(b):
        for item in lista:
            listapradevolver.append(item + a)
        a += 1
    return listapradevolver


lista = [0, 5, 10]
b = int(input("DIgite a porra da quantidade de vezes: "))
x = apeendlista(lista, b)
y = []
a = 0
for item in x:
    a += 1
    y.append(a)
plt.plot(x, y)
plt.scatter(x, y)
plt.show()