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
            print("Fractal não encontrado certifique-se que está escrito conforme o exemplo. EX: Cantor_Set.")
        self.variable_property = self.Define_Vars(args_property, default_vars)
        self.fractal = fractal
        self.max_time = max_time
        self.Create()
    

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
                print("Marcked Squares %d of %d" % (self.object_fractal.property_area.amount_of_marcked_squares, self.object_fractal.property_area.total_amount_of_squares))
            else:
                self.object_fractal.First_Property(self.variable_property["paint_squares"])
                print("Marcked Squares %d of %d" % (self.object_fractal.property_square.amount_of_marcked_squares, self.object_fractal.property_square.total_amount_of_squares))
        elif self.variable_property["property_dimension"]:
            self.object_fractal.Property_Dimension()
            print("Dimension = %s" % (self.object_fractal.dimension))
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
                print("Marcked Squares %d of %d" % (self.object_fractal.property_square.amount_of_marcked_squares, self.object_fractal.property_square.total_amount_of_squares))
            elif self.variable_property["property_dimension"]:
                self.object_fractal.Property_Dimension()
                print("Dimension = %s" % (self.object_fractal.dimension))


    def Show_Property(self):
        if self.fractal == "Mandelbrot":
            if self.variable_property["save_pdf"] and not self.variable_property["property_dimension"]:
                self.object_fractal.Save_Pdf(file_name = self.variable_property["file_name"])
            if self.variable_property["show_time"]:
                self.object_fractal.End_Cronometer()
                print("%f seconds" % (self.object_fractal.runtime))
            if not self.variable_property["property_dimension"]:
                self.object_fractal.Show_Graph()
        else:
            if self.variable_property["save_pdf"] and not self.variable_property["property_dimension"] and self.variable_property["make_graph"]:
                self.object_fractal.Save_Pdf(file_name = self.variable_property["file_name"])
            if self.variable_property["show_time"]:
                self.object_fractal.End_Cronometer()
                print("%f seconds" % (self.object_fractal.runtime))
            if self.variable_property["property_dimension"] or not self.variable_property["make_graph"]:
                pass
            else:
                self.object_fractal.Show_Graph()


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