from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
import matplotlib.pyplot as plt
from fractal import Fractal


class CantorSet(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 10, "size": 50}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [[0, self.variables["size"]]]
        self.y = [[0, 0]]


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
        return new_x, new_y


    def Each_Row_Cantor_Set(self, x_position, value_of_y):
        x_1 = x_position[0]
        x_2 = x_1 + ((x_position[1] - x_position[0]) / 3)
        x_3 = x_position[1]
        x_4 = x_3 - ((x_position[1] - x_position[0]) / 3)
        return ([x_1, x_2], [x_3, x_4]), ([value_of_y, value_of_y], [value_of_y, value_of_y])

    
    def Create_Fractal(self):
        self.iteration_number = 0
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Make_Graph()
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.Make_Graph()

    
    def Property_Perimeter(self, value = 10, paint_squares = True):
        self.iteration_number = 0
        self.iteration_list = []
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.iteration_list.append([self.x, self.y])
            self.Make_Graph()
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.iteration_list.append([self.x, self.y])
        self.Make_Graph()
        passing = self.variables["size"] / value
        list_x, list_y = [], []
        for item in self.iteration_list:
            iteration_x, iteration_y = item[0], item[1]
            limit = len(iteration_x)
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(iteration_x[item], iteration_y[item])
                new_x, new_y = self.property_perimeter.Perimeter(passing)
                list_x.extend(new_x)
                list_y.extend(new_y)
        self.property_square = PropertyPerSquare(list_x, list_y, value, paint_squares)

    
    def Progression_Property_Perimeter(self, value = 10):
        master_x = []
        master_y = []
        
            # master_x.append(self.iteration_number)
            # master_y.append(self.property_square.amount_of_marcked_squares)

        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property per square\nCantor Set Fractal")
        plt.xlabel("Row")
        plt.ylabel("Marcked Squares")
        plt.show()


cantor = CantorSet(args={"times":2})
cantor.Property_Perimeter(value=10)
print("Quadrados pintados %d de %d" % (cantor.property_square.amount_of_marcked_squares, cantor.property_square.total_amount_of_squares))
cantor.Show_Graph()