from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

def f_IN1(amp, w, time, dt):

    amp = float(amp)
    w = float(w)
    time = float(time)
    dt = float(dt)

    axs[0, 1].clear()
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN1 = amp * signal.square(w * t)
    line3 = axs[0, 1].plot(IN1)
    return IN1

def f_IN2(amp, w, time, dt):

    amp = float(amp)
    w = float(w)
    time = float(time)
    dt = float(dt)

    axs[0, 1].clear()
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN2 = amp * signal.sawtooth(w * t, 0.5)
    line3 = axs[0, 1].plot(t, IN2)
    return IN2

def f_IN3(amp, w, time, dt):

    amp = float(amp)
    w = float(w)
    time = float(time)
    dt = float(dt)

    axs[0, 1].clear()
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN3 = amp * np.sin(w * t)
    line3 = axs[0, 1].plot(t, IN3)
    return IN3

def f_sys(R, R2, C):
    sys = signal.TransferFunction([R], [-(R * R2 * C), R + R2])
    w1, mag, phase = signal.bode(sys)
    return w1, mag, phase

def wart_amp(val):
    wartosci_IN[0] = eval(val)
    rysowanie_plotow1()

def wart_time(val):
    wartosci_IN[1] = eval(val)
    rysowanie_plotow1()

def wart_dt(val):
    wartosci_IN[2] = eval(val)
    rysowanie_plotow1()

def wart_w(val):
    wartosci_IN[3] = eval(val)
    rysowanie_plotow1()

def wart_R(val):
    wartosci_BODE[0] = eval(val)
    rysowanie_plotow1()

def wart_L(val):
    wartosci_BODE[1] = eval(val)
    rysowanie_plotow1()

def wart_R2(val):
    wartosci_BODE[2] = eval(val)
    rysowanie_plotow1()

def wart_C(val):
    wartosci_BODE[3] = eval(val)
    rysowanie_plotow1()

def f_OUT(w, amp, R, time, dt, C, R2, f):

    w = float(w)
    amp = float(amp)
    R = float(R)
    R2 = float(R2)
    time = float(time)
    dt = float(dt)
    C = float(C)

    t = np.arange(0, time, dt)
    oryginal_transmitancji = R * exp(-(t * (R + R2)) / -(C * R * R2)) / (R + R2) - R / (R + R2)
    if f == 1:
        line4 = axs[1, 1].plot(np.convolve(f_IN1(amp, w, time, dt), oryginal_transmitancji))
    elif f == 2:
        line4 = axs[1, 1].plot(np.convolve(f_IN2(amp, w, time, dt), oryginal_transmitancji))
    else:
        line4 = axs[1, 1].plot(np.convolve(f_IN3(amp, w, time, dt), oryginal_transmitancji))

def rysowanie_bode(R, R2, C):

    R = float(R)
    R2 = float(R2)
    C = float(C)

    w1, mag, phase = f_sys(R, R2, C)
    line1 = axs[0, 0].semilogx(w1, phase)
    line2 = axs[1, 0].semilogx(w1, mag)

def rysowanie_plotow1(f=None):
    print('po raz drugi', wartosci_IN)
    amp = wartosci_IN[0]
    time = wartosci_IN[1]
    dt = wartosci_IN[2]
    w = wartosci_IN[3]
    R = wartosci_BODE[0]
    L = wartosci_BODE[1]
    R2 = wartosci_BODE[2]
    C = wartosci_BODE[3]
    axs[0, 0].clear()
    axs[0, 1].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    rysowanie_bode(R, R2, C)
    f_OUT(w, amp, R, time, dt, C, R2, f)
    axs[0, 0].set_ylabel('Phase')
    axs[0, 1].set_ylabel('IN')
    axs[1, 0].set_xlabel('Mag')
    axs[1, 1].set_xlabel('OUT')
    plt.show()

def on_IN1_button_clicked(event):
    rysowanie_plotow1(1)
    print('Syg. prosto.')

def on_IN2_button_clicked(event):
    rysowanie_plotow1(2)
    print('Syg. trójkąt.')

def on_IN3_button_clicked(event):
    rysowanie_plotow1(3)
    print('Syg. harmon.')

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.3, bottom=0.2)

axs[0, 0].set_ylabel('Phase')
axs[0, 1].set_ylabel('IN')
axs[1, 0].set_xlabel('Mag')
axs[1, 1].set_xlabel('OUT')

wartosci_BODE = [10, 15, 1, 20]
wartosci_IN = [2, 100, 0.1, 1]

axbox = fig.add_axes([0.13, 0.02, 0.15, 0.075])
amp_box = TextBox(axbox, "amplitude", textalignment="center")
amp_box.set_val(wartosci_IN[0])

timeax = fig.add_axes([0.35, 0.02, 0.15, 0.075])
time_box = TextBox(timeax, "time", textalignment="center")
time_box.set_val(wartosci_IN[1])

dtax = fig.add_axes([0.55, 0.02, 0.15, 0.075])
dt_box = TextBox(dtax, "dt", textalignment="center")
dt_box.set_val(wartosci_IN[2])

wax = fig.add_axes([0.75, 0.02, 0.15, 0.075])
w_box = TextBox(wax, "w", textalignment="center")
w_box.set_val(wartosci_IN[3])

Rax = fig.add_axes([0.05, 0.3, 0.15, 0.075])
R_box = TextBox(Rax, "R", textalignment="center")
R_box.set_val(wartosci_BODE[0])

R2ax = fig.add_axes([0.05, 0.5, 0.15, 0.075])
R2_box = TextBox(R2ax, "R2", textalignment="center")
R2_box.set_val(wartosci_BODE[1])

Lax = fig.add_axes([0.05, 0.4, 0.15, 0.075])
L_box = TextBox(Lax, "L", textalignment="center")
L_box.set_val(wartosci_BODE[2])

Cax = fig.add_axes([0.05, 0.2, 0.15, 0.075])
C_box = TextBox(Cax, "C", textalignment="center")
C_box.set_val(wartosci_BODE[3])

IN1_butt_box=fig.add_axes([0.03, 0.65, 0.18, 0.05])
IN1_button = Button(IN1_butt_box,'Syg. prosto.')

IN2_butt_box=fig.add_axes([0.03, 0.75, 0.18, 0.05])
IN2_button = Button(IN2_butt_box,'Syg. trójkąt.')

IN3_butt_box=fig.add_axes([0.03, 0.85, 0.18, 0.05])
IN3_button = Button(IN3_butt_box,'Syg. harmon,')

IN1_button.on_clicked(on_IN1_button_clicked)
IN2_button.on_clicked(on_IN2_button_clicked)
IN3_button.on_clicked(on_IN3_button_clicked)

rysowanie_plotow1(3)
plt.show()
