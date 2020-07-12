import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


profundidade = 1000
reais = 2
imaginarios = 2
densidade = 100
cores = 's'


lim = profundidade
lim1 = lim
lim2 = 1 / lim
l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9, ll10, ll11, ll12, ll13, ll14, ll15, ll16 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31, l32 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
ll17, ll18, ll19, ll20, ll21, ll22, ll23, ll24, ll25, ll26, ll27, ll28, ll29, ll30, ll31, ll32 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
l0, ll0 = [], []
uni1 = range(int(-reais * densidade), int(reais * densidade))
uni2 = range(int(-imaginarios * densidade), int(imaginarios * densidade))
s = 1000 / densidade

for n in uni1:
    porc = round(50 + 100 * (n) / (len(uni1)), 2)
    print("\r", porc, '%')
    n /= densidade
    for m in uni2:
        m /= densidade
        z = complex(0, 0)
        c = complex(n, m)
        for contador in range(profundidade):
            z = z ** 2 + c
            if abs(z) > lim1:
                if cores:
                    t = abs(z) / abs(c)
                    if contador <= profundidade / 32:
                        l1.append(n)
                        ll1.append(m)
                    elif contador <= profundidade / 31:
                        l2.append(n)
                        ll2.append(m)
                    elif contador <= profundidade / 30:
                        l3.append(n)
                        ll3.append(m)
                    elif contador <= profundidade / 29:
                        l4.append(n)
                        ll4.append(m)
                    elif contador <= profundidade / 28:
                        l5.append(n)
                        ll5.append(m)
                    elif contador <= profundidade / 27:
                        l6.append(n)
                        ll6.append(m)
                    elif contador <= profundidade / 26:
                        l7.append(n)
                        ll7.append(m)
                    elif contador <= profundidade / 25:
                        l8.append(n)
                        ll8.append(m)
                    elif contador <= profundidade / 24:
                        l9.append(n)
                        ll9.append(m)
                    elif contador <= profundidade / 23:
                        l10.append(n)
                        ll10.append(m)
                    elif contador <= profundidade / 22:
                        l11.append(n)
                        ll11.append(m)
                    elif contador <= profundidade / 21:
                        l12.append(n)
                        ll12.append(m)
                    elif contador <= profundidade / 20:
                        l13.append(n)
                        ll13.append(m)
                    elif contador <= profundidade / 19:
                        l14.append(n)
                        ll14.append(m)
                    elif contador <= profundidade / 18:
                        l15.append(n)
                        ll15.append(m)
                    elif contador <= profundidade / 17:
                        l16.append(n)
                        ll16.append(m)
                    elif contador <= profundidade / 16:
                        l17.append(n)
                        ll17.append(m)
                    elif contador <= profundidade / 15:
                        l18.append(n)
                        ll18.append(m)
                    elif contador <= profundidade / 14:
                        l19.append(n)
                        ll19.append(m)
                    elif contador <= profundidade / 13:
                        l20.append(n)
                        ll20.append(m)
                    elif contador <= profundidade / 12:
                        l21.append(n)
                        ll21.append(m)
                    elif contador <= profundidade / 11:
                        l22.append(n)
                        ll22.append(m)
                    elif contador <= profundidade / 10:
                        l23.append(n)
                        ll23.append(m)
                    elif contador <= profundidade / 9:
                        l24.append(n)
                        ll24.append(m)
                    elif contador <= profundidade / 8:
                        l25.append(n)
                        ll25.append(m)
                    elif contador <= profundidade / 7:
                        l26.append(n)
                        ll26.append(m)
                    elif contador <= profundidade / 6:
                        l27.append(n)
                        ll27.append(m)
                    elif contador <= profundidade / 5:
                        l28.append(n)
                        ll28.append(m)
                    elif contador <= profundidade / 4:
                        l29.append(n)
                        ll29.append(m)
                    elif contador <= profundidade / 3:
                        l30.append(n)
                        ll30.append(m)
                    elif contador <= profundidade / 2:
                        l31.append(n)
                        ll31.append(m)
                    else:
                        l32.append(n)
                        ll32.append(m)
                break
            elif contador == profundidade-1 or abs(z) < .01 or (abs(z) < 10 and contador > 100):
                l0.append(n)
                ll0.append(m)
                break

print("\n\nMontando o Gráfico\n\n")
plt.scatter(l1, ll1, color='#008800', s=s)
plt.scatter(l2, ll2, color='#00ff00', s=s)
plt.scatter(l3, ll3, color='#00ff33', s=s)
plt.scatter(l4, ll4, color='#00ff66', s=s)
plt.scatter(l5, ll5, color='#00ff99', s=s)
plt.scatter(l6, ll6, color='#00ffcc', s=s)
plt.scatter(l7, ll7, color='#00ffff', s=s)
plt.scatter(l8, ll8, color='#00ccff', s=s)
plt.scatter(l9, ll9, color='#0099ff', s=s)
plt.scatter(l10, ll10, color='#0066ff', s=s)
plt.scatter(l11, ll11, color='#0033ff', s=s)
plt.scatter(l12, ll12, color='#0000ff', s=s)
plt.scatter(l13, ll13, color='#3300ff', s=s)
plt.scatter(l14, ll14, color='#6600ff', s=s)
plt.scatter(l15, ll15, color='#9900ff', s=s)
plt.scatter(l16, ll16, color='#cc00ff', s=s)
plt.scatter(l17, ll17, color='#ff00ff', s=s)
plt.scatter(l18, ll18, color='#ff00cc', s=s)
plt.scatter(l19, ll19, color='#ff0099', s=s)
plt.scatter(l20, ll20, color='#ff0066', s=s)
plt.scatter(l21, ll21, color='#ff0033', s=s)
plt.scatter(l22, ll22, color='#ff0000', s=s)
plt.scatter(l23, ll23, color='#ff3300', s=s)
plt.scatter(l24, ll24, color='#ff6600', s=s)
plt.scatter(l25, ll25, color='#ff9900', s=s)
plt.scatter(l26, ll26, color='#ffcc00', s=s)
plt.scatter(l27, ll27, color='#ffff00', s=s)
plt.scatter(l28, ll28, color='#ffff33', s=s)
plt.scatter(l29, ll29, color='#ffff66', s=s)
plt.scatter(l30, ll30, color='#ffff99', s=s)
plt.scatter(l31, ll31, color='#ffffcc', s=s)
plt.scatter(l32, ll32, color='#ffffff', s=s)
plt.scatter(l0, ll0, color='#000000', s=s/2)
plt.show()