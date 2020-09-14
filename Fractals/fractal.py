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

        
    def Start_Cronometer(self):
        self.start = time.time()
        # self.Create_Fractal()
    

    def End_Cronometer(self):
        the_end = time.time()
        self.runtime = round(the_end - self.start, 5)

    
    def Define_Vars(self, args, default_vars):
        for variable in default_vars:
            if variable in args:
                default_vars[variable] = args[variable]
        return default_vars

    
    def Show_Graph(self):
        print("Loading Graph")
        plt.show()

    
    def Assemble_Graph(self, master_x = [], master_y = [], title = "Title", label_x = "Label X", label_y = "Label Y", label_plot = "Label Graph", make_graph = True):
        if make_graph:
            plt.plot(master_x, master_y, color = self.variables["color"])
            plt.scatter(master_x, master_y, color = self.variables["color"])
            plt.title(title)
            plt.xlabel(label_x)
            plt.ylabel(label_y)
        else:
            plt.plot(master_x, master_y, color = self.variables["color"], label = label_plot)
            plt.scatter(master_x, master_y, color = self.variables["color"])