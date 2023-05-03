from cgitb import reset
from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import RadioButtons

class Uklad:

    def __init__(self, lista_IN):
        self.IN = None
        self.amp_slider = Slider
        self.axamp = None
        self.line1 = None
        self.R = lista_IN[0]
        self.L = lista_IN[1]
        self.R2 = lista_IN[2]
        self.C = lista_IN[3]
        self.U = lista_IN[4]
        self.biegun = None
        self.Y_string = ''
        self.transmitancja = ' Y/U = -R/(R+R2+sRCR2)'
        fig = plt.figure(figsize=[10, 7])
        self.fig = fig
        fig.subplots_adjust(left=0.2, bottom=0.2)
        gs = fig.add_gridspec(2, 2)
        self.gs = gs

    def rysowanko(self, IN, time, dt):
        t = np.arange(0, time, dt)
        ax3 = self.fig.add_subplot(self.gs[0, 1])
        line1 = plt.plot(t, self.mnozenie_plot(IN, amp_slider.val))

    def bode(self):
        self.sys = signal.TransferFunction([self.R], [self.R * self.R2 * self.C, self.R + self.R2])
        w, mag, phase = signal.bode(self.sys)
        ax1 = self.fig.add_subplot(self.gs[0, 0])
        plt.semilogx(w, phase)
        ax2 = self.fig.add_subplot(self.gs[1, 0])
        plt.semilogx(w, mag)

    def mnozenie_plot(self, IN, A):
        wynik = IN*A
        return wynik


    def sygnal(self, time, A, w, dt):
        t = np.arange(0, time, dt)
        IN1 = signal.square(w * t)
        self.IN1 = IN1
        IN2 = signal.sawtooth(w * t, 0.5)
        self.IN2 = IN2
        IN3 = np.sin(t)
        self.IN3 = IN3
        ax3 = self.fig.add_subplot(self.gs[0, 1])
        ax3.set_title('IN')
        IN = IN1
        self.IN = IN

        return IN
    def wyjscie(self, time, IN, dt):
        t = np.arange(0, time, dt)
        OUT = IN * ((self.R * exp(-(t * (self.R + self.R2)) / (self.C * self.R * self.R2))) / (
                    self.R + self.R2) - self.R / (self.R + self.R2))
        # oryginał transmitancji: (R*exp(-(t*(R + R2))/(C*R*R2)))/(R + R2) - R/(R + R2)
        ax4 = self.fig.add_subplot(self.gs[1, 1])
        plt.plot(t, OUT)
        ax4.set_title('OUT')
        #plt.tight_layout()

    ###################################################


RLC = [10, 1, 15, 20, 1]  # R, L, R2, C, U
time = 100
dt = 0.1
A = 2
w = 1
uklad = Uklad(RLC)
uklad.bode()
IN = uklad.sygnal(time, A, w, dt)
uklad.rysowanko(IN, time, dt)
axamp = uklad.fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
        ax=axamp,
        label="Amplitude",
        valmin=0,
        valmax=10,
        valinit=A,
        orientation="vertical"
    )
amp_slider.on_changed(uklad.rysowanko(IN, time, dt))
uklad.wyjscie(time, IN, dt)
uklad.mnozenie_plot(IN, A)
plt.show()
###################################################
