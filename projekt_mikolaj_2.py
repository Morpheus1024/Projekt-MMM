from cgitb import reset

from scipy import signal
import numpy as np
from numpy import exp as exp, ndarray
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons, TextBox
from matplotlib.widgets import Button as Button








###########################################
#kod co się wykonuje
###########################################

#rysowanie jak wszystko jest na początku

R = 0
L = 0
R2 = 0
C = 0
A = 0
w = 0
time = 0
dt = 0
IN_choise=0

rax = plt.axes([0.02, 0.65, 0.28, 0.18])
radio_button = RadioButtons(rax, ('Syg. Prostokątny','Syg. Trójkątny','Syg. harmoniczny'))

# left, bottom, width, height values
#textboxy
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

#button
plot_butt=plt.axes([0.02,0.07,0.28,0.05])
plot_button=Button(plot_butt, 'Plot', hovercolor='0.975')

#Bode
#plt.suptitle('Uklad')
plt_Bode_A = plt.subplot(232)
plt_Bode_A.set_title('Bode Magnitude')

plt_Bode_p = plt.subplot(235)
plt_Bode_p.set_title('Bode Phase')
plt.tight_layout()

#IN
plt_IN=plt.subplot(233)
plt_IN.set_title('Input')

#OUT
plt_OUT=plt.subplot(236)
plt_OUT.set_title('Output')

plt.show()

def change_R(txt_input):
    R.set_ydata(txt_input)

R_textbox.on_submit(change_R)

def change_C(txt_input):
    C.set_ydata(txt_input)

C_textbox.on_submit(change_C)

def change_R2(txt_input):
    R2.set_ydata(txt_input)

R2_textbox.on_submit(change_R2)

def change_L(txt_input):
    L.set_ydata(txt_input)

L_textbox.on_submit(change_L)

def change_A(txt_input):
    A.set_ydata(txt_input)

A_textbox.on_submit(change_A)

def change_w(txt_input):
    w.set_ydata(txt_input)

w_textbox.on_submit(change_w)

def change_dt(txt_input):
    dt.set_ydata(txt_input)

dt_textbox.on_submit(change_dt)

def change_time(txt_input):
    time.set_ydata(txt_input)

time_textbox.on_submit(change_time)

def IN_choise(txt_input):
    IN_choise={'Syg. Prostokątny':1, 'Syg. Trójkątny':2,'Syg. harmoniczny':3}

radio_button.on_clicked(IN_choise)


def plot(event):
    t=np.arange(0,time,dt)
    if IN_choise==1: IN = signal.square(w * t)
    elif IN_choise==2: IN=signal.sawtooth(w * t, 0.5)
    elif IN_choise==3: IN=np.sin(w * t)

    sys=signal.TransferFunction([R], [R * R2 * C, R + R2])
    w, mag, phase = signal.bode(sys)
    plt_Bode_p = plt.subplot(235) 
    plt_Bode_p.set_title('Phase')
    plt.semilogx(w, phase)  
    plt_Bode_A = plt.subplot(232)
    plt_Bode_A.set_title('Magnitude')
    plt.semilogx(w, mag) 
    plt.tight_layout()

    plt_IN = plt.subplot(233)
    plt.plot(t, IN) 
    plt_IN.set_title('IN') 
    plt.tight_layout()

    oryginal_transmitancji = R*exp(-(t*(R + R2))/(C*R*R2))/(R + R2) - R/(R + R2)
    OUT = np.convolve(IN,oryginal_transmitancji)
    plt_OUT = plt.subplot(236)
    plt.plot(OUT)
    plt_OUT.set_title('OUT')
    plt.tight_layout() 

    plt.show()

    

plot_button.on_clicked(plot)







