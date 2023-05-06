from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox

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

axs[0, 0].set_ylabel('Phase')
axs[1, 0].set_xlabel('Mag')
axs[0, 1].set_ylabel('IN')
axs[1, 1].set_xlabel('OUT')

IN = IN1
def mnozenie(IN_X, A_X):
    IN = IN_X * A_X
    return IN


oryginal_transmitancji = R * exp(-(t * (R + R2)) / (C * R * R2)) / (R + R2) - R / (R + R2)
OUT = np.convolve(IN, oryginal_transmitancji)

def rysowanie_plotow(event):
    axs[0, 0].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 1].clear()
    line1, = axs[0, 0].semilogx(w, phase)
    line2, = axs[1, 0].semilogx(w, mag)
    line3 = axs[0, 1].plot(t, mnozenie(IN, amp_slider.val))
    OUT = np.convolve(mnozenie(IN, amp_slider.val), oryginal_transmitancji)
    line4 = axs[1, 1].plot(OUT)
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')
    plt.show()

def rysowanie_plotow2(expression):
    axs[0, 0].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 1].clear()
    line1, = axs[0, 0].semilogx(w, phase)
    line2, = axs[1, 0].semilogx(w, mag)
    A = eval(expression)
    line3 = axs[0, 1].plot(t, mnozenie(IN, A))
    OUT = np.convolve(mnozenie(IN, A), oryginal_transmitancji)
    line4 = axs[1, 1].plot(OUT)
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')
    plt.show()


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
    line3 = axs[0, 1].plot(t, mnozenie(IN, amp_slider.val))
    axs[1, 1].clear()
    line4 = axs[1, 1].plot(np.convolve(mnozenie(IN, amp_slider.val), oryginal_transmitancji))
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')



axbox = fig.add_axes([0.12, 0.05, 0.15, 0.075])
text_box = TextBox(axbox, "Amplitude", textalignment="center")

text_box.set_val("2")  # Trigger `submit` with the initial string.


resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

plot = fig.add_axes([0.6, 0.025, 0.1, 0.04])
button_plot = Button(plot, 'Plot', hovercolor='0.975')

def reset(event):
    amp_slider.reset()


button.on_clicked(reset)
button_plot.on_clicked(rysowanie_plotow)
text_box.on_submit(rysowanie_plotow2)
amp_slider.on_changed(update)

plt.show()
