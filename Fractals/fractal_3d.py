from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import time


class Fractal3d():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        
    def Cronometer(self, args):
        start = time.time()
        the_end = time.time()
        self.runtime = round(the_end - start, 5)

    
    def Define_Vars(self, args, default_vars):
        for variable in default_vars:
            if variable in args:
                default_vars[variable] = args[variable]
        return default_vars

    
    def Show_Graph(self):
        print("Loading Graph")
        plt.show()
