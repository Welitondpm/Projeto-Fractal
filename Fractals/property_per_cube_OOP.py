from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class PropertyPerCube():
    def __init__(self, x = [], y = [], z = [], value = 10):
        self.x = x
        self.y = y
        self.z = z
        x_copy = self.x[::]
        y_copy = self.y[::]
        z_copy = self.z[::]
        new_x = []
        new_y = []
        new_z = []
        minimum_x = min(self.x)
        minimum_y = min(self.y)
        minimum_z = min(self.z)
        maximum_x = max(self.x)
        maximum_y = max(self.y)
        maximum_z = max(self.z)
        passing = (maximum_x - minimum_x) / value
        next_x = minimum_x + passing
        previous_x = minimum_x
        next_y = minimum_y + passing
        previous_y = minimum_y
        next_z = minimum_z + passing
        previous_z = minimum_z
        total_squares = 0
        painted_cubes = 0
        cube_already_painted = True
        while previous_y < maximum_y:
            if previous_x >= maximum_x:
                previous_x = minimum_x
                next_x = previous_x + passing
                previous_z = next_z
                next_z = previous_z + passing
            elif previous_z >= maximum_z:
                previous_x = minimum_x
                next_x = previous_x + passing
                previous_z = minimum_z
                next_z = previous_z + passing
                previous_y = next_y
                next_y = previous_y + passing
            else:
                total_squares += 1
                z_y_position = 0
                cube_already_painted = True
                for item in x_copy:
                    if item >= previous_x and item <= next_x:
                        if z_copy[z_y_position] >= previous_z and z_copy[z_y_position] <= next_z:
                            if y_copy[z_y_position] >= previous_y and y_copy[z_y_position] <= next_y:
                                if cube_already_painted:
                                    plt.plot([previous_x, previous_x, next_x, next_x, previous_x, previous_x, next_x, next_x, next_x, next_x, previous_x, previous_x, previous_x, previous_x, previous_x, next_x, next_x], [previous_y, previous_y, previous_y, previous_y, previous_y, next_y, next_y, previous_y, previous_y, next_y, next_y, previous_y, next_y, next_y, next_y, next_y, next_y], [previous_z, next_z, next_z, previous_z, previous_z, previous_z, previous_z, previous_z, next_z, next_z, next_z, next_z, next_z, previous_z, previous_z, previous_z, next_z], color="#ff5300")
                                    painted_cubes += 1
                                    cube_already_painted = False
                                else:
                                    pass
                            else:
                                new_x.append(item)
                                new_y.append(y_copy[z_y_position])
                                new_z.append(z_copy[z_y_position])
                        else:
                            new_x.append(item)
                            new_y.append(y_copy[z_y_position])
                            new_z.append(z_copy[z_y_position])
                    else:
                        new_x.append(item)
                        new_y.append(y_copy[z_y_position])
                        new_z.append(z_copy[z_y_position])
                    z_y_position += 1
                x_copy = new_x[::]
                y_copy = new_y[::]
                z_copy = new_z[::]
                new_x, new_y, new_z = [], [], []
                previous_x = next_x
                next_x = previous_x + passing
        self.total_amount_of_squares = total_squares
        self.amount_of_marcked_squares = painted_cubes