import matplotlib.pyplot as plt


class PropertyPerSquare():
    def __init__(self, x = [], y = [], value = 10, paint_squares = False):
        self.x = x
        self.y = y
        self.x_copy = self.x[::]
        self.y_copy = self.y[::]
        self.new_x = []
        self.new_y = []
        self.minimum_x = min(self.x)
        self.minimum_y = min(self.y)
        self.maximum_x = max(self.x)
        self.maximum_y = max(self.y)
        if self.minimum_y == self.maximum_y:
            self.maximum_y += 1 / 10
        self.paint_squares = paint_squares
        self.passing = (self.maximum_x - self.minimum_x) / value
        self.next_x = self.minimum_x + self.passing
        self.previous_x = self.minimum_x
        self.next_y = self.minimum_y + self.passing
        self.previous_y = self.minimum_y
        self.total_squares = 0
        self.painted_squares = 0
        self.square_already_painted = True
        self.Row_Verifier()


    def Row_Verifier(self):
        while self.previous_y < self.maximum_y:
            if self.previous_x >= self.maximum_x:
                self.previous_x = self.minimum_x
                self.next_x = self.previous_x + self.passing
                self.previous_y = self.next_y
                self.next_y = self.previous_y + self.passing
            else:
                self.total_squares += 1
                self.y_position = 0
                self.square_already_painted = True
                self.List_Updater()
                self.x_copy = self.new_x[::]
                self.y_copy = self.new_y[::]
                self.new_x, self.new_y = [], []
                self.previous_x = self.next_x
                self.next_x = self.previous_x + self.passing
        self.total_amount_of_squares = self.total_squares
        self.amount_of_marcked_squares = self.painted_squares

            
    def List_Updater(self):
        for item in self.x_copy:
            if (item >= self.previous_x and item <= self.next_x and
                self.y_copy[self.y_position] >= self.previous_y and self.y_copy[self.y_position] <= self.next_y
            ):
                if self.square_already_painted:
                    if self.paint_squares:
                        self.fig = plt.fill([self.previous_x, self.previous_x, self.next_x, self.next_x], [self.previous_y, self.next_y, self.next_y, self.previous_y], color="#ffff00", alpha=0.3)
                    else:
                        pass
                    self.painted_squares += 1
                    self.square_already_painted = False
                else:
                    pass
            else:
                self.new_x.append(item)
                self.new_y.append(self.y_copy[self.y_position])
            self.y_position += 1