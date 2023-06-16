from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


def f_IN1(A, w, time, dt):
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN1 = A * signal.square(w * t)
    line3 = axs[0, 1].plot(t, IN1)
    return IN1


def f_IN2(A, w, time, dt):
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN2 = A * signal.sawtooth(w * t, 0.5)
    line3 = axs[0, 1].plot(t, IN2)
    return IN2


def f_IN3(A, w, time, dt):
    t = np.arange(0, time, dt)
    w = np.array(w)
    IN3 = A * np.sin(w * t)
    line3 = axs[0, 1].plot(t, IN3)
    return IN3


fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.08, bottom=0.30, right=0.98, top=0.99, wspace=0.25, hspace=0.25)


def f_sys(R, R2, C):
    sys = signal.TransferFunction([R], [R * R2 * C, R + R2])
    w1, mag, phase = signal.bode(sys)
    return w1, mag, phase


axs[0, 0].set_ylabel('Phase')
axs[0, 0].set_xlabel('f')

axs[0, 1].set_ylabel('U_IN [V]')
axs[0, 1].set_xlabel('t [s]')

axs[1, 0].set_ylabel('Mag')
axs[1, 0].set_xlabel('f')

axs[1, 1].set_ylabel('U_OUT [V]')
axs[1, 1].set_xlabel('t [s]')

wartosci_BODE = [10, 1, 15, 20]
wartosci_IN = [2, 100, 0.1, 1]
print('tutaj sa wartosci poza funk', wartosci_IN)


def wart_A(val):
    wartosci_IN[0] = eval(val)


def wart_time(val):
    wartosci_IN[1] = eval(val)


def wart_dt(val): #milisekundy
    wartosci_IN[2] = eval(val)

def wart_w(val):
    wartosci_IN[3] = eval(val)


def wart_R(val):
    wartosci_BODE[0] = eval(val)


def wart_L(val): #mikrohenry
    wartosci_BODE[1] = eval(val)


def wart_R2(val):
    wartosci_BODE[2] = eval(val)


def wart_C(val): #mikrofarad
    wartosci_BODE[3] = eval(val)

def on_IN1_button_clicked(event):
    rysowanie_plotow1(1)
    print('Syg. prosto.')


def on_IN2_button_clicked(event):
    rysowanie_plotow1(2)
    print('Syg. trójkąt.')


def on_IN3_button_clicked(event):
    rysowanie_plotow1(3)
    print('Syg. harmon.')


def f_OUT(w, A, R, time, dt, C, R2, f):
    t = np.arange(0, time, dt, dtype=np.float128)
    oryginal_transmitancji = -exp((t * (R + R2)) / (C * R * R2)) / (C * R2)

    axs[0, 1].clear()
    axs[1, 1].clear()

    if f == 1:
        line4 = axs[1, 1].plot(t, np.convolve(oryginal_transmitancji, f_IN1(A, w, time, dt), mode='same'))

    elif f == 2:
        line4 = axs[1, 1].plot(t, np.convolve(oryginal_transmitancji, f_IN2(A, w, time, dt), mode='same'))

    else:
        line4 = axs[1, 1].plot(t, np.convolve(oryginal_transmitancji, f_IN3(A, w, time, dt), mode='same'))

def rysowanie_bode(R, R2, C):
    w1, mag, phase = f_sys(R, R2, C)
    line1 = axs[0, 0].semilogx(w1, phase)
    line2 = axs[1, 0].semilogx(w1, mag)


def rysowanie_plotow1(f):
    A = wartosci_IN[0]
    time = wartosci_IN[1]
    dt = wartosci_IN[2]
    w = wartosci_IN[3]
    R = wartosci_BODE[0]*1000
    L = wartosci_BODE[1]/1000
    R2 = wartosci_BODE[2]*1000
    C = wartosci_BODE[3]/1000
    print('wart w funk', wartosci_IN)
    axs[0, 0].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 1].clear()

    rysowanie_bode(R, R2, C)
    f_OUT(w, A, R, time, dt, C, R2, f)


    axs[0, 0].set_ylabel('Phase')
    axs[0, 0].set_xlabel('f')

    axs[0, 1].set_ylabel('U_IN [V]')
    axs[0, 1].set_xlabel('t [s]')

    axs[1, 0].set_ylabel('Mag')
    axs[1, 0].set_xlabel('f')

    axs[1, 1].set_ylabel('U_OUT [V]')
    axs[1, 1].set_xlabel('t [s]')
    plt.show()


axbox = fig.add_axes([0.07, 0.06, 0.10, 0.075])
amp_box = TextBox(axbox, "A [V] ", textalignment="center")
amp_box.set_val(2)
amp_box.on_submit(lambda val: wart_A(val))

timeax = fig.add_axes([0.32, 0.06, 0.10, 0.075])
time_box = TextBox(timeax, "time [s] ", textalignment="center")
time_box.set_val(100)  # Trigger `submit` with the initial string.
time_box.on_submit(lambda val: wart_time(val))

dtax = fig.add_axes([0.57, 0.06, 0.10, 0.075])
dt_box = TextBox(dtax, "dt [ms] ", textalignment="center")
dt_box.set_val(0.1)  # Trigger `submit` with the initial string.
dt_box.on_submit(lambda val: wart_dt(val))

wax = fig.add_axes([0.80, 0.06, 0.10, 0.075])
w_box = TextBox(wax, "ω [Hz] ", textalignment="center")
w_box.set_val(1)  # Trigger `submit` with the initial string.
w_box.on_submit(lambda val: wart_w(val))

Rax = fig.add_axes([0.07, 0.15, 0.10, 0.075])
R_box = TextBox(Rax, "R [kΩ]", textalignment="center")
R_box.set_val(10)  # Trigger `submit` with the initial string.
R_box.on_submit(lambda val: wart_R(val))

R2ax = fig.add_axes([0.32, 0.15, 0.10, 0.075])
R2_box = TextBox(R2ax, "R2 [kΩ]", textalignment="center")
R2_box.set_val(15)  # Trigger `submit` with the initial string.
R2_box.on_submit(lambda val: wart_R2(val))

Lax = fig.add_axes([0.57, 0.15, 0.10, 0.075])
L_box = TextBox(Lax, "L [mH]", textalignment="center")
L_box.set_val(1)  # Trigger `submit` with the initial string.
L_box.on_submit(lambda val: wart_L(val))

Cax = fig.add_axes([0.80, 0.15, 0.10, 0.075])
C_box = TextBox(Cax, "C [mF]", textalignment="center")
C_box.set_val(20)  # Trigger `submit` with the initial string.
C_box.on_submit(lambda val: wart_C(val))

IN1_butt_box = fig.add_axes([0.0625, 0.01, 0.25, 0.04])
IN1_button = Button(IN1_butt_box, 'Syg. prosto.')

IN2_butt_box = fig.add_axes([0.375, 0.01, 0.25, 0.04])
IN2_button = Button(IN2_butt_box, 'Syg. trójkąt.')

IN3_butt_box = fig.add_axes([0.6875, 0.01, 0.25, 0.04])
IN3_button = Button(IN3_butt_box, 'Syg. harmon.')

IN1_button.on_clicked(on_IN1_button_clicked)
IN2_button.on_clicked(on_IN2_button_clicked)
IN3_button.on_clicked(on_IN3_button_clicked)

plt.show()