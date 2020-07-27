import matplotlib.pyplot as plt
from fractal import Fractal


class HilbertCurve(Fractal):
    def __init__(self, x = [], y = [], args = {}):
        Fractal.__init__(self, x, y)
        default_vars = {"times": 5, "scale": 1}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [0, 0, self.variables["scale"], self.variables["scale"]]
        self.y = [self.variables["scale"], 0, 0, self.variables["scale"]]
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Do_Calculation(iteration_number)
            print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()     


    def Make_Graph(self, color = "#000000"):
        plt.plot(self.x, self.y, color = color)


    def Reduces_Size(self, iteration_number):
        new_x, new_y = [], []
        for item in self.x:
            new_x.append(item / ((2 ** (iteration_number + 1) - 1) / ((2 ** (iteration_number + 1) - 2) / 2)))
        for item in self.y:
            new_y.append(item / ((2 ** (iteration_number + 1) - 1) / ((2 ** (iteration_number + 1) - 2) / 2)))
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


    def Do_Calculation(self, iteration_number):
        size = self.x[-1] - self.x[0]
        disposable_list = []
        new_x, new_y = [], []
        self.Reduces_Size(iteration_number)
        addition = size / (2 ** (iteration_number + 1) - 1)
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