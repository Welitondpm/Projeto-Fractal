import matplotlib.pyplot as plt

profundidade = 1000
reais = 2
imaginarios = 2
densidade = 200
cores = 's'


lim = profundidade
lim1 = lim
lim2 = 1 / lim
a, a1, b, b1, outroc, c1, d, d1, e, e1, f, f1, g, g1, h, h1, i, i1, j, j1, k, k1, l, l1 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
uni1 = range(-reais * densidade, reais * densidade)
uni2 = range(-imaginarios * densidade, imaginarios * densidade)
s = 1000 / densidade

for n in uni1:
    porc = round(50 + 100 * (n) / (len(uni1)), 2)
    print(porc + " %")
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
                    if contador <= profundidade * 1 / 1024:
                        a.append(n)
                        a1.append(m)
                    elif contador >= profundidade * 1 / 1024 and contador <= profundidade * 1 / 512:
                        b.append(n)
                        b1.append(m)
                    elif contador >= profundidade * 1 / 512 and contador <= profundidade * 1 / 256:
                        outroc.append(n)
                        c1.append(m)
                    elif contador >= profundidade * 1 / 256 and contador <= profundidade * 1 / 128:
                        d.append(n)
                        d1.append(m)
                    elif contador >= profundidade * 1 / 128 and contador <= profundidade * 1 / 64:
                        e.append(n)
                        e1.append(m)
                    elif contador >= profundidade * 1 / 64 and contador <= profundidade * 1 / 32:
                        f.append(n)
                        f1.append(m)
                    elif contador >= profundidade * 1 / 32 and contador <= profundidade * 1 / 16:
                        g.append(n)
                        g1.append(m)
                    elif contador >= profundidade * 1 / 16 and contador <= profundidade * 1 / 8:
                        h.append(n)
                        h1.append(m)
                    elif contador >= profundidade * 1 / 8 and contador <= profundidade * 1 / 4:
                        i.append(n)
                        i1.append(m)
                    elif contador >= profundidade * 1 / 4 and contador <= profundidade * 1 / 2:
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

plt.scatter(a, a1, color='#ff8888', s=s, marker='s')
plt.scatter(b, b1, color='#ff0000', s=s, marker='s')
plt.scatter(outroc, c1, color='#ffbb00', s=s, marker='s')
plt.scatter(d, d1, color='#ff8800', s=s, marker='s')
plt.scatter(e, e1, color='#ffbb00', s=s, marker='s')
plt.scatter(f, f1, color='#ffff00', s=s, marker='s')
plt.scatter(g, g1, color='#88ff00', s=s, marker='s')
plt.scatter(h, h1, color='#00ff00', s=s, marker='s')
plt.scatter(i, i1, color='#00ffff', s=s, marker='s')
plt.scatter(j, j1, color='#0000ff', s=s, marker='s')
plt.scatter(k, k1, color='#000088', s=s, marker='s')
plt.scatter(l, l1, color='#000000', s=s, marker='s')
plt.show()