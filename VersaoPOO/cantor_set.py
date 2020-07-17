import matplotlib.pyplot as plt
from main import Fractal


class Cantor_Set(Fractal):
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y


    def Create_Fractal(self, args = {}):
        default_vars = {"times": 10, "size": 50}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [[0, self.variables["size"]]]
        self.y = [[0, 0]]
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Make_Graph()
            self.Organizing_Function(iteration_number)
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()


    def Make_Graph(self, color = "#000000"):
        limit = len(self.x)
        for item in range(limit):
            plt.plot(self.x[item], self.y[item], color = color, linewidth = 1)


    def Organizing_Function(self, value_of_y):
        new_x, new_y = [], []
        limit = len(self.x)
        for item in range(limit):
            x_list, y_list = self.Each_Row_Cantor_Set(self.x[item], value_of_y)
            new_x.extend(x_list)
            new_y.extend(y_list)
        self.x, self.y = new_x, new_y


    def Each_Row_Cantor_Set(self, x_position, value_of_y):
        x_1 = x_position[0]
        x_2 = x_1 + ((x_position[1] - x_position[0]) / 3)
        x_3 = x_position[1]
        x_4 = x_3 - ((x_position[1] - x_position[0]) / 3)
        return ([x_1, x_2], [x_3, x_4]), ([value_of_y, value_of_y], [value_of_y, value_of_y])


#### Execute Cantor Set
# cantorSet = Cantor_Set()
# cantorSet.Create_Fractal()
# cantorSet.Make_Graph()
# cantorSet.Show_Graph()