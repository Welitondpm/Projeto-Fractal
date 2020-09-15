from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal
import random
import math


class Tree(Fractal):
    def __init__(self, args = {}):
        default_vars = {"times": 10, "size": 1, "angle": 15, "z": 0, "zimp": 0, "w": 0, "wimp": 0, "value": 10, "color": "#000000"}
        self.variables = self.Define_Vars(args, default_vars)
        Fractal.__init__(self, [[0], [0]], [[0], [self.variables["size"]]])
        self.variables["theta"] = (self.variables["angle"] * math.pi) / 180
        self.variables["angle"] = [self.variables["theta"], -self.variables["theta"]]
        self.variables["z"] = 1 - self.variables["z"] / 100 + self.variables["z"] / 50
        self.variables["w"] = 1 - self.variables["w"] / 100 + self.variables["w"] / 50
        self.new_xx, self.new_yy = [], []
        self.property_x, self.property_y = [], []

    
    def Create_Fractal(self):
        for iteration_number in range(self.variables["times"]):
            self.Do_Calculation()
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
        self.Make_Graph()

    
    def Do_Perimeter(self, paint_squares = False):
        self.passing = (max(self.x[-1]) - min(self.x[-1])) / self.variables["value"]
        self.Make_Graph_Property()
        self.property_square = PropertyPerSquare(self.new_xx, self.new_yy, self.variables["value"], paint_squares)

    
    def Property_Perimeter(self, paint_squares = True):
        self.noshow = not paint_squares
        for iteration_number in range(self.variables["times"]):
            self.Do_Calculation()
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
        self.Do_Perimeter(paint_squares)        

    
    def Property_Dimension(self):
        self.Property_Perimeter(paint_squares = False)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, property_perimeter = False, make_graph = True):
        self.noshow = True
        self.Do_Calculation()
        self.property_x.append(1)
        self.property_y.append(self.variables["size"] / self.variables["value"])
        print("%d of %d" % (1, self.variables["times"]))
        for iteration_number in range(1, self.variables["times"]):
            self.Do_Calculation()
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.Do_Perimeter()
            self.new_xx, self.new_yy = [], []
            self.property_x.append(iteration_number + 1)
            if property_perimeter:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if property_perimeter:
            description = {"title": "Progression of property perimeter\nTree Fractal", "label_x": "Iteration Number", "label_y": "Marcked Squares", "label_plot": "Tree"}
        else:
            description = {"title": "Progression of property dimension\nTree Fractal", "label_x": "Iteration Number", "label_y": "Dimension Fractal", "label_plot": "Tree"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


    def Make_Graph_Property(self):
        disposable_list = []
        list_x, list_of_list_x = [], []
        list_y, list_of_list_y = [], []
        maximum_size = len(self.x[-1])
        for item in self.x:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list
                disposable_list = []
            list_of_list_x.append(item)
        for item in self.y:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list
                disposable_list = []
            list_of_list_y.append(item)
        for item in range(maximum_size - 1):
            for subitem in range(len(self.x) - 1):
                list_x.append(list_of_list_x[subitem][item])
                list_y.append(list_of_list_y[subitem][item])
            self.property_perimeter = PropertyPerimeter(list_x, list_y)
            new_x, new_y = self.property_perimeter.Perimeter(self.passing)
            if self.noshow:
                pass
            else:
                plt.plot(list_x, list_y, color = self.variables["color"])
            self.new_xx.extend(new_x)
            self.new_yy.extend(new_y)
            list_x, list_y = [], [] ## Jamais comente essa linha POR FAVOR!!!!!


    def Make_Graph(self):
        disposable_list = []
        list_x, list_of_list_x = [], []
        list_y, list_of_list_y = [], []
        maximum_size = len(self.x[-1])
        for item in self.x:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list
                disposable_list = []
            list_of_list_x.append(item)
        for item in self.y:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list
                disposable_list = []
            list_of_list_y.append(item)
        for item in range(maximum_size - 1):
            for subitem in range(len(self.x) - 1):
                list_x.append(list_of_list_x[subitem][item])
                list_y.append(list_of_list_y[subitem][item])
            plt.plot(list_x, list_y, color = self.variables["color"])
            list_x, list_y = [], [] ## Jamais comente essa linha POR FAVOR!!!!!


    def Imperfectionate(self, w_z, wimp_zimp):
        if type(w_z) == int or type(w_z) == float:
            return w_z * 1 - wimp_zimp / 200 + (random.random() * wimp_zimp) / 100
        else:
            new_x = []
            for item in w_z:
                if type(item) == int or type(item) == float:
                    item *= 1 - wimp_zimp / 200 + (random.random() * wimp_zimp) / 100
                    new_x.append(item)
                else:
                    new_list_of_x = []
                    for subitem in item:
                        subitem *= 1 - wimp_zimp / 200 + (random.random() * wimp_zimp) / 100
                        new_list_of_x.append(subitem)
                    new_x.append(new_list_of_x)
            return new_x

        
    def Add_Angles(self):
        list_1, list_2 = [], []
        for item in self.variables["angle"]:
            list_1.append(item + self.variables["theta"])
            list_2.append(item - self.variables["theta"])
        self.variables["angle"] = list_1 + list_2


    def Do_Calculation(self):
        new_angle = []
        for item in self.variables["angle"]:
            item *= self.Imperfectionate(self.variables["w"], self.variables["wimp"])
            new_angle.append(item)
        self.variables["angle"] = new_angle
        new_x, new_y = [], []
        limit = len(self.x[-1])
        index = 0
        while index < limit:
            new_x.append(self.x[-1][index] + self.variables["size"] * self.Imperfectionate(self.variables["z"], self.variables["zimp"]) * math.sin(self.variables["angle"][2 * index]))
            new_x.append(self.x[-1][index] + self.variables["size"] * self.Imperfectionate(self.variables["z"], self.variables["zimp"]) * math.sin(self.variables["angle"][2 * index + 1]))
            new_y.append(self.y[-1][index] + self.variables["size"] * self.Imperfectionate(self.variables["z"], self.variables["zimp"]) * math.cos(self.variables["angle"][2 * index]))
            new_y.append(self.y[-1][index] + self.variables["size"] * self.Imperfectionate(self.variables["z"], self.variables["zimp"]) * math.cos(self.variables["angle"][2 * index + 1]))
            index += 1
        self.x.append(new_x)
        self.y.append(new_y)
        self.Add_Angles()