import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages
# import time


vezes = int(input("Digite a quantidade de vezes ( <= 12): "))
# inicio = time.time()
x = [[0, 1]]
y = [[0, 0]]


def fazfractal(xrecebido, yrecebido):
    xdevolver, ydevolver = [], []
    for item in range(len(xrecebido)):
        x = xrecebido[item]
        y = yrecebido[item]
        if y[1] - y[0] == 0:
            x1 = x[0]
            x2 = x[0]+(x[1] - x[0]) / 4
            x3 = x[0]+(x[1] - x[0]) * 3 / 4
            x4 = x[1]
            y1 = y[0]
            y2 = y[0] + abs(x[1] - x[0]) / 4
            y3 = y2
            y4 = y[1]
        elif x[1] - x[0] == 0:
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 3
            y3 = y[0] + (y[1] - y[0]) * 2 / 3
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] + (y[1] - y[0]) / 3
            x3 = x2
            x4 = x[1]
        elif x[1] > x[0] and y[1] > y[0]:  # /^
            y1 = y[0]
            y2 = y1
            y3 = y[0] + (y[1] - y[0]) / 2
            y4 = y[1]
            x1 = x[0]
            x2 = x[1]
            x3 = x2 + (y[1] - y[0]) / 2
            x4 = x2
        elif x[1] < x[0] and y[1] > y[0]:  # ^\
            y1 = y[0]
            y2 = y1
            y3 = y[0] + (y[1] - y[0]) / 2
            y4 = y[1]
            x1 = x[0]
            x2 = x[1]
            x3 = x2 - (y[1] - y[0]) / 2
            x4 = x2
        elif x[1] < x[0] and y[1] < y[0]:  # _/
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 2
            y3 = y[1]
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] - (y[1] - y[0]) / 2
            x3 = x1
            x4 = x[1]
        elif x[1] > x[0] and y[1] < y[0]:  # \_
            y1 = y[0]
            y2 = y[0] + (y[1] - y[0]) / 2
            y3 = y[1]
            y4 = y[1]
            x1 = x[0]
            x2 = x[0] + (y[1] - y[0]) / 2
            x3 = x1
            x4 = x[1]
        xdevolver += [[x1, x2], [x2, x3], [x3, x4]]
        ydevolver += [[y1, y2], [y2, y3], [y3, y4]]
    return xdevolver, ydevolver


for vez in range(vezes):
    x, y = fazfractal(x, y)
    print("%d de %d" % (vez, vezes))

listax, listay = [], []

for item in x:
    for subitem in item:
        listax.append(subitem)

for item in y:
    for subitem in item:
        listay.append(subitem)


print("Montando o Gráfico")
# with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\triangulodesierpinskilinearpasso3.pdf') as export_pdf:
plt.plot(listax, listay, color="black")
    # export_pdf.savefig()
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()
