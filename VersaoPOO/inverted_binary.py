import matplotlib.pyplot as plt
from main import Fractal


class Inverted_Binary(Fractal):
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y


    def Create_Fractal(self, args = {}):
        default_vars = {"end": 18}
        self.variables = self.Define_Vars(args, default_vars)
        self.variables["end"] = 2 ** self.variables["end"]
        for point_x in range(self.variables["end"]):
            point_y = 0
            if self.Prime_Number(point_x):
                binary_number = self.Binary(point_x)
                decimal_number = self.Decimal(binary_number)
                point_y = point_x - decimal_number
            self.x.append(point_x)
            self.y.append(point_y)
        self.Make_Graph()


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


#### Execute Inverted Binary
# binary = Inverted_Binary()
# binary.Create_Fractal()
# binary.Make_Graph()
# binary.Show_Graph()