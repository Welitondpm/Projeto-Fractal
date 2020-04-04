import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages
# import time


def é_primo(valor):
    for item in range(2, valor):
        if valor % item == 0:
            return False
    return True


def binario(valor):
    lista = []
    while valor >= 2:
        resto = valor % 2
        valor //= 2
        lista.append(resto)
    if valor == 1:
        lista.append(valor)
    lista.reverse()
    return lista


def decimal(lista):
    a = 0
    soma = 0
    for item in lista:
        soma += (item * (2 ** a))
        a += 1
    return soma


def fazfractal(fim, contagem):
    xs = []
    ys = []
    if contagem:
        for item in range(fim):
            print("%d de %d" % (item, fim))
            y = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                y = item - deci
            xs.append(item)
            ys.append(y)
    else:
        for item in range(fim):
            y = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                y = item - deci
            xs.append(item)
            ys.append(y)
    return xs, ys


fim = int(input("Fim (recomendado <= 262144): "))
contagem = bool(input("Deseja ver o valor atual? (True/False): "))
# inicio = time.time()
xs, ys = fazfractal(fim, contagem)


print("Montando o Gráfico")
# with PdfPages(r'E:\Projeto_Fractal\img_dos_fractais_prontos\binarioinvertidopasso0(16384).pdf') as export_pdf:
plt.scatter(xs, ys, color="black", s=0.01)
    # export_pdf.savefig()
# plt.axis([0, 45000, -45000, 45000])
# fim = time.time()
# print(str(round(fim-inicio, 5)) + "s")
plt.show()