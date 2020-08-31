import matplotlib.pyplot as plt
from property_perimeter_OOP import PropertyPerimeter


class PropertyArea():
    def __init__(self, x = [], y = [], value = 10, show_graph = False, passing = 1000):
        self.x = x
        self.y = y
        minimum_x = min(self.x)
        maximum_x = max(self.x)
        self.passing = passing
        # self.passing = (maximum_x - minimum_x) / value
        # perimeter = PropertyPerimeter(self.x, self.y)
        # self.x, self.y = perimeter.Perimeter(self.passing)
        x_copy = self.x[::]
        y_copy = self.y[::]
        new_x = []
        new_y = []
        minimum_y = min(self.y)
        maximum_y = max(self.y)
        next_x = minimum_x + self.passing
        previous_x = minimum_x
        next_y = minimum_y + self.passing
        previous_y = minimum_y
        total_squares = 0
        painted_squares = 0
        area_squares = 0
        square_already_painted = True
        toggle_painted_squares = False
        previous_squares = True
        while previous_y <= maximum_y:
            if previous_x >= maximum_x:
                toggle_painted_squares = False
                previous_squares = True
                previous_x = minimum_x
                next_x = previous_x + self.passing
                previous_y = next_y
                next_y = previous_y + self.passing
            else:
                total_squares += 1
                y_position = 0
                empty_previous_squares = True
                square_already_painted = True
                prevents_toggle_redundant = True
                if toggle_painted_squares:
                    area_squares += 1
                    prevents_toggle_redundant = False
                    if show_graph:
                        plt.fill([previous_x, previous_x, next_x, next_x], [previous_y, next_y, next_y, previous_y], color="#00ff00")
                    else:
                        pass
                for item in x_copy:
                    if item >= previous_x and item <= next_x:
                        if y_copy[y_position] >= previous_y and y_copy[y_position] <= next_y:
                            if square_already_painted:
                                if previous_squares and not toggle_painted_squares:
                                    toggle_painted_squares = True
                                elif previous_squares and toggle_painted_squares:
                                    toggle_painted_squares = False
                                previous_squares = False
                                empty_previous_squares = False
                                if prevents_toggle_redundant:
                                    if show_graph:
                                        plt.fill([previous_x, previous_x, next_x, next_x], [previous_y, next_y, next_y, previous_y], color="#ffff00")
                                    else:
                                        pass
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
                if empty_previous_squares:
                    previous_squares = True
                x_copy = new_x[::]
                y_copy = new_y[::]
                new_x, new_y = [], []
                previous_x = next_x
                next_x = previous_x + self.passing
        self.total_amount_of_squares = total_squares
        self.amount_of_marcked_squares = painted_squares + area_squares