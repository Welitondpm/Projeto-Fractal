from DD_property_per_square import PropertyPerSquare
from DD_property_perimeter import PropertyPerimeter
from property_dimension import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class DragonCurve(Fractal):
    def __init__(self, args = {}):
        default_vars = {"times": 10, "scale": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        Fractal.__init__(self, [0, self.variables["scale"]], [0, 0])
        self.iteration_number = 0
        self.property_x, self.property_y = [], []

    
    def Create_Fractal(self):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Do_Calculation()
            if self.iteration_number > 2:
                self.Scale_Corrector()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.Make_Graph()

    
    def Do_Perimeter(self, paint_squares = False):
        self.passing = (max(self.x) - min(self.y)) / self.variables["value"]
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(self.passing)
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)

    
    def First_Property(self, paint_squares = True):
        self.Create_Fractal()
        self.Do_Perimeter(paint_squares)

    
    def Property_Dimension(self):
        self.First_Property(paint_squares = False)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension


    def Progression_Property(self, first_property = False, make_graph = True):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Do_Calculation()
            if self.iteration_number > 2:
                self.Scale_Corrector()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
            self.Do_Perimeter(False)
            self.property_x.append(self.iteration_number)
            if first_property:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property perimeter\nDragon Curve Fractal", "label_x": "Iteration", "label_y": "Marcked Squares", "label_plot": "Dragon Curve"}
        else:
            description = {"title": "Progression of property dimension\nDragon Curve Fractal", "label_x": "Iteration", "label_y": "Dimension Fractal", "label_plot": "Dragon Curve"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


    def Make_Graph(self):
        plt.plot(self.x, self.y, color = self.variables["color"])


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