import matplotlib.pyplot as plt
import cmath


#ESSE É ARITMETICO
profundidade = 1000
reais = 2
imaginarios = 2
densidade = 100
cores = True


lim = 10
lim1 = lim
lim2 = 1 / lim
a, a1, b, b1, outroc, c1, d, d1, e, e1, f, f1, g, g1, h, h1, i, i1, j, j1, k, k1, l, l1 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
uni1 = range(-reais * densidade, reais * densidade)
uni2 = range(-imaginarios * densidade, imaginarios * densidade)
s = 3

for n in uni1:
    porc = round(50 + 100 * (n) / (len(uni1)), 2)
    print("\r", porc, '%')
    n /= densidade
    for m in uni2:
        m /= densidade
        z = complex(0, 0)
        c = complex(n, m)
        for contador in range(profundidade):
            z = z * z + c
            if abs(z) > lim1:
                if cores:
                    t = abs(z) / abs(c)
                    if contador <= profundidade * 1 / 12:
                        a.append(n)
                        a1.append(m)
                    elif contador >= profundidade * 1 / 12 and contador <= profundidade * 1 / 6:
                        b.append(n)
                        b1.append(m)
                    elif contador >= profundidade * 1 / 6 and contador <= profundidade * 1 / 4:
                        outroc.append(n)
                        c1.append(m)
                    elif contador >= profundidade * 1 / 4 and contador <= profundidade * 1 / 3:
                        d.append(n)
                        d1.append(m)
                    elif contador >= profundidade * 1 / 3 and contador <= profundidade * 5 / 12:
                        e.append(n)
                        e1.append(m)
                    elif contador >= profundidade * 5 / 12 and contador <= profundidade * 1 / 2:
                        f.append(n)
                        f1.append(m)
                    elif contador >= profundidade * 1 / 2 and contador <= profundidade * 7 / 12:
                        g.append(n)
                        g1.append(m)
                    elif contador >= profundidade * 7 / 12 and contador <= profundidade * 2 / 3:
                        h.append(n)
                        h1.append(m)
                    elif contador >= profundidade * 2 / 3 and contador <= profundidade * 3 / 4:
                        i.append(n)
                        i1.append(m)
                    elif contador >= profundidade * 3 / 4 and contador <= profundidade * 5 / 6:
                        j.append(n)
                        j1.append(m)
                    else:
                        k.append(n)
                        k1.append(m)
                break
            elif abs(z) < lim2:
                l.append(n)
                l1.append(m)
            else:
                continue

print("\n\nMontando o Gráfico\n\n")
plt.scatter(a, a1, color='#ff8888', s=s)
plt.scatter(b, b1, color='#ff0000', s=s)
plt.scatter(outroc, c1, color='#ffbb00', s=s)
plt.scatter(d, d1, color='#ff8800', s=s)
plt.scatter(e, e1, color='#ffbb00', s=s)
plt.scatter(f, f1, color='#ffff00', s=s)
plt.scatter(g, g1, color='#88ff00', s=s)
plt.scatter(h, h1, color='#00ff00', s=s)
plt.scatter(i, i1, color='#00ffff', s=s)
plt.scatter(j, j1, color='#0000ff', s=s)
plt.scatter(k, k1, color='#000088', s=s)
plt.scatter(l, l1, color='#000000', s=s)
plt.show()
