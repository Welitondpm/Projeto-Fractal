import matplotlib.pyplot as plt


class PropertySurface():
    def __init__(self, x = [], y = [], show_graph = False, passing = 1):
        middle_x = sum(x) / len(x)
        middle_y = sum(y) / len(y)
        middle_z = sum(z) / len(z)