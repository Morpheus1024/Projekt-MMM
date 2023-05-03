from cgitb import reset
import button as button
from scipy import signal
import numpy as np
from numpy import exp as exp, ndarray
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import RadioButtons


R, L, R2, C, U = 10, 1, 15, 20, 1
time = 100
dt = 0.1
A = 2
w = 1
t = np.arange(0, time, dt)
IN1 = signal.square(w * t)
IN2 = signal.sawtooth(w * t, 0.5)
IN3 = np.sin(w * t)


fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, bottom=0.2)


sys = signal.TransferFunction([R], [R * R2 * C, R + R2])
w, mag, phase = signal.bode(sys)


line1, = axs[0, 0].semilogx(w, phase)
axs[0, 0].set_xlabel('Phase')


line2, = axs[1, 0].semilogx(w, phase)
axs[1, 0].set_xlabel('Mag')


IN = IN1


def mnozenie(IN_X, A_X):
    return IN_X * A_X


line3 = axs[0, 1].plot(t, mnozenie(IN, A))
axs[0, 1].set_xlabel('IN')


OUT = mnozenie(IN, A) * ((R * exp(-(t * (R + R2)) / (C * R * R2))) / (R + R2) - R / (R + R2))
line4 = axs[1, 1].plot(t, OUT)
axs[1, 1].set_xlabel('OUT')



axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=A,
    orientation="vertical"
)


def update(val):
    axs[0, 1].clear()
    axs[1, 1].clear()
    line3 = axs[0, 1].plot(t, mnozenie(IN, amp_slider.val))
    OUT = mnozenie(IN, amp_slider.val) * ((R * exp(-(t * (R + R2)) / (C * R * R2))) / (R + R2) - R / (R + R2))
    line4 = axs[1, 1].plot(t, OUT)


amp_slider.on_changed(update)


resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    amp_slider.reset()


button.on_clicked(reset)


plt.show()
