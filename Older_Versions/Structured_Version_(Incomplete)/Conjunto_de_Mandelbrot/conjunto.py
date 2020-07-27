import matplotlib.pyplot as plt

print("Use os valores igualmente pra todos EX: profundidade opção 1 o resto também \n(Os valores podem ser variados deste que mantenham sempre os reais e imaginarios inversamente proporsionais a densidade)")
profundidade = int(input("Profundidade (Recomendado: 1°[1000], 2°[1000]): "))
reais = int(input("Alcance dos reais (Recomendado: 1°[2], 2°[5]): "))
imaginarios = int(input("Alcance dos imaginários (Recomendado: 1°[2], 2°[5]): "))
densidade = int(input("Densidade (Recomendado: 1°[200], 2°[100]): "))
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