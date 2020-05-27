import matplotlib.pyplot as plt


def CriaAsVariaveisASeremUsadas(listax, listay, valor):
    # valor = int(input("Digite um valor inteiro, essa é a quantidade de quadrados,\n(Atenção o valor será elevado ao quadrado!!):\n\n >>> "))
    duplox = listax[::]
    duploy = listay[::]
    novox = []
    novoy = []
    minimox = min(listax)
    minimoy = min(listay)
    maximox = max(listax)
    maximoy = max(listay)
    passox = (maximox - minimox) / valor
    passoy = (maximoy - minimoy) / valor
    xquadrado = minimox + passox
    xanterior = minimox
    yquadrado = minimoy + passoy
    yanterior = minimoy
    vezes = valor * valor
    contador = 0
    return duplox, duploy, novox, novoy, minimox, maximox, maximoy, passox, passoy, xquadrado, xanterior, yquadrado, yanterior, vezes, contador


def RemovePontosNasExtremidades(duplox, duploy, seila, xanterior, xquadrado, yanterior, yquadrado):
    listasobrandox = duplox[seila::]
    listasobrandoy = duploy[seila::]
    respx = []
    respy = []
    contador = 0
    for item in listasobrandox:
        if item >= xanterior and item <= xquadrado:
            if listasobrandoy[contador] >= yanterior and listasobrandoy[contador] <= yquadrado:
                pass
            else:
                respx.append(item)
                respy.append(listasobrandoy[contador])
        else:
            respx.append(item)
            respy.append(listasobrandoy[contador])
        contador += 1
    return respx, respy


def progressaoFazCalculo(listax, listay, valor):
    duplox, duploy, novox, novoy, minimox, maximox, maximoy, passox, passoy, xquadrado, xanterior, yquadrado, yanterior, vezes, contador = CriaAsVariaveisASeremUsadas(listax, listay, valor)
    while yanterior < maximoy:
        if xanterior >= maximox:
            xanterior = minimox
            xquadrado = xanterior + passox
            yanterior = yquadrado
            yquadrado = yanterior + passoy
        else:
            seila = 0
            for item in duplox:
                if item >= xanterior and item <= xquadrado:
                    if duploy[seila] >= yanterior and duploy[seila] <= yquadrado:
                        contador += 1
                        respx, respy = RemovePontosNasExtremidades(duplox, duploy, seila, xanterior, xquadrado, yanterior, yquadrado)
                        novox.extend(respx[::])
                        novoy.extend(respy[::])
                        break
                    else:
                        novox.append(item)
                        novoy.append(duploy[seila])
                else:
                    novox.append(item)
                    novoy.append(duploy[seila])
                seila += 1
            duplox = novox[::]
            duploy = novoy[::]
            novox.clear()
            novoy.clear()
            xanterior = xquadrado
            xquadrado = xanterior + passox
    return contador


if __name__ == "__main__":
    print("Esse documento não pode ser executado sozinho")