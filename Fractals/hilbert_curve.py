from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal


class HilbertCurve(Fractal):
    def __init__(self, args = {}):
        default_vars = {"times": 5, "scale": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        x = [0, 0, self.variables["scale"], self.variables["scale"]]
        y = [self.variables["scale"], 0, 0, self.variables["scale"]]
        Fractal.__init__(self, x, y)
        self.iteration_number = 0
        self.property_x, self.property_y = [], []
        
        
    def Create_Fractal(self):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Do_Calculation()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
        self.Make_Graph()


    def Do_Perimeter(self, paint_squares = False):
        self.passing = (max(self.x) - min(self.x)) / self.variables["value"]
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(self.passing)
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)


    def First_Property(self, paint_squares = True):
        self.Create_Fractal()
        self.Do_Perimeter(paint_squares)

    
    def Property_Dimension(self):
        self.First_Property()
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, first_property = False, make_graph = True):
        while self.iteration_number < self.variables["times"]:
            self.iteration_number += 1
            self.Do_Calculation()
            # print("%d of %d" % (self.iteration_number, self.variables["times"]))
            self.Do_Perimeter()
            self.property_x.append(self.iteration_number)
            if first_property:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if first_property:
            description = {"title": "Progression of property perimeter\nHilbert Curve Fractal", "label_x": "Iteration", "label_y": "Marcked Squares", "label_plot": "Hilbert Curve"}
        else:
            description = {"title": "Progression of property dimension\nHilbert Curve Fractal", "label_x": "Iteration", "label_y": "Dimension Fractal", "label_plot": "Hilbert Curve"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


    def Make_Graph(self):
        plt.plot(self.x, self.y, color = self.variables["color"])


    def Reduces_Size(self):
        new_x, new_y = [], []
        for item in self.x:
            new_x.append(item / ((2 ** (self.iteration_number + 1) - 1) / ((2 ** (self.iteration_number + 1) - 2) / 2)))
        for item in self.y:
            new_y.append(item / ((2 ** (self.iteration_number + 1) - 1) / ((2 ** (self.iteration_number + 1) - 2) / 2)))
        self.x, self.y = new_x, new_y


    def Rotate_Counterclockwise(self):
        new_x, new_y = [self.x[0]], [self.y[0]]
        limit = len(self.x)
        for item in range(1, limit):
            new_x.append(new_x[-1] + self.y[-item] - self.y[-item - 1])
            new_y.append(new_y[-1] + self.x[-item] - self.x[-item - 1])
        return new_x, new_y


    def Rotate_Clockwise(self):
        new_x, new_y = [self.x[-1]], [self.y[-1]]
        limit = len(self.x)
        for item in range(1, limit):
            new_x.append(new_x[-1] + self.y[-item - 1] - self.y[-item])
            new_y.append(new_y[-1] - self.x[-item - 1] + self.x[-item])
        return new_x, new_y


    def Do_Calculation(self):
        size = self.x[-1] - self.x[0]
        disposable_list = []
        new_x, new_y = [], []
        self.Reduces_Size()
        addition = size / (2 ** (self.iteration_number + 1) - 1)
        x_3, y_3 = self.Rotate_Counterclockwise()
        x_4, y_4 = self.Rotate_Clockwise()
        for item in self.x:
            disposable_list.append(item + addition + (self.x[-1] - self.x[0]))
        x_2 = disposable_list[::]
        disposable_list = []
        for item in x_4:
            disposable_list.append(item + addition + (self.x[-1] - self.x[0]))
        x_4 = disposable_list[::]
        disposable_list = []
        for item in y_3:
            disposable_list.append(item + addition)
        y_3 = disposable_list[::]
        disposable_list = []
        for item in y_4:
            disposable_list.append(item + addition)
        y_4 = disposable_list[::]
        disposable_list = []
        for item in [x_3[::-1], self.x, x_2, x_4]:
            new_x.extend(item)
        for item in [y_3[::-1], self.y, self.y, y_4]:
            new_y.extend(item)
        self.x, self.y = new_x, new_y