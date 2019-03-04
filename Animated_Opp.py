__author__ = "Reyann Larkey"
__email__ = "reyann.joiner@montana.edu"
__date__ = "March 3, 2019"

'''
This is an interactive wave plotting program that shows the interactions between two waves traveling 
in the opposite directions. 
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.animation as animation
plt.style.use('dark_background')

# Set up the plotting area
fig, ax = plt.subplots(1, figsize = (8,8))

# Give the plot a title
fig.suptitle("Moving in Opposite Directions", color = 'white', fontsize = 24, fontweight = 10)


# Setting up the x and y limits
for ax in [ax]: # Doesn't needt to be a for loop but if more suplots are added, then this is nice
    ax.set_ylim([-20, 20])
    ax.set_xlim([0, 1])

# Move the subplot(s) up to make room for buttons and sliders
plt.subplots_adjust(bottom=0.3)




#-----------------Make initial waves---------------------
x0 = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
time_array = np.arange(0, 50, 0.1)

def update_data(amp = 0.5,wavelen = 2, speed  =1):
    global a, si, co
    a = []
    si = []
    co = []
    for i, item in enumerate(time_array):
        s = amp * np.cos((2*np.pi/wavelen)*(x0 + speed*item))
        c = 1 * np.cos((2*np.pi/2)*(x0 - 0.5*item))
        a.append((s+c))
        si.append(s)
        co.append(c)


k = 0
def animate(k):
    x = a[k]
    k += 1
    ax.clear()
    ax.plot(x0, x, color='cyan')  # Amplitude
    ax.plot(x0, 0.25 * x**2 + 1.15, color='yellow')  # Intensity
    ax.plot(x0, si[k], color='red')  # Reference
    ax.plot(x0, co[k], color='green')  # Object
    ax.legend(('Amplitude', 'Intensity', 'Reference', 'Object'), loc = 'upper right')
    ax.grid(True)
    ax.set_ylim([-5,5])

anim = animation.FuncAnimation(fig, animate, frames=360, interval=20, fargs=(k))


update_data()
# --------------------------------------------------------





# ------------------set up sliders -----------------------
axcolor = 'darkgray' # color of unfilled sliders


# amplitude, wavelength and speed slider locations
axamp = plt.axes([0.125, 0.20, 0.775, 0.03], facecolor=axcolor)
axlen = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor=axcolor)
axspeed = plt.axes([0.125, 0.10, 0.775, 0.03], facecolor=axcolor)

# actual sliders
wamp = Slider(axamp, 'Amp.', 0.1, 2.0, valinit=0.5, color = 'red')
wlen = Slider(axlen, '$\lambda$', 0.1, 10.0, valinit=2, color = 'red')
wspeed = Slider(axspeed, 'v', 0, 5.0, valinit=1, color = 'red')


# function that actually gets called when a slider changes
def update(val):
    amp = wamp.val
    len = wlen.val
    speed = wspeed.val
    update_data(amp = amp, wavelen = len, speed = speed) # makes new data with updated parameters
    fig.canvas.draw_idle()

wamp.on_changed(update)
wlen.on_changed(update)
wspeed.on_changed(update)


# -------------------reset button------------------------
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='navy')
def reset(event):
    wamp.reset()
    wlen.reset()
    wspeed.reset()
button.on_clicked(reset)

# show the plot!
plt.show()

