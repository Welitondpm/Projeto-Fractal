import matplotlib.pyplot as plt


class PropertyPerSquare():
    def __init__(self, x = [], y = [], value = 10):
        self.x = x
        self.y = y
        x_copy = self.x[::]
        y_copy = self.y[::]
        new_x = []
        new_y = []
        minimum_x = min(self.x)
        minimum_y = min(self.y)
        maximum_x = max(self.x)
        maximum_y = max(self.y)
        passing = (maximum_x - minimum_x) / value
        next_x = minimum_x + passing
        previous_x = minimum_x
        next_y = minimum_y + passing
        previous_y = minimum_y
        total_squares = 0
        painted_squares = 0
        square_already_painted = True
        while previous_y < maximum_y:
            if previous_x >= maximum_x:
                previous_x = minimum_x
                next_x = previous_x + passing
                previous_y = next_y
                next_y = previous_y + passing
            else:
                total_squares += 1
                y_position = 0
                square_already_painted = True
                for item in x_copy:
                    if item >= previous_x and item <= next_x:
                        if y_copy[y_position] >= previous_y and y_copy[y_position] <= next_y:
                            if square_already_painted:
                                plt.fill([previous_x, previous_x, next_x, next_x], [previous_y, next_y, next_y, previous_y], color="#ffff00")
                                painted_squares += 1
                                square_already_painted = False
                            else:
                                pass
                        else:
                            new_x.append(item)
                            new_y.append(y_copy[y_position])
                    else:
                        new_x.append(item)
                        new_y.append(y_copy[y_position])
                    y_position += 1
                x_copy = new_x[::]
                y_copy = new_y[::]
                new_x, new_y = [], []
                previous_x = next_x
                next_x = previous_x + passing
        self.total_amount_of_squares = total_squares
        self.amount_of_marcked_squares = painted_squares