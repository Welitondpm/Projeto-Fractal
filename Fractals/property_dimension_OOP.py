import math


class Dimension():
    def __init__(self, painted_square, size_of_side_of_square):
        self.dimension = math.log10(painted_square) / (math.log10(1 / size_of_side_of_square) + 0.00000000000001)