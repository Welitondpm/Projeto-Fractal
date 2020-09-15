from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class CantorSet(Fractal):
    def __init__(self, args = {}):
        default_vars = {"times": 10, "scale": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        Fractal.__init__(self, [[0, self.variables["scale"]]], [[0, 0]])
        self.iteration_number = 0
        self.property_x, self.property_y = [], []
        self.passing = self.variables["scale"] / self.variables["value"]


    def Make_Graph(self):
        limit = len(self.x)
        for item in range(limit):
            plt.plot(self.x[item], self.y[item], color = self.variables["color"], linewidth = 1)


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
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Make_Graph()
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.Make_Graph()


    def Do_Perimeter(self, paint_squares = False):
        limit = len(self.x)
        new_x, new_y = [], []
        for item in range(limit):
            self.property_perimeter = PropertyPerimeter(self.x[item], self.y[item])
            new_x_perimeter, new_y_perimeter = self.property_perimeter.Perimeter(self.passing)
            new_x.extend(new_x_perimeter)
            new_y.extend(new_y_perimeter)
        self.property_square = PropertyPerSquare(new_x, new_y, self.variables["value"], paint_squares)

    
    def Property_Perimeter(self, paint_squares = True):
        self.Create_Fractal()
        self.Do_Perimeter(paint_squares)

    
    def Property_Dimension(self):
        self.Property_Perimeter(paint_squares = False)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, property_perimeter = False, make_graph = True):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.x, self.y = self.Organizing_Function(self.iteration_number)
            print("%d of %d" % (self.iteration_number, self.variables["times"]))
            self.Do_Perimeter()
            self.property_x.append(self.iteration_number)
            if property_perimeter:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if property_perimeter:
            description = {"title": "Progression of property per square\nCantor Set Fractal", "label_x": "Row", "label_y": "Marcked Squares", "label_plot": "Cantor Set"}
        else:
            description = {"title": "Progression of property dimension\nCantor Set Fractal", "label_x": "Row", "label_y": "Dimension Fractal", "label_plot": "Cantor Set"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)