import matplotlib.pyplot as plt
import cmath


print("Use os valores igualmente pra todos EX: profundidade opção 1 o resto também \n(Os valores podem ser variados deste que mantenham sempre os reais e imaginarios inversamente proporsionais a densidade)")
profundidade = int(input("Profundidade (Recomendado: 1°[1000], 2°[1000]): "))
reais = int(input("Alcance dos reais (Recomendado: 1°[2], 2°[20]): "))
imaginarios = int(input("Alcance dos imaginários (Recomendado: 1°[2], 2°[20]): "))
densidade = int(input("Densidade (Recomendado: 1°[200], 2°[100]): "))
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