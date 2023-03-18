import sympy
sympy.init_printing()

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

t, s = sympy.symbols('t, s')



class układ:
    def __init__(self):
        self.R = 0
        self.L = 0
        self.R2 = 0
        self.C = 0
        self.U = 0
        self.Y = 0
        #zerowe warunki początkowe

    def wyjście(uklad):
        uklad.Y = (-1*uklad.U*uklad.R)/(uklad.R + uklad.R+ s*uklad.R*uklad.R2*uklad.C)
        



uklad = układ()
    