import matplotlib.pyplot as plt
from main import Fractal


class Mandlebrot(Fractal):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def pre_calculation(self):
        list_of_lists_x = []
        list_of_lists_y = []
        for item in range(self.variables["amount_of_colors"]):
            list_of_lists_x.append([])
            list_of_lists_y.append([])
        self.universe_set_of_real_numbers = range(- self.variables["real_numbers"] * self.variables["density"], self.variables["real_numbers"] * self.variables["density"])
        self.universe_set_of_imaginary_numbers = range(- self.variables["imaginary_numbers"] * self.variables["density"], self.variables["imaginary_numbers"] * self.variables["density"])
        self.dot_size = 1000 / self.variables["density"]
        self.x, self.y = list_of_lists_x, list_of_lists_y
        self.limit = 1 / self.variables["depth"]

    
    def Go_Through_Universe(self):
        for real_number in self.universe_set_of_real_numbers:     
            percent = round(50 + 100 * real_number / len(self.universe_set_of_real_numbers), 2)
            print(percent, " %")
            real_number /= self.variables["density"]
            for imaginary_number in self.universe_set_of_imaginary_numbers:
                imaginary_number /= self.variables["density"]
                z = complex(0, 0)
                c = complex(real_number, imaginary_number)
                for counter in range(self.variables["depth"]):
                    z = z * z + c
                    if abs(z) > self.variables["depth"]:
                        self.coloring_sepator(counter, real_number, imaginary_number)
                        break
                    elif abs(z) < self.limit:
                        self.x[-1].append(real_number)
                        self.y[-1].append(imaginary_number)


    def coloring_sepator(self, counter, real_number, imaginary_number):
        counter2 = 1
        while counter2 < self.variables["amount_of_colors"]:
            if counter < self.variables["depth"] / (2 ** counter2):
                self.x[counter2].append(real_number)
                self.y[counter2].append(imaginary_number)
            counter2 += 1


    def define_colors_unique(self):
        limit = len(self.x)
        for item in range(limit):
            color = (str(hex(int(16777216 * item // limit)))[2:])
            while len(color) < 6:
                color = '0' + color
            color = "#" + color
            plt.scatter(self.x[item], self.y[item], s=self.dot_size, color = color)


    def define_colors_multi(self):
        limit = len(self.x)
        for item in range(limit):
            R, G, B = 0, 0, 0
            if item <= limit / 6:
                R, G, B = 255 * 6 * item / limit, 0, 0
            elif item <= limit / 3:
                R, G, B = 255, 255 * 6 * item / limit, 0
            elif item <= limit / 2:
                R, G, B = 255 - (255 * 6 * item / limit), 255, 0
            elif item <= limit * 2 / 3:
                R, G, B = 0, 255, 255 * 6 * item / limit
            elif item <= limit * 5 / 6:
                R, G, B = 0, 255 - (255 * 6 * item / limit), 255
            else:
                R, G, B = 255 * 6 * item / limit, 0, 255
            R, G, B = str(hex(int(R)))[2:], str(hex(int(G)))[2:], str(hex(int(B)))[2:]
            while len(R) < 2:
                R = '0' + R
            while len(G) < 2:
                G = '0' + G
            while len(B) < 2:
                B = '0' + B
            while len(R) > 2:
                R = R[1:]
            while len(G) > 2:
                G = G[1:]
            while len(B) > 2:
                B = B[1:]
            color = '#' + R + G + B
            plt.scatter(self.x[item], self.y[item], s=self.dot_size, color = color)


    def Create_Fractal(self, args):
        default_vars = {"depth": 1000, "real_numbers": 2, "imaginary_numbers": 2, "density": 100, "amount_of_colors": 12}
        self.variables = self.Define_Vars(args, default_vars)
        self.pre_calculation()
        self.Go_Through_Universe()


class Harmonic_Mandlebrot(Mandlebrot):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def coloring_sepator(self, counter, real_number, imaginary_number):
        counter2 = 2
        while counter2 < self.variables["amount_of_colors"]:
            if counter < self.variables["depth"] / counter2:
                self.x[counter2].append(real_number)
                self.y[counter2].append(imaginary_number)
            counter2 += 1


class Segmented_Mandlebrot(Mandlebrot):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def coloring_sepator(self, counter, real_number, imaginary_number):
        counter2 = self.variables["amount_of_colors"]
        while counter2 >= 1:
            if counter < self.variables["depth"] / counter2:
                self.x[counter2 - 1].append(real_number)
                self.y[counter2 - 1].append(imaginary_number)
                counter2 -= 1
                continue
            counter2 -= 1


# Execute Logarithmic Mandlebrot 
# mandlebort = Mandlebrot([], [])
# mandlebort.Create_Fractal({"amount_of_colors": 12})
# mandlebort.define_colors_unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandlebort.define_colors_multi()      ## Atenção nunca execute essa linha junto com superior
# mandlebort.Show_Graph()


# Execute Harmonic Mandlebrot
# mandlebort = Harmonic_Mandlebrot([], [])
# mandlebort.Create_Fractal({"depth": 100, "real_numbers": 2, "imaginary_numbers": 2, "density": 200})
# mandlebort.define_colors_unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandlebort.define_colors_multi()      ## Atenção nunca execute essa linha junto com superior
# mandlebort.Show_Graph()


# Execute Segmented Mandlebrot
# mandlebort = Segmented_Mandlebrot([], [])
# mandlebort.Create_Fractal({"depth": 100, "real_numbers": 2, "imaginary_numbers": 2, "density": 200})
# mandlebort.define_colors_unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandlebort.define_colors_multi()      ## Atenção nunca execute essa linha junto com superior
# mandlebort.Show_Graph()