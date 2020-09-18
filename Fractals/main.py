import matplotlib.pyplot as plt
import math
import time
import random
# import os
# import psutil
# import cpuinfo
from random import randint
from fractal import Fractal
from fractal_3d import Fractal3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
from property_per_square_OOP import PropertyPerSquare
from property_per_cube_OOP import PropertyPerCube
from property_perimeter_OOP import PropertyPerimeter
from property_area_OOP import PropertyArea
from property_dimension_OOP import Dimension
from cantor_set import CantorSet
from dragon_curve import DragonCurve
from flake import Flake
from hilbert_curve import HilbertCurve
from inverted_binary import InvertedBinary
from koch import Koch
from tree import Tree
from mandelbrot import Mandelbrot
from mandelbrot import HarmonicMandelbrot
from mandelbrot import SegmentedMandelbrot
from mandelbrot import LogisticMandelbrot
from mandelbrot import LogisticMap
from sierpinski import Sierpinski
from sierpinski import SierpinskiCarpet
from sierpinski import Arrowhead
from sierpinski import ChaoticTriangle
from sierpinski import SierpinskiPascal
from menger import Menger
from menger import ColorfulMenger
from menger import SierpinskiTetrahedron
from menger import ColorfulSierpinskiTetrahedron
from koch_tetrahedron import KochTetrahedron


class CreateFractals():
    def __init__(self, fractal, args = {}, max_time = 600, args_property = {}, harmonic_mandelbrot = False, segmented_mandelbrot = False, 
                logistic_mandelbrot = False, logistic_map = False):
        self.var_else = 0
        if fractal == "Cantor_Set":
            self.object_fractal = CantorSet(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Dragon_Curve":
            self.object_fractal = DragonCurve(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Koch_Flake":
            self.object_fractal = Flake(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "first_property": False, "progression_first_property": False}
        elif fractal == "Hilbert_Curve":
            self.object_fractal = HilbertCurve(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Inverted_Binary":
            self.object_fractal = InvertedBinary(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Koch_Curve":
            self.object_fractal = Koch(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Mandelbrot":
            if harmonic_mandelbrot:
                self.object_fractal = HarmonicMandelbrot(args)
            elif segmented_mandelbrot:
                self.object_fractal = SegmentedMandelbrot(args)
            elif logistic_mandelbrot:
                self.object_fractal = LogisticMandelbrot(args)
            elif logistic_map:
                self.object_fractal = LogisticMap(args)
            else:
                self.object_fractal = Mandelbrot(args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False, 
                            "paint_squares": False, "property_square": False, "multi_colors": False, "harmonic_mandelbrot": harmonic_mandelbrot,
                            "segmented_mandelbrot": segmented_mandelbrot, "logistic_mandelbrot": logistic_mandelbrot, "logistic_map": logistic_map}
        elif fractal == "Sierpinski_Triangle":
            self.object_fractal = Sierpinski(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "first_property": False, "progression_first_property": False}
        elif fractal == "Sierpinski_Carpet":
            self.object_fractal = SierpinskiCarpet(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "first_property": False, "progression_first_property": False}
        elif fractal == "Arrowhead":
            self.object_fractal = Arrowhead(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Chaotic_Triangle":
            self.object_fractal = ChaoticTriangle(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        elif fractal == "Tree":
            self.object_fractal = Tree(args = args)
            default_vars = {"show_time": True, "save_pdf": False, "file_name": "fractal", "property_dimension": False,  
                            "progression_property_dimension": False, "make_graph": True, "paint_squares": False, 
                            "first_property": False, "progression_first_property": False}
        else:
            self.var_else = 1
            print("Fractal não encontrado certifique-se que está escrito conforme o exemplo. EX: Cantor_Set.")
        if self.var_else == 0:
            self.variable_property = self.Define_Vars(args_property, default_vars)
            self.fractal = fractal
            self.max_time = max_time
            self.Create()
        else:
            print("Você Digitou: %s" % (fractal))
    

    def Define_Vars(self, args, default_vars):
        for variable in default_vars:
            if variable in args:
                default_vars[variable] = args[variable]
        return default_vars
    

    def Create(self):
        self.object_fractal.Start_Cronometer()
        if self.fractal in ["Cantor_Set", "Dragon_Curve", "Hilbert_Curve", "Koch_Curve", "Arrowhead", "Tree", "Inverted_Binary", "Chaotic_Triangle"]:
            self.Fractal_Property()
        elif self.fractal in ["Sierpinski_Triangle", "Sierpinski_Carpet", "Koch_Flake"]:
            self.Fractal_Property(property_area = True)
        elif self.fractal == "Mandelbrot":
            self.Fractal_Mandelbrot()
        self.Show_Property()

    
    def Fractal_Property(self, property_area = False):
        if self.variable_property["first_property"]:
            if property_area:
                self.object_fractal.First_Property()
                # print("Marcked Squares %d of %d" % (self.object_fractal.property_area.amount_of_marcked_squares, self.object_fractal.property_area.total_amount_of_squares))
            else:
                self.object_fractal.First_Property(self.variable_property["paint_squares"])
                # print("Marcked Squares %d of %d" % (self.object_fractal.property_square.amount_of_marcked_squares, self.object_fractal.property_square.total_amount_of_squares))
        elif self.variable_property["property_dimension"]:
            self.object_fractal.Property_Dimension()
            # print("Dimension = %s" % (self.object_fractal.dimension))
        elif self.variable_property["progression_first_property"]:
            self.object_fractal.Progression_Property(first_property = True)
        elif self.variable_property["progression_property_dimension"]:
            self.object_fractal.Progression_Property(make_graph = self.variable_property["make_graph"])
        else:
            self.object_fractal.Create_Fractal()

        
    def Fractal_Mandelbrot(self):
        self.object_fractal.Create_Fractal()
        if not self.variable_property["logistic_map"]:
            if not self.variable_property["multi_colors"] and not self.variable_property["property_dimension"]:
                self.object_fractal.Define_Colors_Unique()
            elif not self.variable_property["property_dimension"]:
                self.object_fractal.Define_Colors_Multi()
            if self.variable_property["property_square"]:
                self.object_fractal.Property_Square(self.variable_property["paint_squares"])
                # print("Marcked Squares %d of %d" % (self.object_fractal.property_square.amount_of_marcked_squares, self.object_fractal.property_square.total_amount_of_squares))
            elif self.variable_property["property_dimension"]:
                self.object_fractal.Property_Dimension()
                # print("Dimension = %s" % (self.object_fractal.dimension))


    def Show_Property(self):
        if self.fractal == "Mandelbrot":
            if self.variable_property["save_pdf"] and not self.variable_property["property_dimension"]:
                self.object_fractal.Save_Pdf(file_name = self.variable_property["file_name"])
            if self.variable_property["show_time"]:
                self.object_fractal.End_Cronometer()
                # print("%f seconds" % (self.object_fractal.runtime))
            if not self.variable_property["property_dimension"]:
                self.object_fractal.Show_Graph()
        else:
            if self.variable_property["save_pdf"] and not self.variable_property["property_dimension"] and self.variable_property["make_graph"]:
                self.object_fractal.Save_Pdf(file_name = self.variable_property["file_name"])
            if self.variable_property["show_time"]:
                self.object_fractal.End_Cronometer()
                # print("%f seconds" % (self.object_fractal.runtime))
            if self.variable_property["property_dimension"] or not self.variable_property["make_graph"]:
                pass
            else:
                self.object_fractal.Show_Graph()


def Max_Value(file, name_fractal, max_time = 10, iteration_start = 0, value_start = 0, step_value = 100, max_iteration = 10):
    runtime = 0
    iteration = max_iteration
    value = value_start
    while runtime <= max_time:
        value += step_value
        if name_fractal == "Mandelbrot":
            fractal = CreateFractals("Mandelbrot", args = {"density": iteration, "value": value}, args_property={"property_dimension": True})
        elif name_fractal == "Inverted_Binary":
            fractal = CreateFractals("Inverted_Binary", args = {"end": iteration, "value": value}, args_property={"property_dimension": True})
        else:
            fractal = CreateFractals(name_fractal, args = {"times": iteration,  "value": value}, args_property={"property_dimension": True})
        if fractal.var_else == 1:
            break
        runtime = fractal.object_fractal.runtime
        dimension = fractal.object_fractal.dimension
        if name_fractal == "Mandelbrot":
            data = ["'Mandelbrot', 'Density: " + str(iteration) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        elif name_fractal == "Inverted_Binary":
            data = ["'Inverted_Binary', 'End: " + str(iteration) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        else:
            data = ["'" + name_fractal + "', 'Iteration: " + str(iteration) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        print(data)
        if psutil.virtual_memory().percent >= 60:
            break
    if fractal.var_else == 0:
        print(name_fractal + ", Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration, value, dimension, runtime))


def Test_Max_Value():
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu = cpu.split()
    file = open("Dados/" + cpu[2] + ".txt", "a")
    max_time = 300
    Max_Value(file, "Cantor_Set", max_time, max_iteration = 15, value_start = 25000, step_value = 5000)
    Max_Value(file, "Dragon_Curve", max_time, max_iteration = 13)
    Max_Value(file, "Koch_Flake", max_time, max_iteration = 6)
    Max_Value(file, "Hilbert_Curve", max_time, max_iteration = 6)
    Max_Value(file, "Inverted_Binary", max_time, max_iteration = 18)
    Max_Value(file, "Koch_Curve", max_time, max_iteration = 8)
    Max_Value(file, "Mandelbrot", max_time, max_iteration = 400)
    Max_Value(file, "Sierpinski_Triangle", max_time, max_iteration = 8)
    Max_Value(file, "Sierpinski_Carpet", max_time, max_iteration = 4)
    Max_Value(file, "Arrowhead", max_time, max_iteration = 9)
    Max_Value(file, "Chaotic_Triangle", max_time, max_iteration = 150000)
    # # Max_Value(file, "Tree", max_time, iteration_start = 1)  # Code Break


# 'Cantor_Set', 'Iteration: 15'
# 'Dragon_Curve', 'Iteration: 13'
# 'Koch_Flake', 'Iteration: 6'
# 'Hilbert_Curve', 'Iteration: 6'
# 'Inverted_Binary', 'End: 18'
# 'Koch_Curve', 'Iteration: 8'
# 'Mandelbrot', 'Density: 400'
# 'Sierpinski_Triangle', 'Iteration: 8'
# 'Sierpinski_Carpet', 'Iteration: 4'
# 'Arrowhead', 'Iteration: 9'
# 'Chaotic_Triangle', 'Iteration: 150000'


# fractal = CreateFractals("Cantor_Set")
# fractal = CreateFractals("Cantor_Set", args_property={"property_dimension": True})
# fractal = CreateFractals("Cantor_Set", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Cantor_Set", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Cantor_Set", args_property={"progression_first_property": True})


# fractal = CreateFractals("Dragon_Curve")
# fractal = CreateFractals("Dragon_Curve", args_property={"property_dimension": True})
# fractal = CreateFractals("Dragon_Curve", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Dragon_Curve", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Dragon_Curve", args_property={"progression_first_property": True})


# fractal = CreateFractals("Koch_Flake")
# fractal = CreateFractals("Koch_Flake", args_property={"property_dimension": True})
# fractal = CreateFractals("Koch_Flake", args_property={"first_property": True})
# fractal = CreateFractals("Koch_Flake", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Koch_Flake", args_property={"progression_first_property": True})


# fractal = CreateFractals("Hilbert_Curve")
# fractal = CreateFractals("Hilbert_Curve", args_property={"property_dimension": True})
# fractal = CreateFractals("Hilbert_Curve", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Hilbert_Curve", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Hilbert_Curve", args_property={"progression_first_property": True})


# fractal = CreateFractals("Inverted_Binary")
# fractal = CreateFractals("Inverted_Binary", args_property={"property_dimension": True})
# fractal = CreateFractals("Inverted_Binary", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Inverted_Binary", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Inverted_Binary", args_property={"progression_first_property": True})


# fractal = CreateFractals("Koch_Curve")
# fractal = CreateFractals("Koch_Curve", args_property={"property_dimension": True})
# fractal = CreateFractals("Koch_Curve", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Koch_Curve", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Koch_Curve", args_property={"progression_first_property": True})


# fractal = CreateFractals("Mandelbrot")
# fractal = CreateFractals("Mandelbrot", logistic_map = True)
# fractal = CreateFractals("Mandelbrot", logistic_mandelbrot = True)
# fractal = CreateFractals("Mandelbrot", segmented_mandelbrot = True)
# fractal = CreateFractals("Mandelbrot", harmonic_mandelbrot = True)
# fractal = CreateFractals("Mandelbrot", args_property={"property_dimension": True})
# fractal = CreateFractals("Mandelbrot", args_property={"property_square": True})
# fractal = CreateFractals("Mandelbrot", args_property={"multi_colors": True})


# fractal = CreateFractals("Sierpinski_Triangle")
# fractal = CreateFractals("Sierpinski_Triangle", args_property={"property_dimension": True})
# fractal = CreateFractals("Sierpinski_Triangle", args_property={"first_property": True})
# fractal = CreateFractals("Sierpinski_Triangle", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Sierpinski_Triangle", args_property={"progression_first_property": True})


# fractal = CreateFractals("Sierpinski_Carpet")
# fractal = CreateFractals("Sierpinski_Carpet", args_property={"property_dimension": True})
# fractal = CreateFractals("Sierpinski_Carpet", args_property={"first_property": True})
# fractal = CreateFractals("Sierpinski_Carpet", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Sierpinski_Carpet", args_property={"progression_first_property": True})


# fractal = CreateFractals("Arrowhead")
# fractal = CreateFractals("Arrowhead", args_property={"property_dimension": True})
# fractal = CreateFractals("Arrowhead", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Arrowhead", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Arrowhead", args_property={"progression_first_property": True})


# fractal = CreateFractals("Chaotic_Triangle")
# fractal = CreateFractals("Chaotic_Triangle", args_property={"property_dimension": True})
# fractal = CreateFractals("Chaotic_Triangle", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Chaotic_Triangle", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Chaotic_Triangle", args_property={"progression_first_property": True})


# fractal = CreateFractals("Tree")
# fractal = CreateFractals("Tree", args_property={"property_dimension": True})
# fractal = CreateFractals("Tree", args_property={"first_property": True, "paint_squares": True})
# fractal = CreateFractals("Tree", args_property={"progression_property_dimension": True})
# fractal = CreateFractals("Tree", args_property={"progression_first_property": True})