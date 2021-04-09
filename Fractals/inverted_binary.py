from DD_property_per_square import PropertyPerSquare
from property_dimension import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class InvertedBinary(Fractal):
    def __init__(self, args = {}):
        Fractal.__init__(self, [], [])
        default_vars = {"end": 18, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.initiator = 0
        self.property_x, self.property_y = [], []

    
    def Create_Fractal(self):
        self.variables["end"] = 2 ** self.variables["end"]
        self.Do_Calculation()
        self.Make_Graph()


    def Do_Calculation(self):
        for point_x in range(self.initiator, self.variables["end"]):
            if self.Prime_Number(point_x):
                binary_number = self.Binary(point_x)
                decimal_number = self.Decimal(binary_number)
                point_y = point_x - decimal_number
                self.x.append(point_x)
                self.y.append(point_y)


    def First_Property(self, paint_squares = False):
        self.Create_Fractal()
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)

    
    def Property_Dimension(self):
        self.First_Property()
        self.x, self.y = self.Scale_Corrector()
        self.passing = 1 / self.variables["value"]
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, first_property = False, make_graph = True):
        self.passing = 1 / self.variables["value"]
        times = self.variables["end"]
        for iteration in range(2, times + 1):
            self.variables["end"] = 2 ** iteration
            self.initiator = 2 ** (iteration - 1)
            self.Do_Calculation()
            self.property_x.append(iteration)
            if first_property:
                self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"])
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                property_x, property_y = self.Scale_Corrector()
                self.property_square = PropertyPerSquare(property_x, property_y, self.variables["value"])
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property per square\nInverted Binary Fractal", "label_x": "Iteration", "label_y": "Marcked Squares", "label_plot": "Inverted Binary"}
        else:
            description = {"title": "Progression of property dimension\nInverted Binary Fractal", "label_x": "Iteration", "label_y": "Dimension Fractal", "label_plot": "Inverted Binary"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)

        
    def Scale_Corrector(self):
        property_x, property_y = [], []
        limit = len(self.x)
        index = 0
        while index < limit:
            property_x.append(self.x[index] / self.x[-1])
            property_y.append(self.y[index] / self.x[-1])
            index += 1
        return property_x, property_y


    def Make_Graph(self):
        plt.scatter(self.x, self.y, color = self.variables["color"], s = 0.01)


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