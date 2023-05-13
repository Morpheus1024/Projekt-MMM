from cgitb import reset
from scipy import signal
import numpy as np
from numpy import exp as exp, ndarray
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons, TextBox
from matplotlib.widgets import Button as Button

R, L, R2, C, U = 10, 1, 15, 20, 1
time = 100
dt = 0.1
A = 2
w = 1
t = np.arange(0, time, dt)
IN1 = A*signal.square(w * t)
IN2 = A*signal.sawtooth(w * t, 0.5)
IN3 = A*np.sin(w * t)

choice = "IN1"

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.4, wspace=0.35, hspace=0.32, right=0.95)

rax = plt.axes([0.02, 0.65, 0.28, 0.18])
radio_button = RadioButtons(rax, ('Syg. Prostokątny','Syg. Trójkątny','Syg. harmoniczny'))




sys = signal.TransferFunction([R], [R * R2 * C, R + R2])
w, mag, phase = signal.bode(sys)


axs[0, 0].set_title('Phase')
axs[1, 0].set_title('Mag')
axs[0, 1].set_title('IN')
axs[1, 1].set_title('OUT')

oryginal_transmitancji = R * exp(-(t * (R + R2)) / (C * R * R2)) / (R + R2) - R / (R + R2)

def clear_plot():
    axs[0,0].clear()
    axs[0,1].clear()
    axs[1,0].clear()
    axs[1,1].clear()
    axs[0, 0].set_title('Phase')
    axs[1, 0].set_title('Mag')
    axs[0, 1].set_title('IN')
    axs[1, 1].set_title('OUT')

def refresh_IN():
    t = np.arange(0, time, dt)
    IN1 = A*signal.square(w * t)
    IN2 = A*signal.sawtooth(w * t, 0.5)
    IN3 = A*np.sin(w * t)
    if(choice=='IN1'): IN=IN1
    elif(choice=='IN2'): IN=IN2
    elif(choice=='IN3'): IN=IN3
    refresh_OUT()
    plt.show()

def refresh_OUT():
    oryginal_transmitancji = R * exp(-(t * (R + R2)) / (C * R * R2)) / (R + R2) - R / (R + R2)
    OUT = np.convolve(IN,oryginal_transmitancji)
    clear_plot()
    line1 = axs[0, 0].semilogx(w, phase)
    line2 = axs[1, 0].semilogx(w, mag)
    line3 = axs[0, 1].plot(IN)
    line4 = axs[1, 1].plot(OUT)
    plt.show()

def IN_choice(label):
    t = np.arange(0, time, dt)
    IN1 = A*signal.square(w * t)
    IN2 = A*signal.sawtooth(w * t, 0.5)
    IN3 = A*np.sin(w * t)
    IN_string = {'Syg. Prostokątny':IN1,'Syg. Trójkątny':IN2,'Syg. harmoniczny':IN3}
    choice_string = {'Syg. Prostokątny':'IN1','Syg. Trójkątny':'IN2','Syg. harmoniczny':'IN3'}
    IN =IN_string[label]
    choice = choice_string[label]
    refresh_OUT()

def refresh_R(expression):
    R=expression
    refresh_OUT()

def refresh_R2(expression):
    R2=expression
    refresh_OUT()

def refresh_L(expression):
    L=expression
    refresh_OUT()

def refresh_C(expression):
    C=expression
    refresh_OUT()

def refresh_A(expression):
    A=expression
    refresh_IN()

def refresh_w(expression):
    w=expression
    refresh_IN()

def refresh_time(expression):
    time=expression
    refresh_IN()

def refresh_dt(expression):
    dt_box=expression
    refresh_IN()



A_box =plt.axes([0.2, 0.51, 0.09, 0.05])
w_box =plt.axes([0.2, 0.40, 0.09, 0.05])
dt_box =plt.axes([0.2, 0.29, 0.09, 0.05])
time_box =plt.axes([0.2, 0.17, 0.09, 0.05])
A_textbox = TextBox(A_box, "A:", textalignment="center")
w_textbox = TextBox(w_box, "w:", textalignment="center")
dt_textbox = TextBox(dt_box, "dt:", textalignment="center")
time_textbox = TextBox(time_box, "t:", textalignment="center")

R_box=plt.axes([0.04,0.51,0.09,0.05])
R2_box=plt.axes([0.04,0.4,0.09,0.05])
L_box=plt.axes([0.04,0.29,0.09,0.05])
C_box=plt.axes([0.04,0.17,0.09,0.05])

R_textbox = TextBox(R_box, "R:", textalignment="center")
R2_textbox = TextBox(R2_box, "R2:", textalignment="center")
L_textbox = TextBox(L_box, "L:", textalignment="center")
C_textbox = TextBox(C_box, "C:", textalignment="center")

'''resetax = fig.add_axes([0.2, 0.04, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

plot = fig.add_axes([0.04, 0.04, 0.1, 0.04])
button_plot = Button(plot, 'Plot', hovercolor='0.975')'''


####pierwsze wywołanie


R_textbox.set_val("10")
C_textbox.set_val("1")
R2_textbox.set_val("15")
L_textbox.set_val("20")
A_textbox.set_val("2")
w_textbox.set_val("1")
dt_textbox.set_val("0.1")
time_textbox.set_val("100")
IN = IN2
OUT = np.convolve(IN,oryginal_transmitancji)

clear_plot()
refresh_OUT()

radio_button.on_clicked(IN_choice)
R_textbox.on_text_change(refresh_R)
R2_textbox.on_text_change(refresh_R2)
C_textbox.on_text_change(refresh_C)
L_textbox.on_text_change(refresh_L)
A_textbox.on_text_change(refresh_A)
w_textbox.on_text_change(refresh_w)
dt_textbox.on_text_change(refresh_dt)
time_textbox.on_text_change(refresh_time)

plt.show()