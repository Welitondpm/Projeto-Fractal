from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import time


class Fractal():
    def __init__(self, x = [], y = []):
        self.x = x
        self.y = y

    
    def Save_Pdf(self, file_name = "fractal"):
        file_name = file_name + ".pdf"
        with PdfPages(file_name) as export_pdf:
            export_pdf.savefig()

        
    def Cronometer(self, color = "#000000"):
        start = time.time()
        self.Create_Fractal(color = color)
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