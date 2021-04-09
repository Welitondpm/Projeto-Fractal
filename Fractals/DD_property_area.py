import matplotlib.pyplot as plt


class PropertyArea():
    def __init__(self, x = [], y = [], show_graph = False, passing = 1):
        self.x = x
        self.y = y
        self.minimum_x = min(self.x)
        self.maximum_x = max(self.x)
        self.minimum_y = min(self.y)
        self.maximum_y = max(self.y)
        self.x_copy = self.x[::]
        self.y_copy = self.y[::]
        self.new_x = []
        self.new_y = []
        self.show_graph = show_graph
        self.passing = passing
        self.previous_x = self.minimum_x
        self.previous_y = self.minimum_y
        self.next_x = self.minimum_x + self.passing
        self.next_y = self.minimum_y + self.passing
        self.total_squares = 0
        self.painted_squares = 0
        self.area_squares = 0
        self.square_already_painted = True
        self.toggle_painted_squares = False
        self.previous_squares = True
        self.Row_Verifier()
        
    
    def Row_Verifier(self):
        while self.previous_y <= self.maximum_y:
            if self.previous_x >= self.maximum_x:
                self.toggle_painted_squares = False
                self.previous_squares = True
                self.previous_x = self.minimum_x
                self.next_x = self.previous_x + self.passing
                self.previous_y = self.next_y
                self.next_y = self.previous_y + self.passing
            else:
                self.total_squares += 1
                self.y_position = 0
                self.empty_previous_squares = True
                self.square_already_painted = True
                self.prevents_toggle_redundant = True
                if self.toggle_painted_squares:
                    self.area_squares += 1
                    self.prevents_toggle_redundant = False
                    if self.show_graph:
                        plt.fill([self.previous_x, self.previous_x, self.next_x, self.next_x], [self.previous_y, self.next_y, self.next_y, self.previous_y], color="#00ff00")
                    else:
                        pass
                self.List_Updater()
                if self.empty_previous_squares:
                    self.previous_squares = True
                self.x_copy = self.new_x[::]
                self.y_copy = self.new_y[::]
                self.new_x, self.new_y = [], []
                self.previous_x = self.next_x
                self.next_x = self.previous_x + self.passing
        self.total_amount_of_squares = self.total_squares
        self.amount_of_marcked_squares = self.painted_squares + self.area_squares
    

    def List_Updater(self):
        for item in self.x_copy:
            if (item >= self.previous_x and item <= self.next_x and
                self.y_copy[self.y_position] >= self.previous_y and self.y_copy[self.y_position] <= self.next_y
            ):
                if self.square_already_painted:
                    if self.previous_squares and not self.toggle_painted_squares:
                        self.toggle_painted_squares = True
                    elif self.previous_squares and self.toggle_painted_squares:
                        self.toggle_painted_squares = False
                    self.previous_squares = False
                    self.empty_previous_squares = False
                    if self.prevents_toggle_redundant:
                        if self.show_graph:
                            plt.fill([self.previous_x, self.previous_x, self.next_x, self.next_x], [self.previous_y, self.next_y, self.next_y, self.previous_y], color="#ffff00")
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