import matplotlib.pyplot as plt


profundidade = 1000
reais = 3
imaginarios = 3
densidade = 5
cores = 's'


lim = profundidade
lim1 = lim
l, l1 = [], []
uni1 = range(int(-reais * densidade), int(reais * densidade))
uni2 = range(int(-imaginarios * densidade), int(imaginarios * densidade))
s = 1000 / densidade
lx, ly = [], []

for n in uni1:
    porc = round(50 + 100 * (n) / (len(uni1)), 2)
    print(porc, '%')
    n /= densidade
    for m in uni2:
        m /= densidade
        z = complex(0, 0)
        c = complex(n, m)
        for contador in range(profundidade):
            z = z * z + c
            if abs(z) > lim1:
                if cores:
                    cor = int(2 ** 24 * contador // profundidade)
                    cor = (str(hex(cor))[2:])
                    while len(cor) < 6:
                        cor = '0' + cor
                    cor = "#" + cor
                    plt.scatter([n], [m], color=cor, s=s, marker='s')
            else:
                l.append(n)
                l1.append(m)


print("\n\nMontando o Gráfico\n\n")
plt.show()