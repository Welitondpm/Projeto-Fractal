import math


class Dimension():
    def __init__(self, painted_square, size_of_side_of_square):
        if size_of_side_of_square != 1:
            self.dimension = math.log10(painted_square) / (math.log10(1 / size_of_side_of_square))
        else:
            self.dimension = math.log10(painted_square) * (10 ** 30)