#### Execute Cantor Set
# cantor_set = CantorSet()
# cantor_set.Show_Graph()

# cantor = CantorSet(args={"times":15})
# cantor.Progression_Property_Perimeter(value=150)

# cantor = CantorSet(args={"times":2})
# cantor.Property_Perimeter(value=10)
# print("Quadrados pintados %d de %d" % (cantor.property_square.amount_of_marcked_squares, cantor.property_square.total_amount_of_squares))
# cantor.Show_Graph()



#### Execute Dragon Curve
# dragon_curve = DragonCurve()
# dragon_curve.Show_Graph()



#### Execute Generalization of the Flake
# snow_flake = Flake(args = {"inwards_out_wards": True})
# snow_flake.Show_Graph()



#### Execute Hilbert Curve
# hilbert = HilbertCurve()
# hilbert.Show_Graph()



#### Execute Inverted Binary
# binary = InvertedBinary()
# binary.Show_Graph()



#### Execute Generalization of the Koch
# koch = Koch(args = {"amount_of_sides": 6})
# koch.Show_Graph()


##############################
##############################
##############################
#### Execute Koch Tetrahedron
# kochTetrahedron = KochTetrahedron()
# kochTetrahedron.Show_Graph()



#### Execute Menger Sponge
# menger = Menger(args = {"times": 3})
# menger.Show_Graph()



#### Execute Colorful Menger Sponge
# mengercolor = ColorfulMenger(args = {"times": 3})
# mengercolor.Show_Graph()



#### Execute Sierpinski
# sierpinstetra = SierpinskiTetrahedron(args = {"times": 4})
# sierpinstetra.Show_Graph()



#### Execute Colorful Sierpinski
# sierpinstetracolor = ColorfulSierpinskiTetrahedron(args = {"times": 4})
# sierpinstetracolor.Show_Graph()
##############################
##############################
##############################



#### Execute Logarithmic Mandelbrot 
# mandelbrot = Mandelbrot(args = {"amount_of_colors": 12})
# # # mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior
# mandelbrot.Show_Graph()

# mandelbrot = Mandelbrot(args = {"amount_of_colors": 12})
# mandelbrot.Create_Fractal()
# mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior
# mandelbrot.Property_Square()
# print("Quadrados pintados %d de %d" % (mandelbrot.property_square.amount_of_marcked_squares, mandelbrot.property_square.total_amount_of_squares))
# mandelbrot.Show_Graph()



#### Execute Harmonic Mandelbrot
# mandelbrot = HarmonicMandelbrot(args = {"amount_of_colors":200, "depth":200})
# mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior
# mandelbrot.Show_Graph()



#### Execute Segmented Mandelbrot
# mandelbrot = SegmentedMandelbrot()
# mandelbrot.Define_Colors_Unique()       ## Atenção nunca execute essa linha junto com a inferior
# # mandelbrot.Define_Colors_Multi()      ## Atenção nunca execute essa linha junto com superior
# mandelbrot.Show_Graph()



#### Execute Sierpinski Triangle
# sierpins = Sierpinski(args = {"times": 5})
# sierpins.Show_Graph()



#### Execute Sierpinski Carpet
# carpet = SierpinskiCarpet()
# carpet.Show_Graph()



#### Execute Linear Sierpinski
# arrow = ArrowHead()
# arrow.Show_Graph()



#### Execute Chaotic Sierpinski
# chaotic = ChaoticTriangle()
# chaotic.Show_Graph()
    
# chaotic = ChaoticTriangle()
# chaotic.Property_Square(value=100)
# print("Quadrados pintados %d de %d" % (chaotic.property_square.amount_of_marcked_squares, chaotic.property_square.total_amount_of_squares))
# chaotic.Show_Graph()

# chaotic = ChaoticTriangle(args={"times":100000})
# chaotic.Progression_Property_Square(value=100, new_points_per_measurement=10000)
# print("Quadrados pintados %d de %d" % (chaotic.property_square.amount_of_marcked_squares, chaotic.property_square.total_amount_of_squares))
# chaotic.Show_Graph()



#### Execute Sierpinski Base Pascal
# basePascal = SierpinskiPascal()
# basePascal.Create_Fractal()



#### Execute Tree
# fractalTree = Tree()
# fractalTree.Show_Graph()