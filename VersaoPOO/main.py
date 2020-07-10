from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import time


class Fractal():
    def __init__(self):
        print("Instância Criada")

    
    def Save_Pdf(self, x, y, file_name = "fractal", color = "#000000"):
        plt.plot(x, y, color = color)
        file_name = file_name + ".pdf"
        with PdfPages(file_name) as export_pdf:
            export_pdf.savefig()

        
    def Cronometer(self, args):
        start = time.time()
        self.Create_Fractal(args)
        the_end = time.time()
        print(str(round(the_end - start, 5)) + "s")

        
# fractalexecuta = Fractal()
# fractalexecuta.Save_Pdf([0, 1], [0, 1])