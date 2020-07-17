import matplotlib.pyplot as plt
from main import Fractal
import random
import math


class Tree(Fractal):
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y
    

    def Create_Fractal(self, args = {}):
        default_vars = {"times": 12, "size": 50, "angle": 15, "z": 0, "zimp": 0, "w": 0, "wimp": 0}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [[0], [0]]
        self.y = [[0], [self.variables["size"]]]
        self.variables["theta"] = (self.variables["angle"] * math.pi) / 180
        self.variables["angle"] = [self.variables["theta"], -self.variables["theta"]]
        self.variables["z"] = 1 - self.variables["z"] / 100 + self.variables["z"] / 50
        self.variables["w"] = 1 - self.variables["w"] / 100 + self.variables["w"] / 50
        for iteration_number in range(self.variables["times"]):
            self.DoCalculation()
            print("%d of %d" % (iteration_number + 1, self.variables["times"]))
        self.Make_Graph()


    def Make_Graph(self, color = "#000000"):
        disposable_list = []
        list_x, list_of_list_x = [], []
        list_y, list_of_list_y = [], []
        maximum_size = len(self.x[-1])
        for item in self.x:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list[::]
                disposable_list = []
            list_of_list_x.append(item)
        for item in self.y:
            while len(item) < maximum_size:
                for subitem in item:
                    disposable_list.extend((subitem, subitem))
                item = disposable_list[::]
                disposable_list = []
            list_of_list_y.append(item)
        limit = len(self.x)
        for item in range(limit - 1):
            for subitem in range(len(self.x) - 1):
                list_x.append(list_of_list_x[subitem][item])
                list_y.append(list_of_list_y[subitem][item])
            plt.plot(list_x, list_y, color = color)
            list_x, list_y = [], []


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


    def DoCalculation(self):
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


#### Execute Tree
fractalTree = Tree()
fractalTree.Create_Fractal()
fractalTree.Make_Graph()
fractalTree.Show_Graph()