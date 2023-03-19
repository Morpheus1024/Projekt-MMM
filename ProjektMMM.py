import sympy
sympy.init_printing()

t, s= sympy.symbols('t, s')

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html

import matplotlib.pyplot as plt
import numpy as np

from spicy import signal





class Układ:
    def __init__(self, R, R2, L, U, C):
        self.R = R
        self.L = L
        self.R2 = R2
        self.C = C
        self.U = U
        self.P
        self.Q
        self.Y_string=''
        self.transmitancja =' Y/U = -R/(R+R2+sRCR2)'
        #zerowe warunki początkowe

    def wyjście(self):
        self.P = -(self.R*(self.R + self.R2))/((self.R+self.R2)**2+(sympy.w*self.R*self.R2*self.C)**2)
        self.Q = (sympy.w*self.R*self.R2*self.C)/((self.R+self.R2)**2+(sympy.w*self.R*self.R2*self.C)**2)

        self.Y_string = "("+self.P.toString()+")" + "j*("*self.Q+")"

    def bode(self):
        #sys = signal.TransferFunction()

        
        
#zastanawiam się, czy nie trzeba by zamiast s od razu napisać jw - w sumie zrobiłem to XD

#w tym miejscu będzie pobieranie od użytkownika wartości R R2 C L U

uklad = Układ(R, R2, L, U, C)
    
