# pip3 install py-cpuinfo

# import os
# import psutil
# import cpuinfo
# print(os.getpid())
# print(psutil.virtual_memory())
# print(cpuinfo.get_cpu_info()['brand_raw'])
# cpu = cpuinfo.get_cpu_info()['brand_raw']
# cpu = cpu.split()
# print(cpu[2])

# arquivo = open("Dados/tempo.txt", "a")
# dados = ["'Floco', 'Iteration: 8', 'Time: 20'//", "\n'Koch', 'Iteration: 8', 'Time: 20'//", "\n'Cantor', 'Iteration: 8', 'Time: 20'"]
# arquivo.writelines(dados)

# arquivo = open("Dados/tempo.txt", "r")
# a = arquivo.read()
# a = a.split("//")
# for item in a:
#     item = item.split(", ")
#     print(item[1])


###### Gerar Grafico Progressão Value


# x = [0.001, 0.0002, 0.0001, 6.666666666666667e-05, 5e-05, 4e-05, 3.3333333333333335e-05, 2.857142857142857e-05,
#     2.5e-05, 2.2222222222222223e-05, 2e-05, 1.8181818181818182e-05, 1.6666666666666667e-05, 1.5384615384615384e-05, 1.4285714285714285e-05, 1.3333333333333333e-05]
# y = [0.7347066460605267, 0.709462918005058, 0.7012051590686947, 0.700366867476848, 0.7007856913663121, 0.6967087745052252, 0.693715996438113, 0.693377908767262, 
#     0.6930570826448227, 0.6929135436657303, 0.6932750219509354, 0.6944221067149074, 0.6934576062620404, 0.6921009962809792, 0.6905060922663633, 0.6898858457386077]
# plt.plot(x, y, color = "#001100")
# plt.scatter(x, y, color = "#001100", label = "Conjunto de Cantor")

# x = [0.023422912126804366, 0.011711456063402183, 0.007807637375601455, 0.0058557280317010916]
# y = [2.2373453117675646, 2.1158542159588642, 2.0403447198410256, 1.9898230620484765]
# plt.plot(x, y, color = "#AA0000")
# plt.scatter(x, y, color = "#AA0000", label = "Curva do Dragão")

# x = [0.016180339887498948, 0.008090169943749474, 0.005393446629166316, 0.004045084971874737]
# y = [2.0823355846076237, 2.0532887820583308, 2.0343975197986173, 2.0251786248132215]
# plt.plot(x, y, color = "#00FFFF")
# plt.scatter(x, y, color = "#00FFFF", label = "Floco de Koch")

# x = [0.010000000000000004, 0.005000000000000002, 0.003333333333333335]
# y = [1.9999999999999902, 1.917090573060719, 1.8522505841499566]
# plt.plot(x, y, color = "#00AA11")
# plt.scatter(x, y, color = "#00AA11", label = "Curva de Hilbert")

# x = [0.01, 0.005, 0.0033333333333333335, 0.0025, 0.002]
# y = [1.7694124944689427, 1.746243804345288, 1.6859231221741229, 1.6303689299454274, 1.5854976178789062]
# plt.plot(x, y, color = "#FF0011")
# plt.scatter(x, y, color = "#FF0011", label = "Binário Invertido")

# x = [0.01, 0.005, 0.0033333333333333335, 0.0025, 0.002, 0.0016666666666666668]
# y = [1.276899248990031, 1.2875788021674028, 1.282602910118034, 1.2895037655729424, 1.2871522433515308, 1.2849397015306652]
# plt.plot(x, y, color = "#FF55AA")
# plt.scatter(x, y, color = "#FF55AA", label = "Curva de Koch")

# x = [0.01, 0.005, 0.0033333333333333335, 0.0025, 0.002]
# y = [1.7992311002370662, 1.7768396411587886, 1.770877091948114, 1.7622468448154196, 1.7558001277342279]
# plt.plot(x, y, color = "#550055")
# plt.scatter(x, y, color = "#550055", label = "Triângulo de Sierpinski")

# x = [0.01, 0.005, 0.0033333333333333335]
# y = [1.9776032687709608, 1.9351458810392093, 1.917675808005666]
# plt.plot(x, y, color = "#555555")
# plt.scatter(x, y, color = "#555555", label = "Tapete de Sierpinski")

# x = [0.01, 0.005, 0.0033333333333333335, 0.0025, 0.002, 0.0016666666666666668]
# y = [1.5574748196995223, 1.5585469931637883, 1.563393534050461, 1.5512208306663575, 1.5494005983916013, 1.5325571762923862]
# plt.plot(x, y, color = "#115599")
# plt.scatter(x, y, color = "#115599", label = "Cabeça de Seta")

# x = [0.01, 0.005]
# y = [1.6640956852167548, 1.6518371733108108]
# plt.plot(x, y, color = "#995511")
# plt.scatter(x, y, color = "#995511", label = "Triângulo Caótico")

# plt.legend(loc='upper left')
# plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
# plt.tight_layout()
# plt.xlabel(r"$\varepsilon$")
# plt.ylabel("Dimensão")
# plt.tight_layout()
# plt.savefig("Progression_fractal4.png")
# fractal = Fractal()
# fractal.Save_Pdf(file_name = "Progression_fractal")
# plt.show()