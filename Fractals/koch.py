from property_per_square_OOP import PropertyPerSquare
from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
import matplotlib.pyplot as plt
from fractal import Fractal
import math


class Koch(Fractal):
    def __init__(self, args = {}):
        default_vars = {"times": 5, "amount_of_sides": 3, "size": 1, "color": "#000000", "value": 10}
        self.variables = self.Define_Vars(args, default_vars)
        Fractal.__init__(self, [0, self.variables["size"]], [0, 0])
        self.property_x, self.property_y = [], []


    def Create_Fractal(self, property_dimension = False):
        for iteration_number in range(self.variables["times"]):
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.x, self.y = self.Do_Calculation()
        if not property_dimension:
            self.Make_Graph()

    
    def Do_Perimeter(self, paint_squares = False):
        passing = self.variables["size"] / self.variables["value"]
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(passing)
        self.property_square = PropertyPerSquare(self.x, self.y, self.variables["value"], paint_squares)

    
    def Property_Perimeter(self, paint_squares = True, property_dimension = False):
        self.Create_Fractal(property_dimension)
        self.Do_Perimeter(paint_squares)

    
    def Property_Dimension(self):
        self.Property_Perimeter(paint_squares = False, property_dimension = True)
        dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property(self, property_perimeter = False, make_graph = True):
        for iteration_number in range(self.variables["times"]):
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.x, self.y = self.Do_Calculation()
            self.Do_Perimeter()
            self.property_x.append(iteration_number + 1)
            if property_perimeter:
                self.property_y.append(self.property_square.amount_of_marcked_squares)
            else:
                self.dimension_obj = Dimension(self.property_square.amount_of_marcked_squares, self.property_square.passing)
                self.property_y.append(self.dimension_obj.dimension)
        if property_perimeter:
            description = {"title": "Progression of property perimeter\nKoch Curve Fractal", "label_x": "Iteration", "label_y": "Marcked Squares", "label_plot": "Koch Curve"}
        else:
            description = {"title": "Progression of property dimension\nKoch Curve Fractal", "label_x": "Iteration", "label_y": "Dimension Fractal", "label_plot": "Koch Curve"}
        self.Assemble_Graph(self.property_x, self.property_y, description["title"], description["label_x"], description["label_y"], description["label_plot"], make_graph)


    def Make_Graph(self):
        plt.plot(self.x, self.y, color = self.variables["color"])


    def Do_Calculation(self):
        sum_of_integer_angles = 180 * (self.variables["amount_of_sides"] - 2)
        angle = sum_of_integer_angles / self.variables["amount_of_sides"] * math.pi / 180
        angle_backup = angle
        new_final_x, new_final_y = [], []
        limit = len(self.x) - 1
        for index in range(limit):
            difference_x = self.x[index + 1] - self.x[index]
            difference_y = self.y[index + 1] - self.y[index]
            distance_x_y = (difference_x ** 2 + difference_y ** 2) ** 0.5
            if difference_x < 0:
                distance_x_y *= -1
            if difference_x != 0:
                current_angle = math.atan(difference_y / difference_x)
            elif difference_y > 0:
                current_angle = math.pi / 2
            elif difference_y < 0:
                current_angle = 3 * math.pi / 2
            else:
                continue
            new_x = [self.x[index] + difference_x / 3]
            new_y = [self.y[index] + difference_y / 3]
            counter_while = 0
            while counter_while < self.variables["amount_of_sides"] - 2:
                new_x += [new_x[-1] + (distance_x_y / 3) * math.cos(current_angle + angle)]
                new_y += [new_y[-1] + (distance_x_y / 3) * math.sin(current_angle + angle)]
                angle -= (math.pi - angle_backup)
                counter_while += 1
            angle = angle_backup
            new_x += [self.x[index] + 2 * difference_x / 3]
            new_y += [self.y[index] + 2 * difference_y / 3]
            new_x = [self.x[index]] + new_x + [self.x[index + 1]]
            new_y = [self.y[index]] + new_y + [self.y[index + 1]]
            new_final_x.extend(new_x)
            new_final_y.extend(new_y)
        return new_final_x, new_final_y