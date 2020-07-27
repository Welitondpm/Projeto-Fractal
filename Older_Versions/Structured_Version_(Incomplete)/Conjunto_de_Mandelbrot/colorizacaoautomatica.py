import matplotlib.pyplot as plt

# print("Use os valores igualmente pra todos EX: profundidade opção 1 o resto também")
print("         !!!ATENÇÂO!!!\nESSE FRACTAL É ESTREMAMENTE PESADO NÃO USE VALORES MAIORES DO RECOMENDADOS")
profundidade = int(input("Profundidade (Recomendado: 1°[1000], 2°[1000]): "))
reais = int(input("Alcance dos reais (Recomendado: 1°[2], 2°[3]): "))
imaginarios = int(input("Alcance dos imaginários (Recomendado: 1°[2], 2°[3]): "))
densidade = int(input("Densidade (Recomendado: 1°[10], 2°[5]): "))
cores = 's'  # bool(input("[s/n] Cores? "))
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
# plt.scatter(l,l1,color='#000000',s=s)
plt.show()