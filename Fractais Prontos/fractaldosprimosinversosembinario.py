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


xs = []
ys = []
fim = int(input("Fim: "))
for item in range(fim):
    y = 0
    if é_primo(item): 
        bina = binario(item)
        deci = decimal(bina)
        y = item - deci
    xs.append(item)
    ys.append(y)
plt.scatter(xs, ys)
plt.show()