import matplotlib.pyplot as plt
from main import Fractal
from random import randint


class Sierpinski(Fractal):
    def __init__(self, x, y):
        Fractal.__init__(self, x, y)
        self.x = x
        self.y = y


    def Create_Fractal(self, args = {}):
        default_vars = {"times": 8, "size": 50}
        variables = self.Define_Vars(args, default_vars)
        interation_number = 0
        self.x = [[- variables["size"] / 2, 0, variables["size"] / 2]]
        self.y = [[- variables["size"] * 3 ** 0.5 / 6, variables["size"] * 3 ** 0.5 / 3, - variables["size"] * 3 ** 0.5 / 6]]
        while interation_number < variables["times"]:
            interation_number += 1
            self.Setting_Function()
            print("%d of %d" % (interation_number, variables["times"]))
        self.Triangle_Picker()
        self.Make_Graph()


    def Setting_Function(self): 
        new_x, new_y = [], []
        siz = len(self.x)
        for item in range(siz):
            x, y = self.Sierpinski_Triangle(self.x[item], self.y[item])
            new_x.extend(x)
            new_y.extend(y)
        self.x, self.y = new_x, new_y # Suposto Fatiamento Necessário

    
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
    def __init__(self, x, y):
        Sierpinski.__init__(self, x, y)
        self.x = x
        self.y = y

    
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
        default_vars = {"times": 4, "size": 50}
        variables = self.Define_Vars(args, default_vars)
        interation_number = 0
        self.x = [[0, 0, variables["size"], variables["size"]]]
        self.y = [[0, variables["size"], variables["size"], 0]]
        while interation_number < variables["times"]:
            interation_number += 1
            self.Setting_Function()
            print("%d of %d" % (interation_number, variables["times"]))
        self.Make_Graph()


class ArrowHead(Fractal):
    def __init__(self, x = [[0, 1]], y = [[0, 0]]):
        self.x = x
        self.y = y


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

    
    def Create_Fractal(self, args = {}):
        default_vars = {"times": 12}
        self.variables = self.Define_Vars(args, default_vars)
        for interation_number in range(1, self.variables["times"] + 1):
            self.Make_Triangle()
            print("%d de %d" % (interation_number, self.variables["times"]))
        new_x, new_y = [], []
        index = 0
        limit = len(self.x)
        while index < limit:
            new_x.extend(self.x[index])
            new_y.extend(self.y[index])
            index += 1
        self.x, self.y = new_x, new_y


    def Make_Graph(self, color = "#000000"):
        plt.plot(self.x, self.y, color = color)


class Chaotic_Triangle(Fractal):
    def __init__(self, x = [0, 50, -50], y = [7500 ** 0.5, 0, 0]):
        self.x = x
        self.y = y


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


    def Create_Fractal(self, args = {}):
        default_vars = {"times": 1000000, "value": 2}
        self.variables = self.Define_Vars(args, default_vars)
        self.Make_Chaotic_Triangle()


    def Make_Graph(self, color = "#000000"):
        plt.scatter(self.x, self.y, color = color, s=0.01)


class Sierpinski_Pascal(Fractal):
    def __init__(self):
        self.string_line = ""


    def Create_Fractal(self, args = {}):
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


#### Execute Sierpinski Triangle
# sierpins = Sierpinski([], [])
# sierpins.Create_Fractal({"times": 5})
# sierpins.Show_Graph()


#### Execute Sierpinski Carpet
# carpet = SierpinskiCarpet([], [])
# carpet.Create_Fractal({"times": 5})
# carpet.Show_Graph()


#### Execute Sierpinski Carpet
# arrow = ArrowHead()
# arrow.Create_Fractal()
# arrow.Make_Graph()
# arrow.Show_Graph()


#### Execute Chaotic Sierpinski
# chaotic = Chaotic_Triangle()
# chaotic.Create_Fractal()
# chaotic.Make_Graph()
# chaotic.Show_Graph()


#### Execute Sierpinski Base Pascal
# basePascal = Sierpinski_Pascal()
# basePascal.Create_Fractal()