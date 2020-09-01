from property_perimeter_OOP import PropertyPerimeter
from property_dimension_OOP import Dimension
from property_area_OOP import PropertyArea
import matplotlib.pyplot as plt
from fractal import Fractal
import math


class Flake(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 5, "amount_of_sides": 5, "size": 1, "inwards_out_wards": True}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [0, self.variables["size"]]
        self.y = [0, 0]

    
    def Create_Fractal(self):
        for iteration_number in range(self.variables["times"]):
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.x, self.y = self.Do_Calculation(iteration_number)
        self.Make_Graph()


    def Property_Area(self, value = 10):
        self.Create_Fractal()
        self.passing = (max(self.x) - min(self.x)) / value
        self.property_perimeter = PropertyPerimeter(self.x, self.y)
        self.x, self.y = self.property_perimeter.Perimeter(self.passing)
        self.property_area = PropertyArea(self.x, self.y, value, passing=self.passing)

    
    def Progression_Property_Area(self, value = 10):
        master_x = []
        master_y = []
        for iteration_number in range(self.variables["times"]):
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.x, self.y = self.Do_Calculation(iteration_number)
            self.passing = (max(self.x) - min(self.x)) / value
            self.property_perimeter = PropertyPerimeter(self.x, self.y)
            self.x, self.y = self.property_perimeter.Perimeter(self.passing)
            self.property_area = PropertyArea(self.x, self.y, value, passing=self.passing)
            master_x.append(iteration_number + 1)
            master_y.append(self.property_area.amount_of_marcked_squares)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property area\nFlake of Koch Fractal")
        plt.xlabel("Iteration Number")
        plt.ylabel("Marcked Squares")
        plt.show()


    def Property_Dimension(self, value = 10):
        self.Property_Area(value)
        dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
        self.dimension = dimension_obj.dimension

    
    def Progression_Property_Dimension(self, value = 10):
        master_x = []
        master_y = []
        for iteration_number in range(self.variables["times"]):
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
            self.x, self.y = self.Do_Calculation(iteration_number)
            self.passing = (max(self.x) - min(self.x)) / value
            self.property_perimeter = PropertyPerimeter(self.x, self.y)
            self.x, self.y = self.property_perimeter.Perimeter(self.passing)
            self.property_area = PropertyArea(self.x, self.y, value, passing=self.passing)
            self.dimension_obj = Dimension(self.property_area.amount_of_marcked_squares, self.property_area.passing)
            master_x.append(iteration_number + 1)
            master_y.append(self.dimension_obj.dimension)
        plt.plot(master_x, master_y)
        plt.scatter(master_x, master_y)
        plt.title("Progression of property dimension\nFloco of Koch Fractal")
        plt.xlabel("Iteration Number")
        plt.ylabel("Dimension Fractal")
        plt.show()


    def Make_Graph(self, color = "#000000"):
        plt.plot(self.x, self.y, color = color)


    def Do_Calculation(self, iteration_number):
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
            if iteration_number == 0:
                distance_x_y = 3 * distance_x_y
                new_x = [self.x[index]]
                new_y = [self.y[index]]
            else:
                new_x = [self.x[index] + difference_x / 3]
                new_y = [self.y[index] + difference_y / 3]
            counter_while = 0
            while counter_while < self.variables["amount_of_sides"] - 2:
                new_x += [new_x[-1] + (distance_x_y / 3) * math.cos(current_angle + angle)]
                new_y += [new_y[-1] + (distance_x_y / 3) * math.sin(current_angle + angle)]
                angle -= (math.pi - angle_backup)
                counter_while += 1
            angle = angle_backup
            if iteration_number == 0:
                new_x += [self.x[index + 1]]
                new_y += [self.y[index + 1]]
                new_x += [self.x[index]]
                new_y += [self.y[index]]
                if self.variables["inwards_out_wards"]:
                    new_x = new_x[::-1]
                    new_y = new_y[::-1]
            else:
                new_x += [self.x[index] + 2 * difference_x / 3]
                new_y += [self.y[index] + 2 * difference_y / 3]
                new_x = [self.x[index]] + new_x + [self.x[index + 1]]
                new_y = [self.y[index]] + new_y + [self.y[index + 1]]
            new_final_x.extend(new_x)
            new_final_y.extend(new_y)
        return new_final_x, new_final_y