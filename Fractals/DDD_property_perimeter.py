import matplotlib.pyplot as plt


class PropertyPerimeter():
    def __init__(self, x = [], y = [], z = []):
        self.x = x
        self.y = y
        self.z = z


    def Perimeter(self, size_of_side_of_square):
        new_x, new_y, new_z = [], [], []
        for index in range(len(self.x) - 1):
            x_point = self.x[index]
            y_point = self.y[index]
            z_point = self.z[index]
            next_x_point = self.x[index + 1]
            next_y_point = self.y[index + 1]
            next_z_point = self.z[index + 1]
            difference_x = next_x_point - x_point
            difference_y = next_y_point - y_point 
            difference_z = next_z_point - z_point
            distance_x_y_z = (difference_x ** 2 + difference_y ** 2 + difference_z ** 2) ** 0.5
            amount_squares = int(abs(distance_x_y_z) / size_of_side_of_square) + 1
            if amount_squares > 0:
                for new_point in range(1, amount_squares + 1):
                    new_x.append(x_point + new_point * difference_x / amount_squares)
                    new_y.append(y_point + new_point * difference_y / amount_squares)
                    new_z.append(z_point + new_point * difference_z / amount_squares)
            else:
                if index == 0:
                    new_x.extend((x_point, next_x_point))
                    new_y.extend((y_point, next_y_point))
                    new_z.extend((z_point, next_z_point))
                else:
                    new_x.append(next_x_point)
                    new_y.append(next_y_point)
                    new_z.append(next_z_point)
        return new_x, new_y, new_z