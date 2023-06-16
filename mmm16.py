from scipy import signal
import numpy as np
from numpy import exp as exp
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button













fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.3, bottom=0.2)

axs[0, 0].set_ylabel('Phase')
axs[0, 0].set_xlabel('f')

axs[0, 1].set_ylabel('U_IN [V]')
axs[0, 1].set_xlabel('t [s]')

axs[1, 0].set_ylabel('Mag')
axs[1, 0].set_xlabel('f')

axs[1, 1].set_ylabel('U_OUT [V]')
axs[1, 1].set_xlabel('t [s]')