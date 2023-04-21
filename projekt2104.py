from scipy import signal
import numpy as np
from matplotlib.widgets import TextBox
from matplotlib import pyplot as plt
import pandas as pd


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

    def bode(self):
        self.sys = signal.TransferFunction([self.R], [self.R * self.R2 * self.C, self.R + self.R2])
        w, mag, phase = signal.bode(self.sys)
        #plt.suptitle('Bode plot')
        #plt1 = plt.subplot(211)
        #plt1.set_title('Phase')
        #plt1.tick_params('x', labelbottom=False)
        #plt.semilogx(w, phase)  # Bode phase plot
        #plt2 = plt.subplot(212)
        #plt2.set_title('Magnitude')
        #plt.semilogx(w, mag)  # Bode magnitude plot
        #plt.rcParams['figure.figsize'] = [10, 10]

        plt1 = plt.subplot2grid((4, 4), (0, 0), colspan=4)
        plt1.plot(data=plt.semilogx(w, phase), marker='o')

        plt2 = plt.subplot2grid((4, 4), (1, 0), colspan=4)
        plt2.plot(data=plt.semilogx(w, mag), marker='o')

        # def odp_harmoniczna(self, A, w):
        # IN = [A,w]

        # Y = A*R^2*sin(t*w) + A*R*R2*sin(t*w) - A*C*R^2*R2*w*cos(t*w))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2) + (A*C*R^2*R2*w*exp(-(t*(R + R2))/(C*R*R2)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
        # odp_harm (exp(-(t*(R + R2))/(C*R*R2))*(A*R^2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*R*R2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*C*R^2*R2*w - A*C*R^2*R2*w*exp((t*(R + R2))/(C*R*R2))*cos(t*w)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
        # mnożenie w dzieninie s to to samo co splot w dziedzinie t - numpy.convolution
        # R = self.R
        # R2 = self.R2
        # C = self.C

    def sygnal_prostokatny(self, A, w, time):
        A = 1
        w = 1
        t = np.arange(0, 10, 0.01)  # start, stop, step
        # plt.plot(t, signal.square(w*t))
        # plt.figure()
        IN = signal.square(w * t)
        # plt.plot(t,IN)
        # plt.show()
        #plt3 = plt.subplot(112)
        #plt3.set_title('IN')

        plt3 = plt.subplot2grid((4, 4), (2, 0), colspan=4)
        plt3.plot(data=plt.semilogx(w, w), marker='o')

        return IN

    def sygnal_trojkatny(self, A, w, time):
        A = 1
        w = 1
        t = np.arange(0, 10, 0.01)  # start, stop, step
        # plt.figure()
        IN = signal.sawtooth(w * t, 0.5)  # 0,5 daje trójkątny, 1 dawało by piłokształtny
        #plt3 = plt.subplot(112)
        #plt3.set_title('IN')

        plt3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
        plt3.plot('x_values', 'y_values', data=plt.semilogx(w, w), marker='-', alpha=0.4)
        return IN

    def sygnal_harmoniczny(self, A, w, time):
        A = 1
        w = 1
        t = np.arange(0, 100, 0.01)  # start, stop, step
        #plt3 = plt.subplot(112)
        #plt3.set_title('IN')
        plt3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
        plt3.plot('x_values', 'y_values', data=plt.semilogx(w, w), marker='-', alpha=0.4)

        IN = np.sin(t)
        return IN




RLC = [10, 1, 15, 20, 1]  # R, L, R2, C, U

uklad = Uklad(RLC)

uklad.bode()
uklad.sygnal_prostokatny(1, 1, 1)
plt.show()

print("kompilacja udana")

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