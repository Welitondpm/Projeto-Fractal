def fazPascalposicao(vezes):
    lista = [0, 1, 0]
    if vezes == 1:
        return lista
    vez = 0
    x = []
    while vez < vezes:
        vez += 1
        anterior = lista[0]
        for item in lista:
            x.append(item + anterior)
            anterior = item
        x.append(anterior + anterior)
        lista.clear()
        for item in x:
            lista.append(item)
        x.clear()
    return lista


def fazespasamentonos(x, xstr):
    for item in x:
        item1 = str(item)
        if item % 2 == 0:
            item1 = "     "
        else:
            if len(item1) == 1:
                item1 = "   " + item1
            elif len(item1) == 2:
                item1 = "   " + item1
            elif len(item1) == 3:
                item1 = "  " + item1
            elif len(item1) == 4:
                item1 = " " + item1
        xstr += item1
    return xstr


def triangulostr(vezes):
    vez = 0
    xstr = ""
    while vez < vezes:
        vez += 1
        x = fazPascalposicao(vez)
        x = x[1:-1]
        xstr = fazespasamentonos(x, xstr)
        print(xstr.center(175))
        xstr = ""


if __name__ == "__main__":
    triangulostr(20)