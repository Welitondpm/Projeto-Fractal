from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class CantorSet(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 10, "size": 1}
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
        self.Create_Fractal()
        passing = self.variables["size"] / value
        limit = len(self.x)
        new_x, new_y = [], []
        for item in range(limit):
            self.property_perimeter = PropertyPerimeter(self.x[item], self.y[item])
            new_x_perimeter, new_y_perimeter = self.property_perimeter.Perimeter(passing)
            new_x.extend(new_x_perimeter)
            new_y.extend(new_y_perimeter)
        self.property_square = PropertyPerSquare(new_x, new_y, value, paint_squares)

    
    def Progression_Property_Perimeter(self, value = 10):
        passing = self.variables["size"] / value
        master_x = []
        master_y = []

        self.iteration_number = 0
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            print("%d of %d" % (self.iteration_number, self.variables["times"]))
            limit = len(self.x)
            new_x, new_y = [], []
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item], self.y[item])
                new_x_perimeter, new_y_perimeter = self.property_perimeter.Perimeter(passing)
                new_x.extend(new_x_perimeter)
                new_y.extend(new_y_perimeter)
            self.property_square = PropertyPerSquare(new_x, new_y, value, False)
            master_x.append(self.iteration_number)
            master_y.append(self.property_square.amount_of_marcked_squares)
        
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property per square\nCantor Set Fractal")
        plt.xlabel("Row")
        plt.ylabel("Marcked Squares")
        plt.show()

    
    def Property_Dimension(self, value = 10):
        self.Property_Perimeter(value, False)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10):
        passing = self.variables["size"] / value
        master_x = []
        master_y = []

        self.iteration_number = 0
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            print("%d of %d" % (self.iteration_number, self.variables["times"]))
            limit = len(self.x)
            new_x, new_y = [], []
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item], self.y[item])
                new_x_perimeter, new_y_perimeter = self.property_perimeter.Perimeter(passing)
                new_x.extend(new_x_perimeter)
                new_y.extend(new_y_perimeter)
            self.property_square = PropertyPerSquare(new_x, new_y, value, False)
            self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
            master_x.append(self.iteration_number)
            master_y.append(self.dimension_obj.dimension)       
                
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property dimension\nCantor Set Fractal")
        plt.xlabel("Points(n * new_points_per_measurement)")
        plt.ylabel("Dimension Fractal")
        plt.show()