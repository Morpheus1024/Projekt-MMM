import sympy
sympy.init_printing()

import matplotlib.pyplot as plt
import numpy as np

t, s = sympy.symbols('t, s')



class Układ:
    def __init__(self, R, R2, L, U, C):
        self.R = R
        self.L = L
        self.R2 = R2
        self.C = C
        self.U = U
        self.Y = 0
        #zerowe warunki początkowe

    def wyjście(self):
        self.Y = (-1*self.U*self.R)/(self.R + self.R+ s*self.R*self.R2*self.C)
        
#zastanawiam się, czy nie trzeba by zamiast s od razu napisać jw

#w tym miejscu będzie pobieranie od użytkownika wartości R R2 C L U

uklad = Układ(R, R2, L, U, C)
    
