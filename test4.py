from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, RadioButtons

R, L, R2, C, U = 10, 1, 15, 20, 1
A = 2
time = 100
dt = 0.1


def f_IN1(A, w, time, dt):
    t = np.arange(0, time, dt)
    IN1 = signal.square(w * t)
    line4 = axs[0, 1].plot(t, IN1*A)
    return line4



def f_IN2(A, w, time, dt):
    t = np.arange(0, time, dt)
    IN2 = signal.sawtooth(w * t, 0.5)
    line4 = axs[0, 1].plot(t, IN2*A)
    return line4




def f_IN3(A, w, time, dt):
    t = np.arange(0, time, dt)
    IN3 = np.sin(w * t)
    line4 = axs[0, 1].plot(t, IN3*A)
    return line4


fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, bottom=0.2)

sys = signal.TransferFunction([R], [R * R2 * C, R + R2])
w, mag, phase = signal.bode(sys)

axs[0, 0].set_ylabel('Phase')
axs[1, 0].set_xlabel('Mag')
axs[0, 1].set_ylabel('IN')
axs[1, 1].set_xlabel('OUT')

wartosci_IN = [A, time, dt]
print(wartosci_IN)


def rysowanie_plotow_A(val):
    wartosci_IN[0] = eval(val)
    rysowanie_plotow1()


def rysowanie_plotow_time(val):
    wartosci_IN[1] = eval(val)
    rysowanie_plotow1()


def rysowanie_plotow_dt(val):
    wartosci_IN[2] = eval(val)
    rysowanie_plotow1()


def f_OUT(A, R, time, dt, C, R2):
    t = np.arange(0, time, dt)
    oryginal_transmitancji = R * exp(-(t * (R + R2)) / (C * R * R2)) / (R + R2) - R / (R + R2)
    line4 = axs[1, 1].plot(np.convolve(f_IN1(A, w, time, dt), oryginal_transmitancji))


def rysowanie_plotow1():
    print('po raz drugi', wartosci_IN)
    A = wartosci_IN[0]
    time = wartosci_IN[1]
    dt = wartosci_IN[2]
    axs[0, 0].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 1].clear()
    line1, = axs[0, 0].semilogx(w, phase)
    line2, = axs[1, 0].semilogx(w, mag)
    f_IN1(A, w, time, dt)
    f_OUT(A, R, time, dt, C, R2)
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')
    plt.show()


axbox = fig.add_axes([0.13, 0.02, 0.15, 0.075])
amp_box = TextBox(axbox, "amplitude", textalignment="center")
amp_box.set_val(2)  # Trigger `submit` with the initial string.
amp_box.on_submit(lambda val: rysowanie_plotow_A(val))

timeax = fig.add_axes([0.35, 0.02, 0.15, 0.075])
time_box = TextBox(timeax, "time", textalignment="center")
time_box.set_val(100)  # Trigger `submit` with the initial string.
time_box.on_submit(lambda val: rysowanie_plotow_time(val))

dtax = fig.add_axes([0.55, 0.02, 0.15, 0.075])
dt_box = TextBox(dtax, "dt", textalignment="center")
dt_box.set_val(0.1)  # Trigger `submit` with the initial string.
dt_box.on_submit(lambda val: rysowanie_plotow_dt(val))

plt.show()
