import matplotlib.pyplot as plt
import cmath
#ESSE É HARMÔNICO
print("Use os valores igualmente pra todos EX: profundidade opção 1 o resto também \n(Os valores podem ser variados deste que mantenham sempre os reais e imaginarios inversamente proporsionais a densidade)")
profundidade = int(input("Profundidade (Recomendado: 1°[1000], 2°[1000]): "))
reais = int(input("Alcance dos reais (Recomendado: 1°[2], 2°[5]): "))
imaginarios = int(input("Alcance dos imaginários (Recomendado: 1°[2], 2°[5]): "))
densidade = int(input("Densidade (Recomendado: 1°[200], 2°[100]): "))
cores = bool(input("[s/n] Cores?: "))
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
