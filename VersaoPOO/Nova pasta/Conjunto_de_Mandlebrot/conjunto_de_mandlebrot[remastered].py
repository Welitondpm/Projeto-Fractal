import matplotlib.pyplot as plt
import cmath


profundidade = 1000
reais = 2
imaginarios = 2
densidade = 200


la2, lb2 = [], []
lim = 20

for n in range(-reais * densidade, reais * densidade):
    print(round(100 * (n + reais * densidade) / (reais * densidade * 2), 2), "%")
    n /= densidade
    for m in range(-imaginarios * densidade, imaginarios * densidade):
        m /= densidade
        z = complex(0, 0)
        c = complex(n, m)
        for o in range(profundidade):
            z = z * z + c
            if abs(z) > lim:
                break
        if abs(z) < abs(c):
            la2.append(n)
            lb2.append(m)


print("Montando o Gráfico")
plt.scatter(la2, lb2, color='black', s=.5)
plt.show()