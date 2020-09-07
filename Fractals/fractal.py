# from propriedades/propriedade_por_quadrado.py import *
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import time


class Fractal():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def Save_Pdf(self, file_name = "fractal", color = "#000000"):
        plt.plot(self.x, self.y, color = color)
        file_name = file_name + ".pdf"
        with PdfPages(file_name) as export_pdf:
            export_pdf.savefig()

        
    def Cronometer(self, args):
        start = time.time()
        # self.Create_Fractal(args)
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

    
    # def Create_Sigle_List(self):
    #     """ List of List """
    #     new_x = []
    #     new_y = []
    #     for item in self.x:
    #         new_x.extend(item)
    #     for item in self.y:
    #         new_y.extend(item)
    #     return new_x, new_y  # Usar Self

    
    # def Does_Square_Property(self):
    #     FazCalculo(self.x, self.y, self.value)
    #     print("Montando o Gráfico")
    #     plt.show()
