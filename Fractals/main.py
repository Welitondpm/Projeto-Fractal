import matplotlib.pyplot as plt
import math
import time
import random
# import os
import psutil
import cpuinfo
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


def Do_Cantor_Set(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    cantor_set = CantorSet(args = args)
    cantor_set.Start_Cronometer()
    if property_perimeter:
        cantor_set.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (cantor_set.property_square.amount_of_marcked_squares, cantor_set.property_square.total_amount_of_squares))
    elif property_dimension:
        cantor_set.Property_Dimension()
        # print("Dimension = %s" % (cantor_set.dimension))
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
        # print("%f seconds" % (cantor_set.runtime))
        if property_dimension:
            return cantor_set.runtime, cantor_set.dimension
        else:
            return cantor_set.runtime
    if property_dimension or not make_graph:
        pass
    else:
        cantor_set.Show_Graph()


def Do_Dragon_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    dragon_curve = DragonCurve(args = args)
    dragon_curve.Start_Cronometer()
    if property_perimeter:
        dragon_curve.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (dragon_curve.property_square.amount_of_marcked_squares, dragon_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        dragon_curve.Property_Dimension()
        # print("Dimension = %s" % (dragon_curve.dimension))
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
        # print("%f seconds" % (dragon_curve.runtime))
        if property_dimension:
            return dragon_curve.runtime, dragon_curve.dimension
        else:
            return dragon_curve.runtime
    if property_dimension or not make_graph:
        pass
    else:
        dragon_curve.Show_Graph()


def Do_Koch_Flake(args = {}, save_pdf = False, file_name = "fractal", show_time = True, make_graph = True, property_dimension = False, progression_property_dimension = False, property_area = False, progression_property_area = False):
    koch_flake = Flake(args = args)
    koch_flake.Start_Cronometer()
    if property_area:
        koch_flake.Property_Area()
        # print("Marcked Squares %d of %d" % (koch_flake.property_area.amount_of_marcked_squares, koch_flake.property_area.total_amount_of_squares))
    elif property_dimension:
        koch_flake.Property_Dimension()
        # print("Dimension = %s" % (koch_flake.dimension))
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
        # print("%f seconds" % (koch_flake.runtime))
        if property_dimension:
            return koch_flake.runtime, koch_flake.dimension
        else:
            return koch_flake.runtime
    if property_dimension or not make_graph:
        pass
    else:
        koch_flake.Show_Graph()

    
def Do_Hilbert_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    hilbert_curve = HilbertCurve(args = args)
    hilbert_curve.Start_Cronometer()
    if property_perimeter:
        hilbert_curve.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (hilbert_curve.property_square.amount_of_marcked_squares, hilbert_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        hilbert_curve.Property_Dimension()
        # print("Dimension = %s" % (hilbert_curve.dimension))
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
        # print("%f seconds" % (hilbert_curve.runtime))
        if property_dimension:
            return hilbert_curve.runtime, hilbert_curve.dimension
        else:
            return hilbert_curve.runtime
    if property_dimension or not make_graph:
        pass
    else:
        hilbert_curve.Show_Graph()

    
def Do_Inverted_Binary(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_square = False, progression_property_square = False):
    inverted_binary = InvertedBinary(args = args)
    inverted_binary.Start_Cronometer()
    if property_square:
        inverted_binary.Property_Square(paint_squares)
        # print("Marcked Squares %d of %d" % (inverted_binary.property_square.amount_of_marcked_squares, inverted_binary.property_square.total_amount_of_squares))
    elif property_dimension:
        inverted_binary.Property_Dimension()
        # print("Dimension = %s" % (inverted_binary.dimension))
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
        # print("%f seconds" % (inverted_binary.runtime))
        if property_dimension:
            return inverted_binary.runtime, inverted_binary.dimension
        else:
            return inverted_binary.runtime
    if property_dimension or not make_graph:
        pass
    else:
        inverted_binary.Show_Graph()


def Do_Koch_Curve(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    koch_curve = Koch(args = args)
    koch_curve.Start_Cronometer()
    if property_perimeter:
        koch_curve.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (koch_curve.property_square.amount_of_marcked_squares, koch_curve.property_square.total_amount_of_squares))
    elif property_dimension:
        koch_curve.Property_Dimension()
        # print("Dimension = %s" % (koch_curve.dimension))
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
        # print("%f seconds" % (koch_curve.runtime))
        if property_dimension:
            return koch_curve.runtime, koch_curve.dimension
        else:
            return koch_curve.runtime
    if property_dimension or not make_graph:
        pass
    else:
        koch_curve.Show_Graph()


def Do_Mandelbrot(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, property_dimension = False, property_square = False, harmonic_mandelbrot = False, segmented_mandelbrot = False, logistic_mandelbrot = False, logistic_map = False, multi_colors = False):
    if harmonic_mandelbrot:
        mandelbrot = HarmonicMandelbrot(args)
    elif segmented_mandelbrot:
        mandelbrot = SegmentedMandelbrot(args)
    elif logistic_mandelbrot:
        mandelbrot = LogisticMandelbrot(args)
    elif logistic_map:
        mandelbrot = LogisticMap(args)
    else:
        mandelbrot = Mandelbrot(args)
    mandelbrot.Start_Cronometer()
    mandelbrot.Create_Fractal()
    if not logistic_map:
        # if not multi_colors and not property_dimension:
        #     mandelbrot.Define_Colors_Unique()
        # elif not property_dimension:
        #     mandelbrot.Define_Colors_Multi()
        if property_square:
            mandelbrot.Property_Square(paint_squares)
            # print("Marcked Squares %d of %d" % (mandelbrot.property_square.amount_of_marcked_squares, mandelbrot.property_square.total_amount_of_squares))
        elif property_dimension:
            mandelbrot.Property_Dimension()
            print("Dimension = %s" % (mandelbrot.dimension))
    if save_pdf and not property_dimension:
        mandelbrot.Save_Pdf(file_name = file_name)
    if show_time:
        mandelbrot.End_Cronometer()
        # print("%f seconds" % (mandelbrot.runtime))
        if property_dimension:
            return mandelbrot.runtime, mandelbrot.dimension
        else:
            return mandelbrot.runtime
    if not property_dimension:
        mandelbrot.Show_Graph()

    
def Do_Sierpinski_Triangle(args = {}, save_pdf = False, file_name = "fractal", show_time = True, make_graph = True, property_dimension = False, progression_property_dimension = False, property_area = False, progression_property_area = False):
    sierpinski_triangle = Sierpinski(args = args)
    sierpinski_triangle.Start_Cronometer()
    if property_area:
        sierpinski_triangle.Property_Area()
        # print("Marcked Squares %d of %d" % (sierpinski_triangle.property_area.amount_of_marcked_squares, sierpinski_triangle.property_area.total_amount_of_squares))
    elif property_dimension:
        sierpinski_triangle.Property_Dimension()
        # print("Dimension = %s" % (sierpinski_triangle.dimension))
    elif progression_property_area:
        sierpinski_triangle.Progression_Property(property_area = True)
    elif progression_property_dimension:
        sierpinski_triangle.Progression_Property(make_graph = make_graph)
    else:
        sierpinski_triangle.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        sierpinski_triangle.Save_Pdf(file_name = file_name)
    if show_time:
        sierpinski_triangle.End_Cronometer()
        # print("%f seconds" % (sierpinski_triangle.runtime))
        if property_dimension:
            return sierpinski_triangle.runtime, sierpinski_triangle.dimension
        else:
            return sierpinski_triangle.runtime
    if property_dimension or not make_graph:
        pass
    else:
        sierpinski_triangle.Show_Graph()

    
def Do_Sierpinski_Carpet(args = {}, save_pdf = False, file_name = "fractal", show_time = True, make_graph = True, property_dimension = False, progression_property_dimension = False, property_area = False, progression_property_area = False):
    sierpinski_carpet = SierpinskiCarpet(args = args)
    sierpinski_carpet.Start_Cronometer()
    if property_area:
        sierpinski_carpet.Property_Area()
        # print("Marcked Squares %d of %d" % (sierpinski_carpet.property_area.amount_of_marcked_squares, sierpinski_carpet.property_area.total_amount_of_squares))
    elif property_dimension:
        sierpinski_carpet.Property_Dimension()
        # print("Dimension = %s" % (sierpinski_carpet.dimension))
    elif progression_property_area:
        sierpinski_carpet.Progression_Property(property_area = True)
    elif progression_property_dimension:
        sierpinski_carpet.Progression_Property(make_graph = make_graph)
    else:
        sierpinski_carpet.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        sierpinski_carpet.Save_Pdf(file_name = file_name)
    if show_time:
        sierpinski_carpet.End_Cronometer()
        # print("%f seconds" % (sierpinski_carpet.runtime))
        if property_dimension:
            return sierpinski_carpet.runtime, sierpinski_carpet.dimension
        else:
            return sierpinski_carpet.runtime
    if property_dimension or not make_graph:
        pass
    else:
        sierpinski_carpet.Show_Graph()

    
def Do_Arrowhead(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    arrowhead = Arrowhead(args = args)
    arrowhead.Start_Cronometer()
    if property_perimeter:
        arrowhead.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (arrowhead.property_square.amount_of_marcked_squares, arrowhead.property_square.total_amount_of_squares))
    elif property_dimension:
        arrowhead.Property_Dimension()
        # print("Dimension = %s" % (arrowhead.dimension))
    elif progression_property_perimeter:
        arrowhead.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        arrowhead.Progression_Property(make_graph = make_graph)
    else:
        arrowhead.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        arrowhead.Save_Pdf(file_name = file_name)
    if show_time:
        arrowhead.End_Cronometer()
        # print("%f seconds" % (arrowhead.runtime))
        if property_dimension:
            return arrowhead.runtime, arrowhead.dimension
        else:
            return arrowhead.runtime
    if property_dimension or not make_graph:
        pass
    else:
        arrowhead.Show_Graph()
    

def Do_Chaotic_Triangle(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_square = False, progression_property_square = False):
    chaotic_triangle = ChaoticTriangle(args = args)
    chaotic_triangle.Start_Cronometer()
    if property_square:
        chaotic_triangle.Property_Square(paint_squares)
        # print("Marcked Squares %d of %d" % (chaotic_triangle.property_square.amount_of_marcked_squares, chaotic_triangle.property_square.total_amount_of_squares))
    elif property_dimension:
        chaotic_triangle.Property_Dimension()
        # print("Dimension = %s" % (chaotic_triangle.dimension))
    elif progression_property_square:
        chaotic_triangle.Progression_Property(property_square = True)
    elif progression_property_dimension:
        chaotic_triangle.Progression_Property(make_graph = make_graph)
    else:
        chaotic_triangle.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        chaotic_triangle.Save_Pdf(file_name = file_name)
    if show_time:
        chaotic_triangle.End_Cronometer()
        # print("%f seconds" % (chaotic_triangle.runtime))
        if property_dimension:
            return chaotic_triangle.runtime, chaotic_triangle.dimension
        else:
            return chaotic_triangle.runtime
    if property_dimension or not make_graph:
        pass
    else:
        chaotic_triangle.Show_Graph()


def Do_Tree(args = {}, save_pdf = False, file_name = "fractal", show_time = True, paint_squares = False, make_graph = True, property_dimension = False, progression_property_dimension = False, property_perimeter = False, progression_property_perimeter = False):
    tree = Tree(args = args)
    tree.Start_Cronometer()
    if property_perimeter:
        tree.Property_Perimeter(paint_squares)
        # print("Marcked Squares %d of %d" % (tree.property_square.amount_of_marcked_squares, tree.property_square.total_amount_of_squares))
    elif property_dimension:
        tree.Property_Dimension()
        # print("Dimension = %s" % (tree.dimension))
    elif progression_property_perimeter:
        tree.Progression_Property(property_perimeter = True)
    elif progression_property_dimension:
        tree.Progression_Property(make_graph = make_graph)
    else:
        tree.Create_Fractal()
    if save_pdf and not property_dimension and make_graph:
        tree.Save_Pdf(file_name = file_name)
    if show_time:
        tree.End_Cronometer()
        # print("%f seconds" % (tree.runtime))
        if property_dimension:
            return tree.runtime, tree.dimension
        else:
            return tree.runtime
    if property_dimension or not make_graph:
        pass
    else:
        tree.Show_Graph()


def Max_Value_Cantor_Set(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Cantor_Set(args = {"times": iteration})
        data = ["'Cantor_Set', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Cantor_Set(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Cantor_Set', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Cantor Set, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))

        
def Max_Value_Dragon_Curve(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time and iteration < 15:
        runtime = Do_Dragon_Curve(args = {"times": iteration})
        data = ["'Dragon_Curve', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            print(iteration)
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Dragon_Curve(property_dimension = True, args = {"times": iteration, "value": value})
        data = ["'Dragon_Curve', 'Iteration: " + str(iteration) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        print(value)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Dragon Curve, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration, value, dimension, runtime))


def Max_Value_Koch_Flake(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Koch_Flake(args = {"times": iteration})
        data = ["'Flake', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Koch_Flake(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Flake', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Koch Flake, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Hilbert_Curve(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Hilbert_Curve(args = {"times": iteration})
        data = ["'Hilbert_Curve', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Hilbert_Curve(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Hilbert_Curve', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Hilbert Curve, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Inverted_Binary(file, max_time = 120, max_time_property = 600):
    runtime = 0
    end = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Inverted_Binary(args = {"end": end})
        data = ["'Inverted_Binary', 'End: " + str(end) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            end += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Inverted_Binary(property_dimension = True, args = {"end": end - 3, "value": value})
        data = ["'Inverted_Binary', 'end: " + str(end - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Inverted Binary, End: %d, Value: %d, Dimension: %f, Time: %f" % (end - 3, value, dimension, runtime))


def Max_Value_Koch_Curve(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 50000
    value = 50
    while runtime <= max_time:
        runtime = Do_Koch_Curve(args = {"times": iteration})
        data = ["'Koch_Curve', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 50000
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Koch_Curve(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Koch_Curve', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Koch Curve, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Mandelbrot(file, max_time = 120, max_time_property = 600):
    runtime = 0
    density = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Mandelbrot(args = {"density": density})
        data = ["'Flake', 'Density: " + str(density) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            density += 50
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Mandelbrot(property_dimension = True, args = {"times": density, "value": value})
        data = ["'Flake', 'Density: " + str(density) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Mandelbrot, Density: %d, Value: %d, Dimension: %f, Time: %f" % (density, value, dimension, runtime))


def Max_Value_Sierpinski_Triangle(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Sierpinski_Triangle(args = {"times": iteration})
        data = ["'Sierpinski_Triangle', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Sierpinski_Triangle(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Sierpinski_Triangle', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Sierpinski Triangle, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Sierpinski_Carpet(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Sierpinski_Carpet(args = {"times": iteration})
        data = ["'Sierpinski_Triangle', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Sierpinski_Carpet(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Sierpinski_Triangle', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Sierpinski Carpet, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Arrowhead(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Arrowhead(args = {"times": iteration})
        data = ["'Arrowhead', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Arrowhead(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Arrowhead', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Arrowhead, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Max_Value_Chaotic_Triangle(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Chaotic_Triangle(args = {"times": 10000 * iteration})
        data = ["'Chaotic_Triangle', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Chaotic_Triangle(property_dimension = True, args = {"times": iteration - 10000, "value": value})
        data = ["'Chaotic_Triangle', 'Iteration: " + str(iteration - 10000) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Chaotic Triangle, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 10000, value, dimension, runtime))


def Max_Value_Tree(file, max_time = 120, max_time_property = 600):
    runtime = 0
    iteration = 1
    value = 50
    while runtime <= max_time:
        runtime = Do_Tree(args = {"times": iteration})
        data = ["'Tree', 'Iteration: " + str(iteration) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            iteration += 1
    runtime = 0
    while runtime <= max_time_property:
        runtime, dimension = Do_Tree(property_dimension = True, args = {"times": iteration - 3, "value": value})
        data = ["'Tree', 'Iteration: " + str(iteration - 3) + "', 'Value: " + str(value) + "', 'Dimension: " + str(dimension) + "', 'Time: " + str(runtime) + "'//\n"]
        file.writelines(data)
        if psutil.virtual_memory().percent >= 60:
            break
        else:
            value += 50
    print("Tree, Iteration: %d, Value: %d, Dimension: %f, Time: %f" % (iteration - 3, value, dimension, runtime))


def Test_Max_Value():
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu = cpu.split()
    file = open("Dados/" + cpu[2] + ".txt", "a")
    max_time = 5
    max_time_property = 10
    Max_Value_Cantor_Set(file, max_time, max_time_property)
    Max_Value_Dragon_Curve(file, max_time, max_time_property)
    Max_Value_Koch_Flake(file, max_time, max_time_property)
    Max_Value_Hilbert_Curve(file, max_time, max_time_property)
    Max_Value_Inverted_Binary(file, max_time, max_time_property)
    Max_Value_Koch_Curve(file, max_time, max_time_property)
    Max_Value_Mandelbrot(file, max_time, max_time_property)
    Max_Value_Sierpinski_Triangle(file, max_time, max_time_property)
    Max_Value_Sierpinski_Triangle(file, max_time, max_time_property)
    Max_Value_Arrowhead(file, max_time, max_time_property)
    Max_Value_Chaotic_Triangle(file, max_time, max_time_property)
    Max_Value_Tree(file, max_time, max_time_property)


Test_Max_Value()


# Do_Cantor_Set(paint_squares=True)
# Do_Cantor_Set(paint_squares=True, property_dimension=True)
# Do_Cantor_Set(paint_squares=True, property_perimeter=True)
# Do_Cantor_Set(paint_squares=True, progression_property_dimension= True)
# Do_Cantor_Set(paint_squares=True, progression_property_perimeter=True)


# Do_Dragon_Curve(paint_squares=True)
# Do_Dragon_Curve(paint_squares=True, property_dimension=True)
# Do_Dragon_Curve(paint_squares=True, property_perimeter=True)
# Do_Dragon_Curve(paint_squares=True, progression_property_dimension=True)
# Do_Dragon_Curve(paint_squares=True, progression_property_perimeter=True)


# Do_Koch_Flake(show_time=True)
# Do_Koch_Flake(property_dimension=True)
# Do_Koch_Flake(property_area=True)
# Do_Koch_Flake(progression_property_dimension=True)
# Do_Koch_Flake(progression_property_area=True)


# Do_Hilbert_Curve(paint_squares=True)
# Do_Hilbert_Curve(paint_squares=True, property_dimension=True)
# Do_Hilbert_Curve(paint_squares=True, property_perimeter=True)
# Do_Hilbert_Curve(paint_squares=True, progression_property_perimeter=True)
# Do_Hilbert_Curve(paint_squares=True, progression_property_dimension=True)


# Do_Inverted_Binary(paint_squares=True)
# Do_Inverted_Binary(paint_squares=True, property_square=True)
# Do_Inverted_Binary(paint_squares=True, property_dimension=True)
# Do_Inverted_Binary(paint_squares=True, progression_property_square=True)
# Do_Inverted_Binary(paint_squares=True, progression_property_dimension=True)


# Do_Koch_Curve(paint_squares=True)
# Do_Koch_Curve(paint_squares=True, property_perimeter=True)
# Do_Koch_Curve(paint_squares=True, property_dimension=True)
# Do_Koch_Curve(paint_squares=True, progression_property_perimeter=True)
# Do_Koch_Curve(paint_squares=True, progression_property_dimension=True)


# Do_Mandelbrot(paint_squares=True)
# Do_Mandelbrot(paint_squares=True, multi_colors=True)
# Do_Mandelbrot(paint_squares=True, harmonic_mandelbrot=True)
# Do_Mandelbrot(paint_squares=True, segmented_mandelbrot=True)
# Do_Mandelbrot(paint_squares=True, property_square=True)
# Do_Mandelbrot(show_time=False, property_dimension=True, args={"value": 100})
# Do_Mandelbrot(logistic_mandelbrot=True)
# Do_Mandelbrot(logistic_map=True)


# Do_Sierpinski_Triangle(show_time=True)
# Do_Sierpinski_Triangle(property_area=True)
# Do_Sierpinski_Triangle(property_dimension=True)
# Do_Sierpinski_Triangle(progression_property_area=True)
# Do_Sierpinski_Triangle(progression_property_dimension=True)


# Do_Sierpinski_Carpet(show_time=True)
# Do_Sierpinski_Carpet(property_area=True)
# Do_Sierpinski_Carpet(property_dimension=True)
# Do_Sierpinski_Carpet(progression_property_area=True)
# Do_Sierpinski_Carpet(progression_property_dimension=True)


# Do_Arrowhead(paint_squares=True)
# Do_Arrowhead(paint_squares=True, property_perimeter=True)
# Do_Arrowhead(paint_squares=True, property_dimension=True)
# Do_Arrowhead(paint_squares=True, progression_property_perimeter=True)
# Do_Arrowhead(paint_squares=True, progression_property_dimension=True)


# Do_Chaotic_Triangle(paint_squares=True)
# Do_Chaotic_Triangle(paint_squares=True, property_square=True)
# Do_Chaotic_Triangle(paint_squares=True, property_dimension=True)
# Do_Chaotic_Triangle(paint_squares=True, progression_property_square=True)
# Do_Chaotic_Triangle(paint_squares=True, progression_property_dimension=True)


# Do_Tree(paint_squares=True)
# Do_Tree(paint_squares=True, property_perimeter=True)
# Do_Tree(paint_squares=True, property_dimension=True)
# Do_Tree(paint_squares=True, progression_property_perimeter=True)
# Do_Tree(paint_squares=True, progression_property_dimension=True)