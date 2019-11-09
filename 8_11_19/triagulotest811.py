import matplotlib.pyplot as plt


t = 100
x = [-t / 2, 0, t / 2]
y = [-t * 3 ** 0.5 / 2, 0, -t * 3 ** 0.5 / 2]
vez = 0
vezes = 3
xant = x[::]
yant = y[::]
ultimo = len(x)
while vez < vezes:
    vez+=1
    for item in xant:
        for item2 in xant:
            media = (item + item2) / 2
            x.append(media)
    for item in yant:
        for item2 in yant:
            media = (item + item2) / 2
            y.append(media)
    xant = x[::]
    yant = y[::]

plt.scatter(x, y)
plt.show()