from cgitb import reset
from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# import sympy


'''
todo
sprawdzić czym są w mag i
wyznaczanie punkt po punkcie kolejnych współrzędnych i zapisywanie ich do tablicy - tatarowy "mały dt"
pobudzenie prostokątem o skończonym czasie trwania
pobudzenie trójkątem
pobudzenie sygnałem harmonicznym
wyświetlanie wejścia i wyjścia jako przebieg czasowy
coś nowego jeszcze coś dopisuję




-- char. f. bodego


'''


class Uklad:

    def __init__(self, lista_IN):
        # lista_IN = wektor_wejścia #[R, L, R2, C, U]
        self.IN = None
        self.R = lista_IN[0]
        self.L = lista_IN[1]
        self.R2 = lista_IN[2]
        self.C = lista_IN[3]
        self.U = lista_IN[4]
        self.biegun = None
        # self.P = None
        # self.Q = None
        self.Y_string = ''
        self.transmitancja = ' Y/U = -R/(R+R2+sRCR2)'

        # zerowe warunki początkowe

    def biegun(self):
        self.biegun = -(self.R + self.R2) / (self.R * self.R2 * self.C)
        return self.biegun

    def wybor_IN(self, label,time, A, w):
        t = np.arange(0, time, dt)  # start, stop, step
        IN1 = A * signal.square(w * t) #prostokatny
        IN2 = A * signal.sawtooth(w * t, 0.5)  # 0,5 daje trójkątny, 1 dawało by piłokształtny
        IN3 = A * np.sin(w*t)

        wybor = {'sygnał prostokątny':IN1, 'sygnał trójkątny':IN2, 'sygnał harmoniczy':IN3}
        self.IN = wybor[label] 

    def radio(self):
        rax = plt.axes([0.01, 0.6, 0.3, 0.2])
        #pltradio = plt.subplot(221)
        wybor_sygnalu = RadioButtons(rax, ('sygnał prostokątny', 'sygnał trójkątny', 'sygnał harmoniczy'))
        plt.draw()
        wybor_sygnalu.on_clicked(wybor_IN)


    def bode(self):
        self.sys = signal.TransferFunction([self.R], [self.R * self.R2 * self.C, self.R + self.R2])
        w, mag, phase = signal.bode(self.sys)
        plt.suptitle('Uklad') #glowna nazwa
        plt1 = plt.subplot(232) #subplotem tworzymy mniejsze miejsca na wykres - liczba 2 2 1 oznacza kolejno 2 rzedy, 2 kolumny i ktora kolumna ma byc na ten wykres przeznaczona
        plt1.set_title('Phase')
        #plt1.tick_params('x', labelbottom=False) #nie podpisuje osi ox
        plt.semilogx(w, phase)  # Bode phase plot
        plt2 = plt.subplot(233)
        plt2.set_title('Magnitude')
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.tight_layout()



    def sygnal(self, time, A, w, dt):
        t = np.arange(0, time, dt)  # start, stop, step
        # plt.plot(t, signal.square(w*t))
        # plt.figure()
        plt3 = plt.subplot(235)
        plt.plot(t, self.IN) #tutaj zrobimy zmiane ktorego IN wybieramy
        plt3.set_title('IN') #nazwa
        plt.tight_layout() #to oddala od siebie wykresy zeby nic na siebie nie nachodzilo

        ##tutaj niech będą ify decydujace o wyjściu
        
       # return IN
    
        
    

   
        
    

    def wyjscie(self, time, IN, dt):
        t = np.arange(0, time, dt)
        oryginal_transmitancji = self.R*exp(-(t*(self.R + self.R2))/(self.C*self.R*self.R2))/(self.R + self.R2) - self.R/(self.R + self.R2)
        OUT = np.convolve(IN,oryginal_transmitancji)
        plt4 = plt.subplot(236)
        plt.plot(0)
        plt4.set_title('OUT')
        plt.tight_layout() 


###################################################


RLC = [10, 1, 15, 20, 1]  # R, L, R2, C, U
time = 100
dt = 0.25
A = 2
w = 1
uklad = Uklad(RLC)

uklad.radio()

uklad.bode()
IN = uklad.sygnal(time, A, w, dt) 
uklad.wyjscie(time, IN, dt)
plt.show()

#print("kompilacja udana")

###################################################


# sys = signal.TransferFunction([1], [1, 2])
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html

# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/stable/gallery/widgets/buttons.html#sphx-glr-gallery-widgets-buttons-py
# https://www.youtube.com/watch?v=u5VCZBUNOcA
# https://matplotlib.org/stable/gallery/widgets/buttons.html buttony
# https://matplotlib.org/stable/gallery/widgets/textbox.html textbox
# https://matplotlib.org/stable/gallery/widgets/radio_buttons.html radio buttons
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html sygnał prostokątny
# https://matplotlib.org/3.1.1/gallery/userdemo/demo_gridspec01.html#sphx-glr-gallery-userdemo-demo-gridspec01-py jak zrobic mozaike z wejsc/wyjsc
# https://www.python-graph-gallery.com/194-split-the-graphic-window-with-subplot
# https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/shared_axis_demo.html#sphx-glr-gallery-subplots-axes-and-figures-shared-axis-demo-py
# https://matplotlib.org/stable/gallery/animation/multiple_axes.html#sphx-glr-gallery-animation-multiple-axes-py
