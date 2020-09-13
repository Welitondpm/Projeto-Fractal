from property_per_square_OOP import PropertyPerSquare
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class InvertedBinary(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"end": 18}
        self.variables = self.Define_Vars(args, default_vars)
        self.start = 0

    
    def Create_Fractal(self):
        self.variables["end"] = 2 ** self.variables["end"]
        self.Do_Calculation()
        self.Make_Graph()


    def Do_Calculation(self):
        for point_x in range(self.start, self.variables["end"]):
            if self.Prime_Number(point_x):
                binary_number = self.Binary(point_x)
                decimal_number = self.Decimal(binary_number)
                point_y = point_x - decimal_number
                self.x.append(point_x)
                self.y.append(point_y)


    def Property_Square(self, value = 10, paint_squares = False):
        self.Create_Fractal()
        self.property_square = PropertyPerSquare(self.x, self.y, value, paint_squares)


    def Progression_Property_Square(self, value = 10):
        times = self.variables["end"]
        master_x = []
        master_y = []
        for iteration in range(1, times + 1):
            self.variables["end"] = 2 ** iteration
            self.start = 2 ** (iteration - 1)
            self.Do_Calculation()
            self.property_square = PropertyPerSquare(self.x, self.y, value)
            master_x.append(iteration)
            master_y.append(self.property_square.amount_of_marcked_squares)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property per square\nInverted Binary Fractal")
        plt.xlabel("Iteration")
        plt.ylabel("Marcked Squares")
        plt.show()

    
    def Property_Dimension(self, value = 10):
        self.Property_Square(value)
        self.passing = 2 ** self.variables["end"] / value
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10, color = "#000000", make_graph = True):
        self.passing = 1 / value
        times = self.variables["end"]
        master_x = []
        master_y = []
        for iteration in range(2, times + 1):
            self.variables["end"] = 2 ** iteration
            self.start = 2 ** (iteration - 1)
            self.Do_Calculation()
            property_x, property_y = Scale_Corrector()
            self.property_square = PropertyPerSquare(property_x, property_y, value)
            self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.passing)
            master_x.append(iteration)
            master_y.append(self.dimension_obj.dimension)
        if make_graph:
            plt.plot(master_x, master_y, color = color)
            plt.scatter(master_x, master_y, color = color)
            plt.title("Progression of property dimension\nInverted Binary Fractal")
            plt.xlabel("Iteration")
            plt.ylabel("Dimension Fractal")
        else:
            plt.plot(master_x, master_y, color = color, label = "Inverted Binary")
            plt.scatter(master_x, master_y, color = color)

        
    def Scale_Corrector(self):
        property_x, property_y = [], []
        limit = len(self.x)
        index = 0
        while index < limit:
            property_x.append(self.x[index] / self.x[-1])
            property_y.append(self.y[index] / self.x[-1])
            index += 1
        return property_x, property_y


    def Make_Graph(self, color = "#000000"):
        plt.scatter(self.x, self.y, color = color, s = 0.01)


    def Prime_Number(self, point_x):
        limit = int(point_x ** 0.5) + 1
        for value in range(2, limit):
            if point_x % value == 0:
                return False
        return True

    
    def Binary(self, value):
        binary_list = []
        while value >= 2:
            rest = value % 2
            value //= 2
            binary_list.append(rest)
        if value == 1:
            binary_list.append(value)
        binary_list.reverse()
        return binary_list

    
    def Decimal(self, binary_number):
        index = 0
        binary_sum = 0
        for item in binary_number:
            binary_sum += (item * (2 ** index))
            index += 1
        return binary_sum