import matplotlib.pyplot as plt


class PropertyPerimeter():
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y


    def Perimeter(self, size_of_side_of_square):
        new_x, new_y = [], []
        for index in range(len(self.x) - 1):
            x_point = self.x[index]
            y_point = self.y[index]
            next_x_point = self.x[index + 1]
            next_y_point = self.y[index + 1]
            difference_x = next_x_point - x_point
            difference_y = next_y_point - y_point
            distance_x_y = (difference_x ** 2 + difference_y ** 2) ** 0.5
            amount_squares = int(distance_x_y / size_of_side_of_square) + 1
            if amount_squares > 0:
                for new_point in range(1, amount_squares + 1):
                    new_x.append(x_point + new_point * difference_x / amount_squares)
                    new_y.append(y_point + new_point * difference_y / amount_squares)
            else:
                if index == 0:
                    new_x.extend((x_point, next_x_point))
                    new_y.extend((y_point, next_y_point))
                else:
                    new_x.append(next_x_point)
                    new_y.append(next_y_point)
        return new_x, new_y