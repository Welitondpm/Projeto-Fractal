import matplotlib.pyplot as plt
from main import Fractal


class Sierpinski(Fractal):
    def __init__(self, x, y):
        Fractal.__init__(self, x, y)
        self.x = x
        self.y = y


    def Create_Fractal(self, args):
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


# Execute Sierpinski Triangle
# sierpins = Sierpinski([], [])
# sierpins.Create_Fractal({"times": 5})
# sierpins.Show_Graph()


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

        
    def Create_Fractal(self, args):
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


# Execute Sierpinski Carpet
# carpet = SierpinskiCarpet([], [])
# carpet.Create_Fractal({"times": 5})
# carpet.Show_Graph()