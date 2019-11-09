import matplotlib.pyplot as plt


def funcaopramediadetodoscomtodos(x, y):
    x2 = x[::]
    y2 = y[::]
    for item in x:
        contador = 0
        limite = len(x)
        a = 0
        b = []
        while contador < limite:
            if item == x[contador]:
                a += 1
                b.append(contador)
            contador += 1
        if len(b) >= 2:
            del b[0]
            for item2 in b:
                del x2[item2]
                del y2[item2]
                x2.append(0)
                y2.append(0)
    return x2, y2


def calculamedia(x):
    xant = x[::]
    xant1 = []
    for i, item in enumerate(xant):
        if i > 0:
            xant1.append((item + xant[i - 1]) / 2)
        xant1.append(item)
    return xant1


def todoscomtodos(x, vezes):
    vez = 0
    xant = []
    comeco = 0
    while vez < vezes:
        vez += 1
        for i in x:
            for j in x:
                xant.append((i + j) / 2)
            comeco += 1
        x = xant[::]
    return x


t = 100
x = [0, -t / 2, t / 2, 0]
y = [0, -t * 3 ** 0.5 / 2, -t * 3 ** 0.5 / 2, 0]
vezes = int(input("Digite quantas Vezes: "))
# while vez <= vezes:
#     vez += 1
#     x = calculamedia(x)
#     y = calculamedia(y)
x = todoscomtodos(x, vezes)
y = todoscomtodos(y, vezes)
x2, y2 = funcaopramediadetodoscomtodos(x , y)


print("Está Montado o gráfico")
plt.scatter(x2, y2)
plt.show()