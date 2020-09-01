from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class DragonCurve(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [0, 1]
        self.y = [0, 0]
        

    
    def Create_Fractal(self):
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Do_Calculation()
            if iteration_number > 2:
                self.Scale_Corrector()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()

    
    def Property_Perimeter(self, value = 10, paint_squares = True):
        self.Create_Fractal()
        passing = (max(self.x) - min(self.y)) / value
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(passing)
        self.property_square = PropertyPerSquare(self.x, self.y, value, paint_squares)


    def Progression_Property_Perimeter(self, value = 10):
        master_x = []
        master_y = []
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Do_Calculation()
            if iteration_number > 2:
                self.Scale_Corrector()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            passing = (max(self.x) - min(self.y)) / value
            self.property_perimeter = PropertyPerimeter(self.x, self.y)
            self.x, self.y = self.property_perimeter.Perimeter(passing)
            self.property_square = PropertyPerSquare(self.x, self.y, value, False)
            master_x.append(iteration_number)
            master_y.append(self.property_square.amount_of_marcked_squares)   
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property perimeter\nDragon Curve Fractal")
        plt.xlabel("Iteration")
        plt.ylabel("Marcked Squares")
        plt.show()

    
    def Property_Dimension(self, value = 10):
        self.Property_Perimeter(value)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10):
        master_x = []
        master_y = []
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Do_Calculation()
            if iteration_number > 2:
                self.Scale_Corrector()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            passing = (max(self.x) - min(self.y)) / value
            self.property_perimeter = PropertyPerimeter(self.x, self.y)
            self.x, self.y = self.property_perimeter.Perimeter(passing)
            self.property_square = PropertyPerSquare(self.x, self.y, value, False)
            self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
            master_x.append(iteration_number)
            master_y.append(self.dimension_obj.dimension)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property dimension\nDragon Curve Fractal")
        plt.xlabel("Iteration")
        plt.ylabel("Dimension Fractal")
        plt.show()


    def Make_Graph(self, color = "#000000"):
        plt.plot(self.x, self.y, color = color)


    def Do_Calculation(self):
        new_x = [self.x[-1]]
        new_y = [self.y[-1]]
        limit = len(self.x)
        for item in range(1, limit):
            new_x.append(new_x[-1] - (self.y[-item] - self.y[-item -1]))
            new_y.append(new_y[-1] + (self.x[-item] - self.x[-item -1]))
        self.x = self.x + new_x
        self.y = self.y + new_y


    def Scale_Corrector(self):
        new_x, new_y = [], []
        index = 0
        limit = len(self.x)
        while index < limit:
            new_x.append(self.x[index] / (2 ** 0.5))
            new_y.append(self.y[index] / (2 ** 0.5))
            index += 1
        self.x, self.y = new_x, new_y