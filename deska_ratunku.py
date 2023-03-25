from scipy import signal

import matplotlib.pyplot as plt

import sympy

'''
todo

pobudzenie prostokątem o skończonym czasie trwania
pobudzenie trójkątem
pobudzenie sygnałem harmonicznym
wyświetlanie wejścia i wyjścia jako przebieg czasowy
coś nowego jeszcze coś dopisuję

-- char. f. bodego

'''

class Układ:
    def __init__(self, lista_IN):
        #lista_IN = wektor_wejścia #[R, L, R2, C, U]
        
        self.R = lista_IN[0]
        self.L = lista_IN[1]
        self.R2 = lista_IN[2]
        self.C = lista_IN[3]
        self.U = lista_IN[4]
        self.biegun = None
        #self.P = None
        #self.Q = None
        self.Y_string=''
        self.transmitancja =' Y/U = -R/(R+R2+sRCR2)'

        
        
        #zerowe warunki początkowe

    def biegun(self):
        self.biegun = -(self.R+self.R2)/(self.R*self.R2*self.C)
        return self.biegun

    def bode(self):
        self.sys = signal.TransferFunction([self.R], [self.R*self.R2*self.C, self.R+self.R2])
        w, mag, phase = signal.bode(self.sys)
        plt.figure()
        plt.semilogx(w, mag)    # Bode magnitude plot
        plt.figure()
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

    def odp_harmoniczna(self, IN):
        #IN = [A,w]
        A = IN[0]
        w = IN[1]
        #Y = A*R^2*sin(t*w) + A*R*R2*sin(t*w) - A*C*R^2*R2*w*cos(t*w))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2) + (A*C*R^2*R2*w*exp(-(t*(R + R2))/(C*R*R2)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
        #odp_harm (exp(-(t*(R + R2))/(C*R*R2))*(A*R^2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*R*R2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*C*R^2*R2*w - A*C*R^2*R2*w*exp((t*(R + R2))/(C*R*R2))*cos(t*w)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
        R = self.R
        R2 = self.R2
        C = self.C

        https://realpython.com/python-matplotlib-guide/



RLC = [10,1,15,20,1] #R, L, R2, C, U

uklad = Układ(RLC)

uklad.bode()

###################################################

#sys = signal.TransferFunction([1], [1, 2])  
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html
