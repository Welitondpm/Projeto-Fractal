from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fractal_3d import Fractal3d
from DDD_property_perimeter import PropertyPerimeter
from DDD_property_per_cube import PropertyPerCube
from DDD_property_surface import PropertySurface
from DDD_property_volume import PropertyVolume
import math


class KochTetrahedron(Fractal3d):
    def __init__(self, x = [], y = [], z = [], args = {}):
        Fractal3d.__init__(self, x, y, z)
        default_vars = {"times": 2, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        fig = plt.figure()
        self.sub = fig.add_subplot(1, 1, 1, projection="3d")
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2, 0]]
        self.y = [[(3 ** 0.5 * self.variables["size"] / 2) * -1 / 3, (3 ** 0.5 * self.variables["size"] / 2) * 2 / 3, (3 ** 0.5 * self.variables["size"] / 2) * -1 / 3, 0]]
        self.z = [[0, 0, 0, 0]]
        self.all_x_lists = []
        self.all_y_lists = []
        self.all_z_lists = []
        self.all_triangles_last_iteration = []
        self.newer_x, self.newer_y, self.newer_z = [], [], []


    def Create_Fractal(self):
        self.Initiator()
        self.Do_Calculation()


    def Initiator(self):
        faces = self.Make_Tetrahedron(self.x[0], self.y[0], self.z[0], 0)
        new_x, new_y, new_z = [], [], []
        for face in faces:
            new_x += face[0]
            new_y += face[1]
            new_z += face[2]
            self.Make_Graph(new_x, new_y, new_z)
            self.all_x_lists += [new_x]
            self.all_y_lists += [new_y]
            self.all_z_lists += [new_z]
            new_x, new_y, new_z = [], [], []
        self.x, self.y, self.z = self.all_x_lists[::], self.all_y_lists[::], self.all_z_lists[::]


    def Do_Calculation(self):
        for iteration_number in range(1, self.variables["times"]):
            limit = len(self.x)
            for index in range(limit):
                faces = self.Make_Tetrahedron(self.x[index], self.y[index], self.z[index], iteration_number)
                new_x, new_y, new_z = [], [], []
                for face in faces:
                    new_x += face[0]
                    new_y += face[1]
                    new_z += face[2]
                    self.Make_Graph(new_x, new_y, new_z)
                    self.all_x_lists += [new_x]
                    self.all_y_lists += [new_y]
                    self.all_z_lists += [new_z]
                    new_x, new_y, new_z = [], [], []
            self.x, self.y, self.z = self.all_x_lists[::], self.all_y_lists[::], self.all_z_lists[::]


    def Make_Graph(self, x, y, z, color = "#000000"):
        self.sub.plot(x, y, z, color = color)


    def Make_Tetrahedron(self, base_x, base_y, base_z, iteration_number):
        triangle_x = [base_x[0] + (base_x[1] - base_x[0]) / 2, base_x[0] + (base_x[2] - base_x[0]) / 2, base_x[1] + (base_x[2] - base_x[1]) / 2]
        triangle_y = [base_y[0] + (base_y[1] - base_y[0]) / 2, base_y[0] + (base_y[2] - base_y[0]) / 2, base_y[1] + (base_y[2] - base_y[1]) / 2]
        triangle_z = [base_z[0] + (base_z[1] - base_z[0]) / 2, base_z[0] + (base_z[2] - base_z[0]) / 2, base_z[1] + (base_z[2] - base_z[1]) / 2]
        point_x_1, point_y_1, point_z_1 = triangle_x[0], triangle_y[0], triangle_z[0]
        point_x_2, point_y_2, point_z_2 = triangle_x[1], triangle_y[1], triangle_z[1]
        point_x_3, point_y_3, point_z_3 = triangle_x[2], triangle_y[2], triangle_z[2]
        distance = 0.5 * (((base_x[0] - base_x[1]) ** 2 + (base_y[0] - base_y[1]) ** 2 + (base_z[0] - base_z[1]) ** 2) ** 0.5)
        point_x_4 = ((2.0 ** 1.5) / (3 * distance)) * ((triangle_y[2] - triangle_y[1]) * (triangle_z[1] - triangle_z[0]) - (triangle_y[1] - triangle_y[0]) * (triangle_z[2] - triangle_z[1])) + sum(triangle_x) / 3.0
        point_y_4 = ((2.0 ** 1.5) / (3 * distance)) * ((triangle_z[2] - triangle_z[1]) * (triangle_x[1] - triangle_x[0]) - (triangle_z[1] - triangle_z[0]) * (triangle_x[2] - triangle_x[1])) + sum(triangle_y) / 3.0
        point_z_4 = ((2.0 ** 1.5) / (3 * distance)) * ((triangle_x[2] - triangle_x[1]) * (triangle_y[1] - triangle_y[0]) - (triangle_x[1] - triangle_x[0]) * (triangle_y[2] - triangle_y[1])) + sum(triangle_z) / 3.0
        face_1 = [[point_x_1, point_x_2, point_x_3], [point_y_1, point_y_2, point_y_3], [point_z_1, point_z_2, point_z_3]]
        face_2 = [[point_x_2, point_x_1, point_x_4], [point_y_2, point_y_1, point_y_4], [point_z_2, point_z_1, point_z_4]]
        face_3 = [[point_x_4, point_x_1, point_x_3], [point_y_4, point_y_1, point_y_3], [point_z_4, point_z_1, point_z_3]]
        face_4 = [[point_x_2, point_x_4, point_x_3], [point_y_2, point_y_4, point_y_3], [point_z_2, point_z_4, point_z_3]]
        triangle_1 = [[base_x[0], triangle_x[0], triangle_x[1]], [base_y[0], triangle_y[0], triangle_y[1]], [base_z[0], triangle_z[0], triangle_z[1]]]
        triangle_2 = [[triangle_x[0], base_x[1], triangle_x[2]], [triangle_y[0], base_y[1], triangle_y[2]], [triangle_z[0], base_z[1], triangle_z[2]]]
        triangle_3 = [[triangle_x[1], triangle_x[2], base_x[2]], [triangle_y[1], triangle_y[2], base_y[2]], [triangle_z[1], triangle_z[2], base_z[2]]]
        if iteration_number == 0:
            return (face_1, face_2, face_3, face_4)
        elif iteration_number == self.variables["times"] - 1:
            self.all_triangles_last_iteration += (triangle_1, triangle_2, triangle_3, face_1, face_2, face_3, face_4)
        return (triangle_1, triangle_2, triangle_3, face_2, face_3, face_4)


    def Property_Perimeter(self, value = 10):
        passing = self.variables["size"] / value
        for list in self.all_triangles_last_iteration:
            perimeter = PropertyPerimeter(list[0], list[1], list[2])
            new_x, new_y, new_z = perimeter.Perimeter(passing)
            self.newer_x += new_x
            self.newer_y += new_y
            self.newer_z += new_z
        self.sub.scatter(self.newer_x , self.newer_y, self.newer_z)


    def Property_Surface(self, value = 10):
        all_x_x, all_y_y, all_z_z = [], [], []
        passing = self.variables["size"] / value
        for element in self.all_triangles_last_iteration:
            surface_x, surface_y, surface_z = [], [], []
            all_x, all_y, all_z = [], [], []
            all_x_end, all_y_end, all_z_end = [], [], []
            list_length = len(element[0])
            middle_x = sum(element[0]) / list_length
            middle_y = sum(element[1]) / list_length
            middle_z = sum(element[2]) / list_length
            max_size_line = 0
            perimeter = PropertyPerimeter(element[0], element[1], element[2])
            new_x, new_y, new_z = perimeter.Perimeter(passing)
            for item in range(list_length):
                perimeter = PropertyPerimeter([element[0][item], middle_x], [element[1][item], middle_y], [element[2][item], middle_z])
                new_x, new_y, new_z = perimeter.Perimeter(passing)
                all_x.append(new_x)
                all_y.append(new_y)
                all_z.append(new_z)
                if len(new_x) > max_size_line:
                    max_size_line = len(new_x)
                    line_index = item
            for item in range(len(all_x)):
                difference_x = all_x[item][-1] - all_x[item][0]
                difference_y = all_y[item][-1] - all_y[item][0]
                difference_z = all_z[item][-1] - all_z[item][0]
                distance_x_y_z = (difference_x ** 2 + difference_y ** 2 + difference_z ** 2) ** 0.5
                amount_squares = abs(distance_x_y_z) / max_size_line
                if amount_squares == 0:
                    continue
                perimeter = PropertyPerimeter([all_x[item][-1],  all_x[item][0]], [all_y[item][-1], all_y[item][0]], [all_z[item][-1], all_z[item][0]])
                new_x, new_y, new_z = perimeter.Perimeter(amount_squares)
                all_x_end.append(new_x)
                all_y_end.append(new_y)
                all_z_end.append(new_z)
            if len(all_x_end) != 0:
                for item in range(len(all_x_end[0])):
                    list_x = [all_x_end[0][item], all_x_end[1][item], all_x_end[2][item], all_x_end[0][item]]
                    list_y = [all_y_end[0][item], all_y_end[1][item], all_y_end[2][item], all_y_end[0][item]]
                    list_z = [all_z_end[0][item], all_z_end[1][item], all_z_end[2][item], all_z_end[0][item]]
                    perimeter = PropertyPerimeter(list_x, list_y, list_z)
                    new_x, new_y, new_z = perimeter.Perimeter(passing)
                    surface_x.extend(new_x)
                    surface_y.extend(new_y)
                    surface_z.extend(new_z)
            # self.sub.scatter(surface_x, surface_y, surface_z)
            all_x_x.extend(surface_x)
            all_y_y.extend(surface_y)
            all_z_z.extend(surface_z)
        property_volume = PropertyVolume(x = all_x_x, y = all_y_y, z = all_z_z, show_graph = True, passing = passing)
        property_volume.Row_Verifier()



a = KochTetrahedron(args = {"times": 3})
a.Create_Fractal()
# a.Property_Perimeter(value=30)
# a.Property_Surface(value=30)
# self.sub.scatter([-10,10], [-10,10], [-10,10])
a.Show_Graph()