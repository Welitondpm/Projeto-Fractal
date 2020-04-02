import matplotlib.pyplot as plt


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
xs, ys = fazfractal(fim, contagem)


print("Montando o Gráfico")
plt.scatter(xs, ys, color="black", s=0.01)
# plt.axis([0, 45000, -45000, 45000])
plt.show()