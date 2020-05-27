import matplotlib.pyplot as plt

print("         !!!ATENÇÂO!!!\nESSE FRACTAL É ESTREMAMENTE PESADO NÃO USE VALORES MAIORES DO RECOMENDADOS")
profundidade = int(input("Profundidade (Recomendado: 1°[1000], 2°[1000]): "))
reais = int(input("Alcance dos reais (Recomendado: 1°[2], 2°[3]): "))
imaginarios = int(input("Alcance dos imaginários (Recomendado: 1°[2], 2°[3]): "))
densidade = int(input("Densidade (Recomendado: 1°[10], 2°[5]): "))
cores = 's'  # bool(input("[s/n] Cores? "))
lim = profundidade
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
            if abs(z) > lim:
                if cores:
                    R, G, B = 0, 0, 0
                    if contador <= profundidade / 6:
                        R, G, B = 255 * 6 * contador / profundidade, 0, 0
                    elif contador <= profundidade / 3:
                        R, G, B = 255, 255 * 6 * contador / profundidade, 0
                    elif contador <= profundidade / 2:
                        R, G, B = 255 - (255 * 6 * contador / profundidade), 255, 0
                    elif contador <= profundidade * 2 / 3:
                        R, G, B = 0, 255, 255 * 6 * contador / profundidade
                    elif contador <= profundidade * 5 / 6:
                        R, G, B = 0, 255 - (255 * 6 * contador / profundidade), 255
                    else:
                        R, G, B = 255 * 6 * contador / profundidade, 0, 255
                    R, G, B = str(hex(int(R)))[2:], str(hex(int(G)))[2:], str(hex(int(B)))[2:]
                    while len(R) < 2:
                        R = '0' + R
                    while len(G) < 2:
                        G = '0' + G
                    while len(B) < 2:
                        B = '0' + B
                    while len(R) > 2:
                        R = R[1:]
                    while len(G) > 2:
                        G = G[1:]
                    while len(B) > 2:
                        B = B[1:]
                    cor = '#' + R + G + B
                    plt.scatter([n], [m], color=cor, s=s, marker='s')
            else:
                l.append(n)
                l1.append(m)


print("\n\nMontando o Gráfico\n\n")
# plt.scatter(l,l1,color='#000000',s=s,marker='s')
plt.show()