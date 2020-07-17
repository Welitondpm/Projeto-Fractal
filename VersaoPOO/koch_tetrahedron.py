from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from main import Fractal
import math


class Koch_Tetrahedron(Fractal):
    def __init__(self, x = [], y = [], z = []):
        self.x = x
        self.y = y
        self.z = z


    def Create_Fractal(self, args = {}):
        default_vars = {"times": 3, "size": 1}
        self.variables = self.Define_Vars(args, default_vars)
        fig = plt.figure()
        sub = fig.add_subplot(1, 1, 1, projection="3d")
        self.x = [[- self.variables["size"] / 2, 0, self.variables["size"] / 2, 0]]
        self.y = [[(3 ** 0.5 * self.variables["size"] / 2) * -1 / 3, (3 ** 0.5 * self.variables["size"] / 2) * 2 / 3, (3 ** 0.5 * self.variables["size"] / 2) * -1 / 3, 0]]
        self.z = [[0, 0, 0, 0]]
        all_x_lists = []
        all_y_lists = []
        all_z_lists = []
        faces = self.Make_Tetrahedron(self.x[0], self.y[0], self.z[0], 0)
        new_x, new_y, new_z = [], [], []
        for face in faces:
            new_x += face[0]
            new_y += face[1]
            new_z += face[2]
            self.Make_Graph(new_x, new_y, new_z, sub)
            all_x_lists += [new_x]
            all_y_lists += [new_y]
            all_z_lists += [new_z]
            new_x, new_y, new_z = [], [], []
        self.x, self.y, self.z = all_x_lists[::], all_y_lists[::], all_z_lists[::]
        for iteration_number in range(1, self.variables["times"]):
            print(iteration_number)
            limit = len(self.x)
            for index in range(limit):
                faces = self.Make_Tetrahedron(self.x[index], self.y[index], self.z[index], iteration_number)
                new_x, new_y, new_z = [], [], []
                for face in faces:
                    new_x += face[0]
                    new_y += face[1]
                    new_z += face[2]
                    self.Make_Graph(new_x, new_y, new_z, sub)
                    all_x_lists += [new_x]
                    all_y_lists += [new_y]
                    all_z_lists += [new_z]
                    new_x, new_y, new_z = [], [], []
            self.x, self.y, self.z = all_x_lists[::], all_y_lists[::], all_z_lists[::]
        

    def Make_Graph(self, x, y, z, sub, color = "#000000"):
        sub.plot(x, y, z, color = color)


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
        return (triangle_1, triangle_2, triangle_3, face_2, face_3, face_4)


#### Execute Koch Tetrahedron
kochTetrahedron = Koch_Tetrahedron()
kochTetrahedron.Create_Fractal()
kochTetrahedron.Show_Graph()