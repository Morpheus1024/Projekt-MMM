from cgitb import reset
from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

'''
todo
sprawdzić czym są w mag i
radiobuttony
pola tekstowe dla w, dt, t





--wyświetlanie wejścia i wyjścia jako przebieg czasowy
-- pobudzenie sygnałem harmonicznym
-- pobudzenie trójkątem
-- pobudzenie prostokątem o skończonym czasie trwania
-- wyznaczanie punkt po punkcie kolejnych współrzędnych i zapisywanie ich do tablicy - tatarowy "mały dt"
-- char. f. bodego


'''

class Uklad:

    def __init__(self, lista_IN):
        self.R = lista_IN[0]
        self.L = lista_IN[1]
        self.R2 = lista_IN[2]
        self.C = lista_IN[3]
        self.U = lista_IN[4]
        self.biegun = None

    def biegun(self):
        self.biegun = -(self.R + self.R2) / (self.R * self.R2 * self.C)
        return self.biegun

    def bode(self):
        self.sys = signal.TransferFunction([self.R], [self.R * self.R2 * self.C, self.R + self.R2])
        w, mag, phase = signal.bode(self.sys)
        plt.suptitle('Uklad') 
        plt1 = plt.subplot(221) 
        plt1.set_title('Phase')
        plt.semilogx(w, phase)  
        plt2 = plt.subplot(223)
        plt2.set_title('Magnitude')
        plt.semilogx(w, mag) 
        plt.tight_layout()

    def sygnal(self, time, A, w, dt):
        t = np.arange(0, time, dt)  
        IN1 = A * signal.square(w * t) 
        IN2 = A * signal.sawtooth(w * t, 0.5)  
        IN3 = A * np.sin(w*t)
        IN = IN1
        plt3 = plt.subplot(222)
        plt.plot(t, IN) 
        plt3.set_title('IN') 
        plt.tight_layout()
        
        return IN
    
    def wyjscie(self, time, IN, dt):
        t = np.arange(0, time, dt)
        oryginal_transmitancji = self.R*exp(-(t*(self.R + self.R2))/(self.C*self.R*self.R2))/(self.R + self.R2) - self.R/(self.R + self.R2)
        OUT = np.convolve(IN,oryginal_transmitancji)
        plt4 = plt.subplot(224)
        plt.plot(OUT)
        plt4.set_title('OUT')
        plt.tight_layout() 


###################################################
RLC = [10, 1, 15, 20, 1]  # R, L, R2, C, U
time = 250
dt = 0.1
A = 2
w = 1
uklad = Uklad(RLC)

uklad.bode()
IN = uklad.sygnal(time, A, w, dt) 
uklad.wyjscie(time, IN, dt)
plt.show()
###################################################
