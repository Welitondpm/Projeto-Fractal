import matplotlib.pyplot as plt
import math
import time
import random
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
from mandelbrot import Logistic_Mandelbrot
from mandelbrot import LogisticMap
from sierpinski import Sierpinski
from sierpinski import SierpinskiCarpet
from sierpinski import ArrowHead
from sierpinski import ChaoticTriangle
from sierpinski import SierpinskiPascal
from menger import Menger
from menger import ColorfulMenger
from menger import SierpinskiTetrahedron
from menger import ColorfulSierpinskiTetrahedron
from koch_tetrahedron import KochTetrahedron


def Do_Cantor_Set(args = {}, save_pdf = False, file_name = "fractal", show_time = False, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    cantor_set = CantorSet(args = args)
    cantor_set.Start_Cronometer()
    if property_perimeter:
        cantor_set.Property_Perimeter(paint_squares)
        print("Marcked Squares %d of %d" % (cantor_set.property_square.amount_of_marcked_squares, cantor_set.property_square.total_amount_of_squares))
    elif property_dimension:
        cantor_set.Property_Dimension()
        print("Dimension = %s" % (cantor_set.dimension))
    elif progression_property_perimeter:
        cantor_set.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        cantor_set.Progression_Property(make_graph = make_graph)
    else:
        cantor_set.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        cantor_set.Save_Pdf(file_name = file_name)
    if show_time:
        cantor_set.End_Cronometer()
        print("%f seconds" % (cantor_set.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        cantor_set.Show_Graph()


def Do_Dragon_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = False, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    dragon_curve = DragonCurve(args = args)
    dragon_curve.Start_Cronometer()
    if property_perimeter:
        dragon_curve.Property_Perimeter(paint_squares)
        print("Marcked Squares %d of %d" % (dragon_curve.property_square.amount_of_marcked_squares, dragon_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        dragon_curve.Property_Dimension()
        print("Dimension = %s" % (dragon_curve.dimension))
    elif progression_property_perimeter:
        dragon_curve.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        dragon_curve.Progression_Property(make_graph = make_graph)
    else:
        dragon_curve.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        dragon_curve.Save_Pdf(file_name = file_name)
    if show_time:
        dragon_curve.End_Cronometer()
        print("%f seconds" % (dragon_curve.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        dragon_curve.Show_Graph()


def Do_Koch_Flake(args = {}, save_pdf = False, file_name = "fractal", show_time = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_area = False, progression_property_area = False):
    koch_flake = Flake(args = args)
    koch_flake.Start_Cronometer()
    if property_area:
        koch_flake.Property_Area()
        print("Marcked Squares %d of %d" % (koch_flake.property_area.amount_of_marcked_squares, koch_flake.property_area.total_amount_of_squares))
    elif property_dimension:
        koch_flake.Property_Dimension()
        print("Dimension = %s" % (koch_flake.dimension))
    elif progression_property_area:
        koch_flake.Progression_Property(property_area = True)
    elif progression_property_dimension:
        koch_flake.Progression_Property(make_graph = make_graph)
    else:
        koch_flake.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        koch_flake.Save_Pdf(file_name = file_name)
    if show_time:
        koch_flake.End_Cronometer()
        print("%f seconds" % (koch_flake.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        koch_flake.Show_Graph()

    
def Do_Hilbert_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = False, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    hilbert_curve = HilbertCurve(args = args)
    hilbert_curve.Start_Cronometer()
    if property_perimeter:
        hilbert_curve.Property_Perimeter(paint_squares)
        print("Marcked Squares %d of %d" % (hilbert_curve.property_square.amount_of_marcked_squares, hilbert_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        hilbert_curve.Property_Dimension()
        print("Dimension = %s" % (hilbert_curve.dimension))
    elif progression_property_perimeter:
        hilbert_curve.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        hilbert_curve.Progression_Property(make_graph = make_graph)
    else:
        hilbert_curve.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        hilbert_curve.Save_Pdf(file_name = file_name)
    if show_time:
        hilbert_curve.End_Cronometer()
        print("%f seconds" % (hilbert_curve.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        hilbert_curve.Show_Graph()

    
def Do_Inverted_Binary(args = {}, save_pdf = False, file_name = "fractal", show_time = False, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_square = False, progression_property_square = False):
    inverted_binary = InvertedBinary(args = args)
    inverted_binary.Start_Cronometer()
    if property_square:
        inverted_binary.Property_Square(paint_squares)
        print("Marcked Squares %d of %d" % (inverted_binary.property_square.amount_of_marcked_squares, inverted_binary.property_square.total_amount_of_squares))
    elif property_dimension:
        inverted_binary.Property_Dimension()
        print("Dimension = %s" % (inverted_binary.dimension))
    elif progression_property_square:
        inverted_binary.Progression_Property(property_square = True)
    elif progression_property_dimension:
        inverted_binary.Progression_Property(make_graph = make_graph)
    else:
        inverted_binary.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        inverted_binary.Save_Pdf(file_name = file_name)
    if show_time:
        inverted_binary.End_Cronometer()
        print("%f seconds" % (inverted_binary.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        inverted_binary.Show_Graph()


def Do_Koch_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = False, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    koch_curve = Koch(args = args)
    koch_curve.Start_Cronometer()
    if property_perimeter:
        koch_curve.Property_Perimeter(paint_squares)
        print("Marcked Squares %d of %d" % (koch_curve.property_square.amount_of_marcked_squares, koch_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        koch_curve.Property_Dimension()
        print("Dimension = %s" % (koch_curve.dimension))
    elif progression_property_perimeter:
        koch_curve.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        koch_curve.Progression_Property(make_graph = make_graph)
    else:
        koch_curve.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        koch_curve.Save_Pdf(file_name = file_name)
    if show_time:
        koch_curve.End_Cronometer()
        print("%f seconds" % (koch_curve.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        koch_curve.Show_Graph()


def Sierpinski_Triangle_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    sierpinski_triangle = Sierpinski()
    sierpinski_triangle.Progression_Property_Dimension(args = args, value = value, color =color, make_graph = make_graph)
    if make_graph:
        sierpinski_triangle.Show_Graph()

    
def Sierpinski_Carpet_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    sierpinski_carpet = SierpinskiCarpet()
    sierpinski_carpet.Progression_Property_Dimension(args = args, value = value, color = color, make_graph = make_graph)
    if make_graph:
        sierpinski_carpet.Show_Graph()


def Arrowhead_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    arrowhead = ArrowHead(args = args)
    arrowhead.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        arrowhead.Show_Graph()


def Chaotic_Triangle_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True, new_points_per_measurement = 10000):
    chaotic_triangle = ChaoticTriangle(args = args)
    chaotic_triangle.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph, new_points_per_measurement = new_points_per_measurement)
    if make_graph:
        chaotic_triangle.Show_Graph()


def Tree_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    tree = Tree(args = args)
    tree.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        tree.Show_Graph()


def Calculation_Progression_Fractal_2D(value = 10):
    Sierpinski_Carpet_Progression_Dimension(args = {"times": 3}, value = value, color = "#00ff00", make_graph = False)
    Sierpinski_Triangle_Progression_Dimension(args = {"times": 5}, value = value, color = "#ff0000", make_graph = False)
    # Chaotic_Triangle_Progression_Dimension(args = {"times": 500000}, new_points_per_measurement = 100000, value = value, color = "#ff8800", make_graph = False)
    Arrowhead_Progression_Dimension(args = {"times": 5}, value = value, color = "#0000ff", make_graph = False)
    plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
    plt.savefig("Progression_fractal.png")
    fractal = Fractal()
    fractal.Save_Pdf(file_name = "Progression_fractal")
    plt.show()


# arquivo = open("Fractals/Dados/dados.txt", "a")
# dados = ["Floco: 9 iterações"]
# arquivo.writelines(dados)


#### Execute Segmented Mandelbrot
# mandelbrot = SegmentedMandelbrot()
# mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior