from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fractal_3d import Fractal3d


class Menger(Fractal3d):
    def __init__(self, x = [], y = [], z = [], args = {}):
        fig = plt.figure()
        sub = fig.add_subplot(1, 1, 1, projection="3d")
        Fractal3d.__init__(self, x, y, z)
        default_vars = {"times": 3, "size": 50}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [[0, 0, self.variables["size"], self.variables["size"], self.variables["size"], self.variables["size"], 0, 0]]
        self.y = [[0, self.variables["size"], self.variables["size"], 0, 0, self.variables["size"], self.variables["size"], 0]]
        self.z = [[0, 0, 0, 0, self.variables["size"], self.variables["size"], self.variables["size"], self.variables["size"]]]
    

    def Create_Fractal(self):
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()


    def Setting_Function(self): 
        new_x, new_y, new_z = [], [], []
        siz = len(self.x)
        for item in range(siz):
            x, y, z = self.Seed_Aplication(self.x[item], self.y[item], self.z[item])
            new_x.extend(x)
            new_y.extend(y)
            new_z.extend(z)
        self.x, self.y, self.z = new_x, new_y, new_z

    
    def Seed_Aplication(self, x, y, z):
        x_1 = x[0]
        x_2 = x_1 + (x[3] - x[0]) / 3
        x_3 = x_1 + (x[3] - x[0]) * 2 / 3
        x_4 = x[3]
        y_1 = y[0]
        y_2 = y_1 + (y[2] - y[0]) / 3
        y_3 = y_1 + (y[2] - y[0]) * 2 / 3
        y_4 = y[2]
        z_1 = z[0]
        z_2 = z_1 + (z[4] - z[0]) / 3
        z_3 = z_1 + (z[4] - z[0]) * 2 / 3
        z_4 = z[4]
        cube_1_x = [x_1, x_1, x_2, x_2, x_2, x_2, x_1, x_1]
        cube_1_y = [y_1, y_2, y_2, y_1, y_1, y_2, y_2, y_1]
        cube_2_x = [x_2, x_2, x_3, x_3, x_3, x_3, x_2, x_2]
        cube_2_y = cube_1_y
        cube_3_x = [x_3, x_3, x_4, x_4, x_4, x_4, x_3, x_3]
        cube_3_y = cube_1_y
        cube_4_x = cube_1_x
        cube_4_y = [y_2, y_3, y_3, y_2, y_2, y_3, y_3, y_2]
        cube_6_x = cube_3_x
        cube_6_y = cube_4_y
        cube_7_x = cube_1_x
        cube_7_y = [y_3, y_4, y_4, y_3, y_3, y_4, y_4, y_3]
        cube_8_x = cube_2_x
        cube_8_y = cube_7_y
        cube_9_x = cube_6_x
        cube_9_y = cube_7_y
        cube_1_z = [z_1, z_1, z_1, z_1, z_2, z_2, z_2, z_2]
        cube_2_z = [z_2, z_2, z_2, z_2, z_3, z_3, z_3, z_3]
        cube_3_z = [z_3, z_3, z_3, z_3, z_4, z_4, z_4, z_4]
        return (
            (
                cube_1_x, cube_2_x, cube_3_x, cube_4_x, cube_6_x, cube_7_x, cube_8_x, cube_9_x, cube_1_x, cube_3_x,
                cube_7_x, cube_9_x, cube_1_x, cube_2_x, cube_3_x, cube_4_x, cube_6_x, cube_7_x, cube_8_x, cube_9_x
            ),
            (
                cube_1_y, cube_2_y, cube_3_y, cube_4_y, cube_6_y, cube_7_y, cube_8_y, cube_9_y, cube_1_y, cube_3_y,
                cube_7_y, cube_9_y, cube_1_y, cube_2_y, cube_3_y, cube_4_y, cube_6_y, cube_7_y, cube_8_y, cube_9_y
            ),
            (
                cube_1_z, cube_1_z, cube_1_z, cube_1_z, cube_1_z, cube_1_z, cube_1_z, cube_1_z, cube_2_z, cube_2_z,
                cube_2_z, cube_2_z, cube_3_z, cube_3_z, cube_3_z, cube_3_z, cube_3_z, cube_3_z, cube_3_z, cube_3_z
            )
        )


    def Make_Graph(self, color = "#000000"):
        limit = len(self.x)
        for item in range(limit):
            new_x, new_y, new_z = self.Path_Finder(self.x[item], self.y[item], self.z[item])
            plt.plot(new_x, new_y, new_z, color = color, linewidth = 0.1)


    def Path_Finder(self, x, y, z):
        new_x = [x[0], x[0], x[1], x[1], x[2], x[2], x[3], x[3], x[0]]
        new_y = [y[0], y[0], y[1], y[1], y[2], y[2], y[3], y[3], y[0]]
        new_z = [z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1], z[0], z[0]]
        return new_x + new_x, new_y + new_y, new_z + [z[0], z[0], z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1]]


class ColorfulMenger(Menger):
    def __init__(self, x = [], y = [], z = [], args = {}):
        Menger.__init__(self, x, y, z, args)

    
    def Make_Graph(self):
        x_y_z_max = max(self.x[-1])
        limit = len(self.x)
        for item in range(limit):
            new_x, new_y, new_z = self.Path_Finder(self.x[item], self.y[item], self.z[item])
            color_1 = str(hex(int(255 * (new_x[0] / x_y_z_max))))[2:4]
            color_2 = str(hex(int(255 * (new_y[0] / x_y_z_max))))[2:4]
            color_3 = str(hex(int(255 * (new_z[0] / x_y_z_max))))[2:4]
            while len(color_1) < 2:
                color_1 = "0" + color_1
            while len(color_2) < 2:
                color_2 = "0" + color_2
            while len(color_3) < 2:
                color_3 = "0" + color_3
            plt.plot(new_x, new_y, new_z, color = "#" + color_1 + color_2 + color_3, linewidth = 0.1)


class SierpinskiTetrahedron(Menger):
    def __init__(self, x = [], y = [], z = [], args = {}):
        Fractal3d.__init__(self, x, y, z)
        fig = plt.figure()
        sub = fig.add_subplot(1, 1, 1, projection="3d")
        default_vars = {"times": 4, "size": 50}
        self.variables = self.Define_Vars(args, default_vars)
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2, 0]]
        self.y = [[- self.variables["size"] * 3 ** 0.5 / 6, self.variables["size"] * 3 ** 0.5 / 3, - self.variables["size"] * 3 ** 0.5 / 6, 0]]
        self.z = [[- self.variables["size"] * 3 ** 0.5 / 24, - self.variables["size"] * 3 ** 0.5 / 24, - self.variables["size"] * 3 ** 0.5 / 24, self.variables["size"] * 3 ** 0.5 / 12]]
        
        
    def Create_Fractal(self):
        iteration_number = 0
        while iteration_number < self.variables["times"]:
            iteration_number += 1
            self.Setting_Function()
            # print("%d of %d" % (iteration_number, self.variables["times"]))
        self.Make_Graph()


    def Seed_Aplication(self, x, y, z):
        x_1 = x[0]
        x_2 = x_1 + (x[1] - x[0]) / 2
        x_3 = x[1]
        x_4 = x_3 + (x[2] - x[1]) / 2
        x_5 = x[2]
        x_6 = x_1 + (x[2] - x[0]) / 2
        x_8 = (x_1 + x[3]) / 2
        x_9 = (x_3 + x[3]) / 2
        x_10 = (x_5 + x[3]) / 2
        x_11 = x[3]
        y_1 = y[0]
        y_2 = y_1 + (y[1] - y[0]) / 2
        y_3 = y[1]
        y_4 = y_3 + (y[2] - y[1]) / 2
        y_5 = y[2]
        y_6 = y_1 + (y[2] - y[0]) / 2
        y_8 = (y_1 + y[3]) / 2
        y_9 = (y_3 + y[3]) / 2
        y_10 = (y_5 + y[3]) / 2
        y_11 = y[3]
        z_1 = z[0]
        z_2 = z_1 + (z[1] - z[0]) / 2
        z_3 = z[1]
        z_4 = z_3 + (z[2] - z[1]) / 2
        z_5 = z[2]
        z_6 = z_1 + (z[2] - z[0]) / 2
        z_8 = (z_1 + z[3]) / 2
        z_9 = (z_3 + z[3]) / 2
        z_10 = (z_5 + z[3]) / 2
        z_11 = z[3]
        return (
            ((x_1, x_2, x_6, x_8), (x_2, x_3, x_4, x_9), (x_6, x_4, x_5, x_10), (x_8, x_9, x_10, x_11)),
            ((y_1, y_2, y_6, y_8), (y_2, y_3, y_4, y_9), (y_6, y_4, y_5, y_10), (y_8, y_9, y_10, y_11)),
            ((z_1, z_2, z_6, z_8), (z_2, z_3, z_4, z_9), (z_6, z_4, z_5, z_10), (z_8, z_9, z_10, z_11))
        )


    def Path_Finder(self, x, y, z):
        x = [x[0], x[1], x[2], x[0], x[3], x[1], x[2], x[3]]
        y = [y[0], y[1], y[2], y[0], y[3], y[1], y[2], y[3]]
        z = [z[0], z[1], z[2], z[0], z[3], z[1], z[2], z[3]]
        return x, y, z        


class ColorfulSierpinskiTetrahedron(SierpinskiTetrahedron):
    def __init__(self, x = [], y = [], z = [], args = {}):
        SierpinskiTetrahedron.__init__(self, x, y, z, args)

    
    def Make_Graph(self):
        limit = len(self.x)
        for item in range(limit):
            new_x, new_y, new_z = self.Path_Finder(self.x[item], self.y[item], self.z[item])
            number = ((new_x[0] ** 2 + new_y[0] ** 2 + new_z[0] ** 2) ** 0.5) / ((self.variables["size"] * 3 ** 0.5 / 2) * 2 / 3) * 255
            color = str(hex(int(255 - number)))
            if len(color) == 4 and color[2] != "x":
                color = color[2:]
            else:
                color = "0" + color[-1]
            plt.plot(new_x, new_y, new_z, color = "#" + color + color + color, linewidth = 0.5)