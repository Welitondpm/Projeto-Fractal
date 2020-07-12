import matplotlib.pyplot as plt


profundidade = 1000
reais = 2
imaginarios = 2
densidade = 200


la1, lb1 = [], []
la2, lb2 = [], []
lim = profundidade
s = 1000 / densidade

for n in range(-reais * densidade, reais * densidade):
    porc = round(50 + 100 * (n) / (len(range(-reais * densidade, reais * densidade))), 2)
    print("\r", porc, '%')
    n /= densidade
    for m in range(-imaginarios * densidade, imaginarios * densidade):
        m /= densidade
        z = complex(0, 0)
        c = complex(n, m)
        for o in range(profundidade):
            z = z * z + c
            if abs(z) > lim:
                la1.append(n)
                lb1.append(m)
                break
        if abs(z) > abs(c):
            la1.append(n)
            lb1.append(m)
        else:
            la2.append(n)
            lb2.append(m)

print("Montando o Gráfico")
plt.scatter(la1, lb1, s=s, marker='s')
plt.scatter(la2, lb2, color='black', s=s, marker='s')
plt.show()