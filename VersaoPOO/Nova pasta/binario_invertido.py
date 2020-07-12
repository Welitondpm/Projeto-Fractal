import matplotlib.pyplot as plt


def é_primo(valor):
    for item in range(2, int(valor ** 0.5) + 1):
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


def decimal(valor):
    indice = 0
    soma = 0
    for item in valor:
        soma += (item * (2 ** indice))
        indice += 1
    return soma


def fazbinario(fim, contagem):
    x, y = [], []
    if contagem:
        for item in range(fim):
            print("%d de %d" % (item, fim))
            ycalculado = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                ycalculado = item - deci
            x.append(item)
            y.append(ycalculado)
    else:
        for item in range(fim):
            ycalculado = 0
            if é_primo(item): 
                bina = binario(item)
                deci = decimal(bina)
                ycalculado = item - deci
            x.append(item)
            y.append(ycalculado)
    return x, y


if __name__ == "__main__":
    x, y = fazbinario(262144, False)
    print("Montando o Gráfico")
    plt.scatter(x, y, color="black", s=0.01)
    plt.show()