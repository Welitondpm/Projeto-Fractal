from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
from property_area_OOP import PropertyArea
import matplotlib.pyplot as plt
from fractal import Fractal
from random import randint


class Sierpinski(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)


    def Create_Fractal(self, args = {}):
        default_vars = {"times": 8, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6]]
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Triangle_Picker()
        self.Make_Graph()

    
    def Property_Area(self, value = 10, args={}):
        default_vars = {"times": 8, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6]]
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()
        self.passing = self.variables["size"] / value
        self.new_x, self.new_y = [], []
        limit = len(self.x)
        for item in range(limit):
            self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
            self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
            self.new_x.append(self.perimeter_x)
            self.new_y.append(self.perimeter_y)
        self.x, self.y = [], []
        for item in range(limit):
            self.x.extend(self.new_x[item])
            self.y.extend(self.new_y[item])
        self.property_area = PropertyArea(self.x, self.y, value, True, passing = self.passing)

    
    def Progression_Property_Area(self, value = 10, args={}):
        master_x = []
        master_y = []
        default_vars = {"times": 8, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6]]
        self.passing = self.variables["size"] / value
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            self.new_x, self.new_y = [], []
            limit = len(self.x)
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
                self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
                self.new_x.append(self.perimeter_x)
                self.new_y.append(self.perimeter_y)
            self.area_x, self.area_y = [], []
            for item in range(limit):
                self.area_x.extend(self.new_x[item])
                self.area_y.extend(self.new_y[item])
            self.property_area = PropertyArea(self.area_x, self.area_y, value, passing = self.passing)
            master_x.append(iteration_number)
            master_y.append(self.property_area.amount_of_marcked_squares)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property area\nSierpinski Fractal")
        plt.xlabel("Iteration Number")
        plt.ylabel("Marcked Squares")
        plt.show()

    
    def Property_Dimension(self, value = 10, args = {}):
        self.Property_Area(value, args = args)
        dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10, args = {}, color = "#000000", make_graph = True):
        master_x = []
        master_y = []
        default_vars = {"times": 8, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6]]
        self.passing = self.variables["size"] / value
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            self.new_x, self.new_y = [], []
            limit = len(self.x)
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
                self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
                self.new_x.append(self.perimeter_x)
                self.new_y.append(self.perimeter_y)
            self.area_x, self.area_y = [], []
            for item in range(limit):
                self.area_x.extend(self.new_x[item])
                self.area_y.extend(self.new_y[item])
            self.property_area = PropertyArea(self.area_x, self.area_y, value, passing = self.passing)
            self.dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
            master_x.append(iteration_number)
            master_y.append(self.dimension_obj.dimension)
        if make_graph:
            plt.plot(master_x, master_y, color = color)
            plt.scatter(master_x, master_y, color = color)
            plt.title("Progression of property dimension\nSierpinski Triangle Fractal")
            plt.xlabel("Iteration Number")
            plt.ylabel("Dimension Fractal")
        else:
            plt.plot(master_x, master_y, color = color, label = "Sierpinski Triangle")
            plt.scatter(master_x, master_y, color = color)


    def Setting_Function(self): 
        new_x, new_y = [], []
        siz = len(self.x)
        for item in range(siz):
            x, y = self.Sierpinski_Triangle(self.x[item], self.y[item])
            new_x.extend(x)
            new_y.extend(y)
        self.x, self.y = new_x, new_y

    
    def Sierpinski_Triangle(self, x, y):
        x_1 = x[0]
        x_2 = (x[0] + x[1]) / 2
        x_3 = x[1]
        x_4 = (x[1] + x[2]) / 2
        x_5 = x[2]
        x_6 = (x[2] + x[0]) / 2
        y_1 = y[0]
        y_2 = (y[0] + y[1]) / 2
        y_3 = y[1]
        y_4 = (y[1] + y[2]) / 2
        y_5 = y[2]
        y_6 = (y[2] + y[0]) / 2
        triangle_1_x = [x_1, x_6, x_2] 
        triangle_1_y = [y_1, y_6, y_2] 
        triangle_2_x = [x_2, x_3, x_4] 
        triangle_2_y = [y_2, y_3, y_4] 
        triangle_3_x = [x_6, x_4, x_5] 
        triangle_3_y = [y_6, y_4, y_5]
        return (triangle_1_x, triangle_2_x, triangle_3_x), (triangle_1_y, triangle_2_y, triangle_3_y)
    

    def Triangle_Picker(self):
        new_x, new_y = [], []
        indication = 0
        limit = len(self.x)
        while indication < limit:
            new_x.append([self.x[indication][0], self.x[indication][1], self.x[indication][2]])
            new_y.append([self.y[indication][0], self.y[indication][1], self.y[indication][2]])
            indication += 1
        self.x, self.y = new_x, new_y


    def Make_Graph(self, color = "#000000"):
        limit = len(self.x)
        for item in range(limit):
            plt.fill(self.x[item], self.y[item], color = color)


class SierpinskiCarpet(Sierpinski):
    def __init__(self, x = [], y = [], args = {}):
        Sierpinski.__init__(self, x, y, args)

    
    def Sierpinski_Triangle(self, x, y):
        x_1 = x[0]
        x_2 = x_1 + (x[3] - x[0]) / 3
        x_3 = x_1 + (x[3] - x[0]) * 2 / 3
        x_4 = x[3]
        y_1 = y[0]
        y_2 = y_1 + (y[2] - y[0]) / 3
        y_3 = y_1 + (y[2] - y[0]) * 2 / 3
        y_4 = y[2]
        square_1_x = [x_1, x_1, x_2, x_2]
        square_2_x = [x_2, x_2, x_3, x_3]
        square_3_x = [x_3, x_3, x_4, x_4]
        square_4_x = square_1_x
        square_5_x = square_3_x
        square_6_x = square_1_x
        square_7_x = square_2_x
        square_8_x = square_3_x
        square_1_y = [y_1, y_2, y_2, y_1]
        square_2_y = square_1_y
        square_3_y = square_1_y
        square_4_y = [y_2, y_3, y_3, y_2]
        square_5_y = square_4_y
        square_6_y = [y_3, y_4, y_4, y_3]
        square_7_y = square_6_y
        square_8_y = square_6_y
        return ((square_1_x, square_2_x, square_3_x, square_4_x, square_5_x, square_6_x, square_7_x, square_8_x), 
                (square_1_y, square_2_y, square_3_y, square_4_y, square_5_y, square_6_y, square_7_y, square_8_y))

        
    def Create_Fractal(self, args = {}):
        default_vars = {"times": 4, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[0, 0, self.variables["size"], self.variables["size"]]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0]]
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()

    
    def Property_Area(self, value = 10, args={}):
        default_vars = {"times": 4, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[0, 0, self.variables["size"], self.variables["size"]]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0]]
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()
        self.passing = self.variables["size"] / value
        self.new_x, self.new_y = [], []
        limit = len(self.x)
        for item in range(limit):
            self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
            self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
            self.new_x.append(self.perimeter_x)
            self.new_y.append(self.perimeter_y)
        self.x, self.y = [], []
        for item in range(limit):
            self.x.extend(self.new_x[item])
            self.y.extend(self.new_y[item])
        self.property_area = PropertyArea(self.x, self.y, value, True, passing = self.passing)

    
    def Progression_Property_Area(self, value = 10, args={}):
        master_x = []
        master_y = []
        default_vars = {"times": 4, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[0, 0, self.variables["size"], self.variables["size"]]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0]]
        self.passing = self.variables["size"] / value
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            self.new_x, self.new_y = [], []
            limit = len(self.x)
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
                self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
                self.new_x.append(self.perimeter_x)
                self.new_y.append(self.perimeter_y)
            self.area_x, self.area_y = [], []
            for item in range(limit):
                self.area_x.extend(self.new_x[item])
                self.area_y.extend(self.new_y[item])
            self.property_area = PropertyArea(self.area_x, self.area_y, value, passing = self.passing)
            master_x.append(iteration_number)
            master_y.append(self.property_area.amount_of_marcked_squares)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property area\nSierpinski Carpet Fractal")
        plt.xlabel("Iteration Number")
        plt.ylabel("Marcked Squares")
        plt.show()


    def Property_Dimension(self, value = 10, args = {}):
        self.Property_Area(value, args = args)
        dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10, args = {}, color = "#000000", make_graph = True):
        master_x = []
        master_y = []
        default_vars = {"times": 4, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        iteration_number = 0
        self.x = [[0, 0, self.variables["size"], self.variables["size"]]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0]]
        self.passing = self.variables["size"] / value
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            print("%d of %d" % (iteration_number, self.variables["times"]))
            self.new_x, self.new_y = [], []
            limit = len(self.x)
            for item in range(limit):
                self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
                self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
                self.new_x.append(self.perimeter_x)
                self.new_y.append(self.perimeter_y)
            self.area_x, self.area_y = [], []
            for item in range(limit):
                self.area_x.extend(self.new_x[item])
                self.area_y.extend(self.new_y[item])
            self.property_area = PropertyArea(self.area_x, self.area_y, value, passing = self.passing)
            self.dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
            master_x.append(iteration_number)
            master_y.append(self.dimension_obj.dimension)
        if make_graph:
            plt.plot(master_x, master_y, color = color)
            plt.scatter(master_x, master_y, color = color)
            plt.title("Progression of property dimension\nSierpinski Carpet Fractal")
            plt.xlabel("Iteration Number")
            plt.ylabel("Dimension Fractal")
        else:
            plt.plot(master_x, master_y, color = color, label = "Sierpinski Carpet")
            plt.scatter(master_x, master_y, color = color)


class ArrowHead(Fractal):
    def __init__(self, x = [[0, 1]], y = [[0, 0]], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 8}
        self.variables = self.Define_Vars(args, default_vars)
        

    def Create_Fractal(self):
        for iteration_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            print("%d of %d" % (iteration_number, self.variables["times"]))
        new_x, new_y = [], []
        index = 0
        limit = len(self.x)
        while index < limit:
            new_x.extend(self.x[index])
            new_y.extend(self.y[index])
            index += 1
        self.x, self.y = new_x, new_y
        self.Make_Graph()

    
    def Property_Perimeter(self, value = 10, paint_squares = True):
        self.Create_Fractal()
        passing = (max(self.x) - min(self.x)) / value
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(passing)
        self.property_square = PropertyPerSquare(self.x, self.y, value, paint_squares)

    
    def Progression_Property_Perimeter(self, value = 10):
        master_x = []
        master_y = []
        for iteration_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            new_x, new_y = [], []
            index = 0
            limit = len(self.x)
            while index < limit:
                new_x.extend(self.x[index])
                new_y.extend(self.y[index])
                index += 1
            passing = (max(new_x) - min(new_y)) / value
            self.property_perimeter = PropertyPerimeter(new_x, new_y)
            new_x, new_y = self.property_perimeter.Perimeter(passing)
            self.property_square = PropertyPerSquare(new_x, new_y, value, False)
            master_x.append(iteration_number)
            master_y.append(self.property_square.amount_of_marcked_squares)
            print("%d of %d" % (iteration_number, self.variables["times"]))
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property perimeter\nArrowHead Fractal")
        plt.xlabel("Iteration Number")
        plt.ylabel("Marcked Squares")
        plt.show()


    def Property_Dimension(self, value = 10):
        self.Property_Perimeter(value)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10, color = "#000000", make_graph = True):
        master_x = []
        master_y = []
        for iteration_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            new_x, new_y = [], []
            index = 0
            limit = len(self.x)
            while index < limit:
                new_x.extend(self.x[index])
                new_y.extend(self.y[index])
                index += 1
            passing = (max(new_x) - min(new_y)) / value
            self.property_perimeter = PropertyPerimeter(new_x, new_y)
            new_x, new_y = self.property_perimeter.Perimeter(passing)
            self.property_square = PropertyPerSquare(new_x, new_y, value)
            self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
            master_x.append(iteration_number)
            master_y.append(self.dimension_obj.dimension)
            print("%d of %d" % (iteration_number, self.variables["times"]))
        if make_graph:
            plt.plot(master_x, master_y, color = color)
            plt.scatter(master_x, master_y, color = color)
            plt.title("Progression of property dimension\nArrowHead Fractal")
            plt.xlabel("Iteration")
            plt.ylabel("Dimension Fractal")
        else:
            plt.plot(master_x, master_y, color = color, label = "Arrowhead")
            plt.scatter(master_x, master_y, color = color)


    def Make_Triangle(self):
        new_x, new_y = [], []
        limit = len(self.x)
        for item in range(limit):
            x_list = self.x[item]
            y_list = self.y[item]
            if y_list[1] - y_list[0] == 0:
                x_1 = x_list[0]
                x_2 = x_list[0] + (x_list[1] - x_list[0]) / 4
                x_3 = x_list[0] + (x_list[1] - x_list[0]) * 3 / 4
                x_4 = x_list[1]
                y_1 = y_list[0]
                y_2 = y_list[0] + abs(x_list[1] - x_list[0]) / 4
                y_3 = y_2
                y_4 = y_list[1]
            elif x_list[1] - x_list[0] == 0:
                x_1 = x_list[0]
                x_2 = x_list[0] + abs(y_list[1] - y_list[0]) / 4
                x_3 = x_2
                x_4 = x_list[1]
                y_1 = y_list[0]
                y_2 = y_list[0] + (y_list[1] - y_list[0]) / 4
                y_3 = y_list[0] + (y_list[1] - y_list[0]) * 2 / 4
                y_4 = y_list[1]
            elif x_list[1] > x_list[0] and y_list[1] > y_list[0]:
                x_1 = x_list[0]
                x_2 = x_list[1]
                x_3 = x_2 + (y_list[1] - y_list[0]) / 2
                x_4 = x_2
                y_1 = y_list[0]
                y_2 = y_1
                y_3 = y_list[0] + (y_list[1] - y_list[0]) / 2
                y_4 = y_list[1]
            elif x_list[1] < x_list[0] and y_list[1] > y_list[0]:
                x_1 = x_list[0]
                x_2 = x_list[1]
                x_3 = x_2 - (y_list[1] - y_list[0]) / 2
                x_4 = x_2
                y_1 = y_list[0]
                y_2 = y_1
                y_3 = y_list[0] + (y_list[1] - y_list[0]) / 2
                y_4 = y_list[1]
            elif x_list[1] < x_list[0] and y_list[1] < y_list[0]:
                x_1 = x_list[0]
                x_2 = x_list[0] - (y_list[1] - y_list[0]) / 2
                x_3 = x_1
                x_4 = x_list[1]
                y_1 = y_list[0]
                y_2 = y_list[0] + (y_list[1] - y_list[0]) / 2
                y_3 = y_list[1]
                y_4 = y_list[1]
            elif x_list[1] > x_list[0] and y_list[1] < y_list[0]:
                x_1 = x_list[0]
                x_2 = x_list[0] + (y_list[1] - y_list[0]) / 2
                x_3 = x_1
                x_4 = x_list[1]
                y_1 = y_list[0]
                y_2 = y_list[0] + (y_list[1] - y_list[0]) / 2
                y_3 = y_list[1]
                y_4 = y_list[1]
            new_x.extend(([x_1, x_2], [x_2, x_3], [x_3, x_4]))
            new_y.extend(([y_1, y_2], [y_2, y_3], [y_3, y_4]))
        self.x, self.y = new_x, new_y


    def Make_Graph(self, color = "#000000"):
        plt.plot(self.x, self.y, color = color)


class ChaoticTriangle(Fractal):
    def __init__(self, x = [0, 0.5, -0.5], y = [3 ** 0.5 / 2, 0, 0], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 1000000, "value": 2}
        self.variables = self.Define_Vars(args, default_vars)

    
    def Create_Fractal(self):
        self.Make_Chaotic_Triangle()
        self.Make_Graph()

    
    def Property_Square(self, value = 10, paint_squares = True):
        self.Create_Fractal()
        self.property_square = PropertyPerSquare(self.x, self.y, value, paint_squares)

    
    def Progression_Property_Square(self, value = 10, new_points_per_measurement = 50000):
        master_x = []
        master_y = []
        x_start = self.x
        y_start = self.y
        self.x = [sum(x_start) / len(x_start)]
        self.y = [sum(y_start) / len(y_start)]
        counter = 0
        limit = new_points_per_measurement
        iteration = 1
        while counter <= self.variables["times"]:
            if counter == limit or counter == self.variables["times"]:
                self.property_square = PropertyPerSquare(self.x, self.y, value)
                master_x.append(iteration)
                master_y.append(self.property_square.amount_of_marcked_squares)
                iteration += 1
                limit = iteration * new_points_per_measurement
            index = randint(0, len(x_start) - 1)
            self.x.append((x_start[index] + self.x[-1]) / self.variables["value"])
            self.y.append((y_start[index] + self.y[-1]) / self.variables["value"])
            counter += 1
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property per square\nChaotic Triangle Fractal")
        plt.xlabel("Points(n * new_points_per_measurement)")
        plt.ylabel("Marcked Squares")
        plt.show()

    
    def Property_Dimension(self, value = 10):
        self.Property_Square(value)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10, new_points_per_measurement = 50000, color = "#000000", make_graph = True):
        master_x = []
        master_y = []
        x_start = self.x
        y_start = self.y
        self.x = [sum(x_start) / len(x_start)]
        self.y = [sum(y_start) / len(y_start)]
        counter = 0
        limit = new_points_per_measurement
        iteration = 1
        while counter <= self.variables["times"]:
            if counter == limit or counter == self.variables["times"]:
                self.property_square = PropertyPerSquare(self.x, self.y, value)
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                master_x.append(iteration)
                master_y.append(self.dimension_obj.dimension)
                iteration += 1
                limit = iteration * new_points_per_measurement
            index = randint(0, len(x_start) - 1)
            self.x.append((x_start[index] + self.x[-1]) / self.variables["value"])
            self.y.append((y_start[index] + self.y[-1]) / self.variables["value"])
            counter += 1
        if make_graph:
            plt.plot(master_x, master_y, color = color)
            plt.scatter(master_x, master_y, color = color)
            plt.title("Progression of property dimension\nChaotic Triangle Fractal")
            plt.xlabel("Points(n * new_points_per_measurement)")
            plt.ylabel("Dimension Fractal")
        else:
            plt.plot(master_x, master_y, color = color, label = "Chaotic Triangle")
            plt.scatter(master_x, master_y, color = color)


    def Make_Chaotic_Triangle(self):
        counter = 0
        x_start = self.x
        y_start = self.y
        self.x = [sum(x_start) / len(x_start)]
        self.y = [sum(y_start) / len(y_start)]
        while counter <= self.variables["times"]:
            index = randint(0, len(x_start) - 1)
            self.x.append((x_start[index] + self.x[-1]) / self.variables["value"])
            self.y.append((y_start[index] + self.y[-1]) / self.variables["value"])
            counter += 1


    def Make_Graph(self, color = "#000000"):
        plt.scatter(self.x, self.y, color = color, s=0.01)


class SierpinskiPascal(Fractal):
    def __init__(self, args = {}):
        self.string_line = ""
        default_vars = {"times": 20}
        self.variables = self.Define_Vars(args, default_vars)
        number_line = 0
        while number_line < self.variables["times"]:
            number_line += 1
            line = self.Make_Line_Pascal(number_line)
            line = line[1:-1]
            self.string_line = self.Make_Spacing(line)
            print(self.string_line.center(175))
            self.string_line = ""


    def Make_Line_Pascal(self, number_line):
        line_list = [0, 1, 0]
        if number_line == 1:
            return line_list
        index = 0
        disposable_list = []
        while index < number_line:
            index += 1
            previous = line_list[0]
            for item in line_list:
                disposable_list.append(item + previous)
                previous = item
            disposable_list.append(previous + previous)
            line_list = []
            for item in disposable_list:
                line_list.append(item)
            disposable_list = []
        return line_list


    def Make_Spacing(self, line):
        string_line = ""
        for item in line:
            item_1 = str(item)
            if item % 2 == 0:
                item_1 = "     "
            else:
                if len(item_1) == 1:
                    item_1 = "   " + item_1
                elif len(item_1) == 2:
                    item_1 = "   " + item_1
                elif len(item_1) == 3:
                    item_1 = "  " + item_1
                elif len(item_1) == 4:
                    item_1 = " " + item_1
            string_line += item_1
        return string_line