# pip3 install py-cpuinfo

import os
import psutil
import cpuinfo
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

def runtieeeeee():
    pass
    # arquivo = open("Fractals/Dados/tempo.txt", "a")
    # dados = []
    # dados.append("Cantor Set:   Iteração %d    Tempo %f" % (iteration, tempo))
    # arquivo.writelines(dados)




def Test_Max_Value():
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu = cpu.split()
    file = open("Dados/" + cpu[2] + ".txt", "a")
    max_time = 5
    max_time_property = 10
    # Max_Value_Cantor_Set(file, max_time, max_time_property)
    # Max_Value_Dragon_Curve(file, max_time, max_time_property)
    # Max_Value_Koch_Flake(file, max_time, max_time_property)
    # Max_Value_Hilbert_Curve(file, max_time, max_time_property)
    # Max_Value_Inverted_Binary(file, max_time, max_time_property)
    # Max_Value_Koch_Curve(file, max_time, max_time_property)
    # Max_Value_Mandelbrot(file, max_time, max_time_property)
    # Max_Value_Sierpinski_Triangle(file, max_time, max_time_property)
    # Max_Value_Sierpinski_Triangle(file, max_time, max_time_property)
    # Max_Value_Arrowhead(file, max_time, max_time_property)
    # Max_Value_Chaotic_Triangle(file, max_time, max_time_property)
    # Max_Value_Tree(file, max_time, max_time_property)


# Test_Max_Value()

# def Max_Value(self):
    # runtime = 0
    # iteration = 1
    # value = 50
    # self.object_fractal.runtime, self.object_fractal.dimension
    # while runtime <= max_time:
    #     runtime = Do_Tree(args = {"times": iteration})
    #     data = ["'Tree', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
    #     file.writelines(data)
    #     if psutil.virtual_memory().percent >= 60:
    #         break
    #     else:
    #         iteration += 1
    # runtime = 0
    # while runtime <= self.max_time:
    #     runtime, dimension = Do_Tree(property_dimension = True, args = {"times": iteration, "value": value})
    #     data = ["'" + self.fractal + "', '" + self.iteration + ": " + str(iteration) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
    #     file.writelines(data)
    #     if psutil.virtual_memory().percent >= 60:
    #         break
    #     else:
    #         value += 50
    # print(self.fractal + ", " + self.iteration + ": %d, Value: %d, Dimension: %f, Time: %f" % (iteration, value, dimension, runtime))