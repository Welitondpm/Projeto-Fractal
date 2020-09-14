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
        print("%f segundos" % (cantor_set.runtime))
    if property_dimension or not make_graph:
        pass
    else:
        cantor_set.Show_Graph()


def Dragon_Curve_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    dragon_curve = DragonCurve(args = args)
    dragon_curve.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        dragon_curve.Show_Graph()

    
def Flake_of_Koch_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    flake = Flake(args = args)
    flake.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        flake.Show_Graph()


def Hilbert_Curve(args = {}, value = 10, color = "#000000", make_graph = True):
    hilbert_curve = HilbertCurve(args = args)
    hilbert_curve.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        hilbert_curve.Show_Graph()


def Koch_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    koch = Koch(args = args)
    koch.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        koch.Show_Graph()


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


def Inverted_Binary_Progression_Dimension(args = {}, value = 10, color = "#000000", make_graph = True):
    inverted_binary = InvertedBinary(args = args)
    inverted_binary.Progression_Property_Dimension(value = value, color = color, make_graph = make_graph)
    if make_graph:
        inverted_binary.Show_Graph()


def Calculation_Progression_Fractal_2D(value = 10):
    Sierpinski_Carpet_Progression_Dimension(args = {"times": 3}, value = value, color = "#00ff00", make_graph = False)
    Sierpinski_Triangle_Progression_Dimension(args = {"times": 5}, value = value, color = "#ff0000", make_graph = False)
    # Chaotic_Triangle_Progression_Dimension(args = {"times": 500000}, new_points_per_measurement = 100000, value = value, color = "#ff8800", make_graph = False)
    Arrowhead_Progression_Dimension(args = {"times": 5}, value = value, color = "#0000ff", make_graph = False)
    # Cantor_Set_Progression_Dimension(args = {"times": 5}, value = value, color = "#ff00ff", make_graph = False)
    Dragon_Curve_Progression_Dimension(args = {"times": 5}, value = value, color = "#ff88ff", make_graph = False)
    Koch_Progression_Dimension(args = {"times": 5}, value = value, color = "#880000", make_graph = False)
    Flake_of_Koch_Progression_Dimension(args = {"times": 3}, value = value, color = "#00ff88", make_graph = False)
    plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.savefig("Progression_fractal.png", bbox_inches='tight')
    fractal = Fractal()
    fractal.Save_Pdf(file_name = "Progression_fractal")
    plt.show()


# Do_Cantor_Set(show_time=True)
# Calculation_Progression_Fractal_2D(value= 500)


# arquivo = open("Fractals/Dados/dados.txt", "a")
# dados = ["Floco: 9 iterações"]
# arquivo.writelines(dados)


#### Execute Segmented Mandelbrot
# mandelbrot = SegmentedMandelbrot()
# mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior