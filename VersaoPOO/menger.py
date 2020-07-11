from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from main import Fractal


class Menger(Fractal):
    def __init__(self, x, y, z):
        # Fractal.__init__(self, x, y)
        self.x = x
        self.y = y
        self.z = z


    def Create_Fractal(self, args):
        default_vars = {"times": 3, "size": 50}
        variables = self.Define_Vars(args, default_vars)
        fig = plt.figure()
        sub = fig.add_subplot(1, 1, 1, projection="3d")
        interation_number = 0
        self.x = [[0, 0, variables["size"], variables["size"], variables["size"], variables["size"], 0, 0]]
        self.y = [[0, variables["size"], variables["size"], 0, 0, variables["size"], variables["size"], 0]]
        self.z = [[0, 0, 0, 0, variables["size"], variables["size"], variables["size"], variables["size"]]]
        while interation_number < variables["times"]:
            interation_number += 1
            self.Setting_Function()
            print("%d of %d" % (interation_number, variables["times"]))
        self.Make_Graph()


    def Setting_Function(self): 
        new_x, new_y, new_z = [], [], []
        siz = len(self.x)
        for item in range(siz):
            x, y, z = self.Menger_Sponge(self.x[item], self.y[item], self.z[item])
            new_x.extend(x)
            new_y.extend(y)
            new_z.extend(z)
        self.x, self.y, self.z = new_x, new_y, new_z

    
    def Menger_Sponge(self, x, y, z):
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
            new_x, new_y, new_z = self.Make_Cube(self.x[item], self.y[item], self.z[item])
            plt.plot(new_x, new_y, new_z, color = color, linewidth = 0.1)


    def Make_Cube(self, x, y, z):
        new_x = [x[0], x[0], x[1], x[1], x[2], x[2], x[3], x[3], x[0]]
        new_y = [y[0], y[0], y[1], y[1], y[2], y[2], y[3], y[3], y[0]]
        new_z = [z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1], z[0], z[0]]
        return new_x + new_x, new_y + new_y, new_z + [z[0], z[0], z[0], z[-1], z[-1], z[0], z[0], z[-1], z[-1]]


# Execute Menger Sponge
# menger = Menger([], [], [])
# menger.Create_Fractal({"times": 3})
# menger.Show_Graph()


class MengerColorful(Menger):
    def __init__(self, x, y, z):
        # Fractal.__init__(self, x, y)
        self.x = x
        self.y = y
        self.z = z

    
    def Make_Graph(self):
        x_y_z_max = max(self.x[-1])
        limit = len(self.x)
        for item in range(limit):
            new_x, new_y, new_z = self.Make_Cube(self.x[item], self.y[item], self.z[item])
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


# Execute Menger Sponge
mengercolor = MengerColorful([], [], [])
mengercolor.Create_Fractal({"times": 3})
mengercolor.Show_Graph()