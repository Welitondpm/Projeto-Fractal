from DD_property_per_square import PropertyPerSquare
from DD_property_perimeter import PropertyPerimeter
from property_dimension import Dimension
from DD_property_area import PropertyArea
import matplotlib.pyplot as plt
from fractal import Fractal
from random import randint


class Sierpinski(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        self.Create_Vars(args)

    
    def Create_Vars(self, args = {}):
        default_vars = {"times": 8, "size": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.iteration_number = 0
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6]]
        self.property_x, self.property_y = [], []
        self.passing = self.variables["size"] / self.variables["value"]


    def Create_Fractal(self, property_area = False):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
        if not property_area:
            self.Triangle_Picker()
        self.Make_Graph()


    def Do_Area(self):
        self.new_x, self.new_y = [], []
        self.limit = len(self.x)
        for item in range(self.limit):
            self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
            self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
            self.new_x.append(self.perimeter_x)
            self.new_y.append(self.perimeter_y)
        self.area_x, self.area_y = [], []
        for item in range(self.limit):
            self.area_x.extend(self.new_x[item])
            self.area_y.extend(self.new_y[item])
        self.property_area = PropertyArea(self.area_x, self.area_y, self.variables["value"], passing = self.passing)

    
    def First_Property(self):
        self.Create_Fractal(property_area = True)
        self.Do_Area()

    
    def Property_Dimension(self):
        self.First_Property()
        dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, first_property = False, make_graph = True):
        self.Create_Vars()
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
            self.Do_Area()
            self.property_x.append(self.iteration_number)
            if first_property:
                self.property_y.append(self.property_area.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property area\nSierpinski Triangle Fractal", "label_x": "Iteration Number", "label_y": "Marcked Squares", "label_plot": "Sierpinski Triangle"}
        else:
            description = {"title": "Progression of property dimension\nSierpinski Triangle Fractal", "label_x": "Iteration Number", "label_y": "Dimension Fractal", "label_plot": "Sierpinski Triangle"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


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


    def Make_Graph(self):
        limit = len(self.x)
        for item in range(limit):
            plt.fill(self.x[item], self.y[item], color = self.variables["color"])


class SierpinskiCarpet(Sierpinski):
    def __init__(self, args = {}):
        Sierpinski.__init__(self, [], [], args)

    
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


    def Create_Vars(self, args = {}):
        default_vars = {"times": 4, "size": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.iteration_number = 0
        self.x = [[0, 0, self.variables["size"], self.variables["size"]]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0]]
        self.property_x, self.property_y = [], []
        self.passing = self.variables["size"] / self.variables["value"]


    def Create_Fractal(self):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.Make_Graph()

    
    def Do_Area(self):
        self.new_x, self.new_y = [], []
        self.limit = len(self.x)
        for item in range(self.limit):
            self.property_perimeter = PropertyPerimeter(self.x[item] + [self.x[item][0]], self.y[item] + [self.y[item][0]])
            self.perimeter_x, self.perimeter_y = self.property_perimeter.Perimeter(self.passing)
            self.new_x.append(self.perimeter_x)
            self.new_y.append(self.perimeter_y)
        self.area_x, self.area_y = [], []
        for item in range(self.limit):
            self.area_x.extend(self.new_x[item])
            self.area_y.extend(self.new_y[item])
        self.property_area = PropertyArea(self.area_x, self.area_y, self.variables["value"], passing = self.passing)

    
    def First_Property(self):
        self.Create_Fractal()
        self.Do_Area()
    

    def Property_Dimension(self):
        self.First_Property()
        dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, first_property = False, make_graph = True):
        self.Create_Vars()
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
            self.Do_Area()
            self.property_x.append(self.iteration_number)
            if first_property:
                self.property_y.append(self.property_area.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property area\nSierpinski Carpet Fractal", "label_x": "Iteration Number", "label_y": "Marcked Squares", "label_plot": "Sierpinski Carpet"}
        else:
            description = {"title": "Progression of property dimension\nSierpinski Carpet Fractal", "label_x": "Iteration Number", "label_y": "Dimension Fractal", "label_plot": "Sierpinski Carpet"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


class Arrowhead(Fractal):
    def __init__(self, x = [[0, 1]], y = [[0, 0]], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 8, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.property_x, self.property_y = [], []
        

    def Create_Fractal(self):
        for iteration_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            # print("%d of %d" % (iteration_number, self.variables["times"]))
        new_x, new_y = [], []
        index = 0
        limit = len(self.x)
        while index < limit:
            new_x.extend(self.x[index])
            new_y.extend(self.y[index])
            index += 1
        self.x, self.y = new_x, new_y
        self.Make_Graph()

    
    def First_Property(self, paint_squares = True):
        self.Create_Fractal()
        passing = (max(self.x) - min(self.x)) / self.variables["value"]
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(passing)
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)

    
    def Property_Dimension(self):
        self.First_Property()
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, first_property = False, make_graph = True):
        for iteration_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            new_x, new_y = [], []
            index = 0
            limit = len(self.x)
            while index < limit:
                new_x.extend(self.x[index])
                new_y.extend(self.y[index])
                index += 1
            passing = (max(new_x) - min(new_y)) / self.variables["value"]
            self.property_perimeter = PropertyPerimeter(new_x, new_y)
            new_x, new_y = self.property_perimeter.Perimeter(passing)
            self.property_square = PropertyPerSquare(new_x, new_y, self.variables["value"])
            # print("%d of %d" % (iteration_number, self.variables["times"]))
            self.property_x.append(iteration_number)
            if first_property:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property perimeter\nArrowhead Fractal", "label_x": "Iteration", "label_y": "Marcked Squares", "label_plot": "Arrowhead"}
        else:
            description = {"title": "Progression of property dimension\nArrowhead Fractal", "label_x": "Iteration", "label_y": "Dimension Fractal", "label_plot": "Arrowhead"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


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


    def Make_Graph(self):
        plt.plot(self.x, self.y, color = self.variables["color"])


class ChaoticTriangle(Fractal):
    def __init__(self, x = [0, 0.5, -0.5], y = [3 ** 0.5 / 2, 0, 0], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 100000, "divader": 2, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        self.property_x, self.property_y = [], []

    
    def Create_Fractal(self):
        self.Make_Chaotic_Triangle()
        self.Make_Graph()

    
    def First_Property(self, paint_squares = True):
        self.Create_Fractal()
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)
    

    def Property_Dimension(self):
        self.First_Property(paint_squares = False)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension


    def Progression_Property(self, new_points_per_measurement = 10000, first_property = False, make_graph = True):
        x_start = self.x
        y_start = self.y
        self.x = [sum(x_start) / len(x_start)]
        self.y = [sum(y_start) / len(y_start)]
        counter = 0
        limit = new_points_per_measurement
        iteration = 1
        while counter <= self.variables["times"]:
            if counter == limit or counter == self.variables["times"]:
                self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"])
                self.property_x.append(iteration)
                if first_property:
                    self.property_y.append(self.property_square.amount_of_marcked_squares)
                else:
                    self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                    self.property_y.append(self.dimension_obj.dimension)
                iteration += 1
                limit = iteration * new_points_per_measurement
            index = randint(0, len(x_start) - 1)
            self.x.append((x_start[index] + self.x[-1]) / self.variables["divader"])
            self.y.append((y_start[index] + self.y[-1]) / self.variables["divader"])
            counter += 1
        if first_property:
            description = {"title": "Progression of property per square\nChaotic Triangle Fractal", "label_x": "Points(n * new_points_per_measurement)", "label_y": "Marcked Squares", "label_plot": "Chaotic Triangle"}
        else:
            description = {"title": "Progression of property dimension\nChaotic Triangle Fractal", "label_x": "Points(n * new_points_per_measurement)", "label_y": "Dimension Fractal", "label_plot": "Chaotic Triangle"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


    def Make_Chaotic_Triangle(self):
        counter = 0
        x_start = self.x
        y_start = self.y
        self.x = [sum(x_start) / len(x_start)]
        self.y = [sum(y_start) / len(y_start)]
        while counter <= self.variables["times"]:
            index = randint(0, len(x_start) - 1)
            self.x.append((x_start[index] + self.x[-1]) / self.variables["divader"])
            self.y.append((y_start[index] + self.y[-1]) / self.variables["divader"])
            counter += 1


    def Make_Graph(self):
        plt.scatter(self.x, self.y, color = self.variables["color"], s=0.01)


class SierpinskiPascal(Fractal):
    def __init__(self, args = {}):
        self.string_line = ""
        default_vars = {"times": 20}
        self.variables = self.Define_Vars(args, default_vars)

    
    def Create_Fractal(self):
        number_line = 0
        while number_line < self.variables["times"]:
            number_line += 1
            line = self.Make_Line_Pascal(number_line)
            line = line[1:-1]
            self.string_line = self.Make_Spacing(line)
            # print(self.string_line.center(175))
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