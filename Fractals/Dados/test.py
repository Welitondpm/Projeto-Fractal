# pip3 install py-cpuinfo

import os
import psutil
import cpuinfo
# print(os.getpid())
# print(psutil.virtual_memory())
# print(cpuinfo.get_cpu_info()['brand_raw'])

# arquivo = open("Fractals/Dados/dados.txt", "a")
# dados = ["Floco: 9 iterações"]
# arquivo.writelines(dados)

def runtieeeeee():
    # arquivo = open("Fractals/Dados/tempo.txt", "a")
    runtime = 0
    iteration = 1
    # dados = []
    # dados = ["Floco: 9 iterações"]
    while runtime <= 240:
        runtime = Do_Cantor_Set(make_graph=False, args = {"times": iteration})
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            print("ainda não")
        # dados.append("Cantor Set:   Iteração %d    Tempo %f" % (iteration, tempo))
        iteration += 1
        # print(iteration, "   ", tempo)
    # arquivo.writelines(dados)