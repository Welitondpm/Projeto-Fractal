import matplotlib.pyplot as plt
import cmath

#ESSE É HARMÔNICO
profundidade = 1000
reais = 2
imaginarios =2
densidade = 100
cores = True


lim = 10
lim1 = lim
lim2 = 1 / lim
b, g, y, o, r, k = [], [], [], [], [], []
b_, g_, y_, o_, r_, k_ = [], [], [], [], [], []
uni1 = range(-reais * densidade, reais * densidade)
uni2 = range(-imaginarios * densidade, imaginarios * densidade)
s = 1

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
                    t = abs(z)/abs(c)
                    if contador >= profundidade / 7 and contador <= profundidade / 6:
                        b.append(n)
                        b_.append(m)
                    elif contador >= profundidade / 6 and contador <= profundidade / 5:
                        g.append(n)
                        g_.append(m)
                    elif contador >= profundidade / 5 and contador <= profundidade / 4:
                        y.append(n)
                        y_.append(m)
                    elif contador >= profundidade / 4 and contador <= profundidade / 3:
                        o.append(n)
                        o_.append(m)
                    elif contador >= profundidade / 3 and contador <= profundidade / 2:
                        r.append(n)
                        r_.append(m)
                break
            elif abs(z) < lim2:
                k.append(n)
                k_.append(m)
            else:
                continue

print("\n\nMontando o Gráfico\n\n")
plt.scatter(b, b_, color='#0000ff', s=s)
plt.scatter(g, g_, color='#00ff00', s=s)
plt.scatter(y, y_, color='#ffff00', s=s)
plt.scatter(o, o_, color='#ff8800', s=s)
plt.scatter(r, r_, color='#ff0000', s=s)
plt.scatter(k, k_, color='k', s=s)
plt.show()