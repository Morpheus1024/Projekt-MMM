import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox

t = np.arange(-2.0, 2.0, 0.001)

class Index:
    ind = 0

def prev(self, event):
    self.ind -= 1

fig, ax = plt.subplots()
l, = ax.plot(t, np.zeros_like(t), lw=2) #grubosc linii
fig.subplots_adjust(left=0.3)

axcolor = 'lightblue' #kolor okienek
'''rax = fig.add_axes([0.05, 0.7, 0.15, 0.25], facecolor=axcolor)
radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
                     label_props={'color': 'cmy', 'fontsize': [12, 12, 12]},
                     radio_props={'s': [16, 16, 16]})

def hzfunc(label):
    hzdict = {'1 Hz': s0, '2 Hz': s1, '4 Hz': s2, "8 Hz": s3}
    ydata = hzdict[label]
    l.set_ydata(ydata)
    fig.canvas.draw()
radio.on_clicked(hzfunc)'''

rax = fig.add_axes([0.05, 0.5, 0.15, 0.15], facecolor=axcolor) #zmiana kolorow
radio2 = RadioButtons(
    rax, ('red', 'blue', 'green', 'pink'),
    label_props={'color': ['red', 'blue', 'green', 'pink']},
    radio_props={
        'facecolor': ['red', 'blue', 'green', 'pink'],
        'edgecolor': ['darkred', 'darkblue', 'darkgreen', 'pink'],
    })
def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw()
radio2.on_clicked(colorfunc)

rax = fig.add_axes([0.05, 0.35, 0.15, 0.15], facecolor=axcolor)
radio3 = RadioButtons(rax, ('-', '--', '-.', 'dotted'))
def stylefunc(label):
    l.set_linestyle(label)
    fig.canvas.draw()
radio3.on_clicked(stylefunc)

fig.subplots_adjust(bottom=0.2)

axprev = fig.add_axes([0.05, 0.8, 0.15, 0.15])
axnext = fig.add_axes([0.05, 0.65, 0.15, 0.15])
bnext = Button(axnext, 'Next')
bprev = Button(axprev, 'Previous')

def submit(expression):

    ydata = eval(expression)
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

axbox = fig.add_axes([0.15, 0.05, 0.7, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)

text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.


plt.show()