from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons

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
    A=2
    line3 = axs[0, 1].plot(t, mnozenie(IN, A))
    OUT = np.convolve(mnozenie(IN, A), oryginal_transmitancji)
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
    #A = eval(expression)
    line3 = axs[0, 1].plot(t, mnozenie(IN, A))
    OUT = np.convolve(mnozenie(IN, A), oryginal_transmitancji)
    line4 = axs[1, 1].plot(OUT)
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')
    plt.show()

def change_R(txt_input):
    R.eval(txt_input)
    rysowanie_plotow2()

def change_C(txt_input):
    C.eval(txt_input)
    rysowanie_plotow2()

def change_R2(txt_input):
    R2.eval(txt_input)
    rysowanie_plotow2()

def change_L(txt_input):
    L.eval(txt_input)
    rysowanie_plotow2()

def change_A(txt_input):
    A.eval(txt_input)
    rysowanie_plotow2()

def change_w(txt_input):
    w.eval(txt_input)
    rysowanie_plotow2()

def change_dt(txt_input):
    dt.eval(txt_input)
    rysowanie_plotow2()

def change_time(txt_input):
    time.eval(txt_input)
    rysowanie_plotow2()


'''axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=A,
    orientation="vertical"
)'''


def update(val):
    axs[0, 1].clear()
    line3 = axs[0, 1].plot(t, mnozenie(IN, A))
    axs[1, 1].clear()
    line4 = axs[1, 1].plot(np.convolve(mnozenie(IN, A), oryginal_transmitancji))
    axs[0, 0].set_ylabel('Phase')
    axs[1, 0].set_xlabel('Mag')
    axs[0, 1].set_ylabel('IN')
    axs[1, 1].set_xlabel('OUT')



#axbox = fig.add_axes([0.12, 0.05, 0.15, 0.075])
#text_box = TextBox(axbox, "Amplitude", textalignment="center")

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
#plot_butt=plt.axes([0.02,0.07,0.28,0.05])
#plot_button=Button(plot_butt, 'Plot', hovercolor='0.975')




#text_box.set_val("2")  # Trigger `submit` with the initial string.


resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

plot = fig.add_axes([0.6, 0.025, 0.1, 0.04])
button_plot = Button(plot, 'Plot', hovercolor='0.975')

#def reset(event):
#   amp_slider.reset()
R_textbox.set_val("10")
C_textbox.set_val("1")
R2_textbox.set_val("15")
L_textbox.set_val("20")
A_textbox.set_val("2")
w_textbox.set_val("1")
dt_textbox.set_val("0.1")
time_textbox.set_val("100")

#button.on_clicked(reset)
button_plot.on_clicked(rysowanie_plotow2)
#text_box.on_submit(rysowanie_plotow2)
R_textbox.on_submit(change_R)
C_textbox.on_submit(change_C)
R2_textbox.on_submit(change_R2)
L_textbox.on_submit(change_L)
A_textbox.on_submit(change_A)
w_textbox.on_submit(change_w)
dt_textbox.on_submit(change_dt)
time_textbox.on_submit(change_time)
#radio_button.on_clicked(IN_choise)
#amp_slider.on_changed(update)

plt.show()
