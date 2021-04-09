from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class PropertyPerCube():
    def __init__(self, x = [], y = [], z = [], value = 10):
        self.x = x
        self.y = y
        self.z = z
        self.x_copy = self.x[::]
        self.y_copy = self.y[::]
        self.z_copy = self.z[::]
        self.new_x = []
        self.new_y = []
        self.new_z = []
        self.minimum_x = min(self.x)
        self.minimum_y = min(self.y)
        self.minimum_z = min(self.z)
        self.maximum_x = max(self.x)
        self.maximum_y = max(self.y)
        self.maximum_z = max(self.z)
        self.passing = (self.maximum_x - self.minimum_x) / value
        self.next_x = self.minimum_x + self.passing
        self.previous_x = self.minimum_x
        self.next_y = self.minimum_y + self.passing
        self.previous_y = self.minimum_y
        self.next_z = self.minimum_z + self.passing
        self.previous_z = self.minimum_z
        self.total_squares = 0
        self.painted_cubes = 0
        self.cube_already_painted = True
        self.Row_Verifier()
        

    def Row_Verifier(self):
        while self.previous_y < self.maximum_y:
            if self.previous_x >= self.maximum_x:
                self.previous_x = self.minimum_x
                self.next_x = self.previous_x + self.passing
                self.previous_z = self.next_z
                self.next_z = self.previous_z + self.passing
            elif self.previous_z >= self.maximum_z:
                self.previous_x = self.minimum_x
                self.next_x = self.previous_x + self.passing
                self.previous_z = self.minimum_z
                self.next_z = self.previous_z + self.passing
                self.previous_y = self.next_y
                self.next_y = self.previous_y + self.passing
            else:
                self.total_squares += 1
                self.z_y_position = 0
                self.cube_already_painted = True
                self.List_Updater()
                self.x_copy = self.new_x[::]
                self.y_copy = self.new_y[::]
                self.z_copy = self.new_z[::]
                self.new_x, self.new_y, self.new_z = [], [], []
                self.previous_x = self.next_x
                self.next_x = self.previous_x + self.passing
        self.total_amount_of_squares = self.total_squares
        self.amount_of_marcked_squares = self.painted_cubes

    
    def List_Updater(self):
        for item in self.x_copy:
            if (item >= self.previous_x and item <= self.next_x and
                self.z_copy[self.z_y_position] >= self.previous_z and self.z_copy[self.z_y_position] <= self.next_z and
                self.y_copy[self.z_y_position] >= self.previous_y and self.y_copy[self.z_y_position] <= self.next_y
            ):
                if self.cube_already_painted:
                    plt.plot(
                        [self.previous_x, self.previous_x, self.next_x, self.next_x, self.previous_x, self.previous_x, self.next_x, self.next_x, self.next_x, self.next_x, self.previous_x, self.previous_x, self.previous_x, self.previous_x, self.previous_x, self.next_x, self.next_x],
                        [self.previous_y, self.previous_y, self.previous_y, self.previous_y, self.previous_y, self.next_y, self.next_y, self.previous_y, self.previous_y, self.next_y, self.next_y, self.previous_y, self.next_y, self.next_y, self.next_y, self.next_y, self.next_y],
                        [self.previous_z, self.next_z, self.next_z, self.previous_z, self.previous_z, self.previous_z, self.previous_z, self.previous_z, self.next_z, self.next_z, self.next_z, self.next_z, self.next_z, self.previous_z, self.previous_z, self.previous_z, self.next_z],
                        color="#ff5300"
                    )
                    self.painted_cubes += 1
                    self.cube_already_painted = False
                else:
                    pass
            else:
                self.new_x.append(item)
                self.new_y.append(self.y_copy[self.z_y_position])
                self.new_z.append(self.z_copy[self.z_y_position])
            self.z_y_position += 1