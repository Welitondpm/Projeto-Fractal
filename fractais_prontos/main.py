import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
import time
import random
from random import randint
from propriedadeporquadrados import *


NaoEscolheo = True
Escolha = str(input(" (A)Fila de Koch:\n (B)Fractal Árvore:\n (C)Fractal Binário Invertido:\n (D)Fractal Curva de Hilbert:\n (E)Fractal Curva de Koch:\n (F)Fractal Curva de Koch X:\n (G)Fractal Curva do Dragão:\n (H)Fractal DPMFRR:\n (I)Fractal DPMFRR uma linha:\n (J)Fractal Floco:\n (K)Fractal Triângulo Caótico:\n (L)Fractal Triângulo de Sierpinski:\n (M)Fractal Triângulo de Sierpinski base Pascal:\n (N)Fractal Triângulo de Sierpinski Linear:\n (O)Generalização de Koch:\n (P)Generalização do Floco:\n (Q)Progressão da Generalização de Koch:\n (R)Progressão da Generalização do Floco:\n\n>>> "))
Functions = locals()
Options = {"A":"filakoch", "B":"arvore", "C":"binario", "D":"hilbert", "E":"koch", "F":"kochx", "G":"dragao", "H":"dpmfrr", "I":"dpmfrrumalinha", "J":"floco", "K":"caotico", "L":"sierpinski", "M":"sierpinskipascal", "N":"sierpinskilinear", "O":"generalizakoch", "P":"generalizafloco", "Q":"progressaogeneralizakoch", "R":"progressaogeneralizafloco"}
while NaoEscolheo:
    Escolha = Escolha.upper()
    if Escolha in Options:
        NaoEscolheo = False
        # NaoEscolheo = Functions[Options[Escolha]]()
        Escolha = Options[Escolha]
        if Escolha == Options["A"]:
            from filadekoch import *
            Begin()
        elif Escolha == Options["B"]:
            from fractal_arvore import *
            Begin()
        elif Escolha == Options["C"]:
            from fractal_binarioinvertido import *
            Begin()
        elif Escolha == Options["D"]:
            from fractal_curvadehilbert import *
            Begin()
        elif Escolha == Options["E"]:
            from fractal_curvadekoch import *
            Begin()
        elif Escolha == Options["F"]:
            from fractal_curvadekochX import *
            Begin()
        elif Escolha == Options["G"]:
            from fractal_curvadodragao import *
            Begin()
        elif Escolha == Options["H"]:
            from fractal_dpmfrr import *
            Begin()
        elif Escolha == Options["I"]:
            from fractal_dpmfrrumalinha import *
            Begin()
        elif Escolha == Options["J"]:
            from fractal_floco import *
            Begin()
        elif Escolha == Options["K"]:
            from fractal_triangulocaotico import *
            Begin()
        elif Escolha == Options["L"]:
            from fractal_triangulodesierpinski import *
            Begin()
        elif Escolha == Options["M"]:
            from fractal_triangulodesierpinskibasepascal import *
            Begin()
        elif Escolha == Options["N"]:
            from fractal_triangulodesierpinskilinear import *
            Begin()
        elif Escolha == Options["O"]:
            from generalizaçãodekoch import *
            Begin()
        elif Escolha == Options["P"]:
            from generalizaçãodofloco import *
            Begin()
        elif Escolha == Options["Q"]:
            from progressãodageneralizaçãodekoch import *
            Begin()
        elif Escolha == Options["R"]:
            from progressãodageneralizaçãodofloco import *
            Begin()
    else:
        Escolha = str(input("\nDIGITA DIREITO!!!\n\n (A)Fila de Koch:\n (B)Fractal Árvore:\n (C)Fractal Binário Invertido:\n (D)Fractal Curva de Hilbert:\n (E)Fractal Curva de Koch:\n (F)Fractal Curva de Koch X:\n (G)Fractal Curva do Dragão:\n (H)Fractal DPMFRR:\n (I)Fractal DPMFRR uma linha:\n (J)Fractal Floco:\n (K)Fractal Triângulo Caótico:\n (L)Fractal Triângulo de Sierpinski:\n (M)Fractal Triângulo de Sierpinski base Pascal:\n (N)Fractal Triângulo de Sierpinski Linear:\n (O)Generalização de Koch:\n (P)Generalização do Floco:\n (Q)Progressão da Generalização de Koch:\n (R)Progressão da Generalização do Floco:\n\n>>> "))