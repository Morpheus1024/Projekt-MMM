from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


#wykresy
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.08, bottom=0.30, right=0.98, top=0.99, wspace=0.25, hspace=0.25)

axs[0, 0].set_ylabel('Phase')
axs[0, 0].set_xlabel('f')

axs[0, 1].set_ylabel('U_IN [V]')
axs[0, 1].set_xlabel('t [s]')

axs[1, 0].set_ylabel('Mag')
axs[1, 0].set_xlabel('f')

axs[1, 1].set_ylabel('U_OUT [V]')
axs[1, 1].set_xlabel('t [s]')




wartosci_BODE = [10, 15, 1, 20]
wartosci_IN = [2, 100, 100, 1]

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
R_box = TextBox(Rax, "R [Ω]", textalignment="center")
R_box.set_val(10)  # Trigger `submit` with the initial string.
R_box.on_submit(lambda val: wart_R(val))

R2ax = fig.add_axes([0.32, 0.15, 0.10, 0.075])
R2_box = TextBox(R2ax, "R2 [Ω]", textalignment="center")
R2_box.set_val(15)  # Trigger `submit` with the initial string.
R2_box.on_submit(lambda val: wart_R2(val))

Lax = fig.add_axes([0.57, 0.15, 0.10, 0.075])
L_box = TextBox(Lax, "L [uH]", textalignment="center")
L_box.set_val(1)  # Trigger `submit` with the initial string.
L_box.on_submit(lambda val: wart_L(val))

Cax = fig.add_axes([0.80, 0.15, 0.10, 0.075])
C_box = TextBox(Cax, "C [uF]", textalignment="center")
C_box.set_val(20)  # Trigger `submit` with the initial string.
C_box.on_submit(lambda val: wart_C(val))



IN1_butt_box=fig.add_axes([0.0625, 0.01, 0.25, 0.04])
IN1_button = Button(IN1_butt_box,'Syg. prosto.')

IN2_butt_box=fig.add_axes([0.375, 0.01, 0.25, 0.04])
IN2_button = Button(IN2_butt_box,'Syg. trójkąt.')

IN3_butt_box=fig.add_axes([0.6875, 0.01, 0.25, 0.04])
IN3_button = Button(IN3_butt_box,'Syg. harmon,')


plt.show()