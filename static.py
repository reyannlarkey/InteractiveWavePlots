import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


# One figure with 3 sublots (ax1, ax2, and ax3)
plt.style.use('dark_background')
fig, axes = plt.subplots(3, figsize = (8,8))
[ax1, ax2, ax3] = axes

# Give the plot a title
fig.suptitle("Wave Addition Example", color = 'white', fontsize = 24, fontweight = 10)


# Setting up the x and y limits
for ax in axes:
    ax.set_ylim([-20, 20])
    ax.set_xlim([0, 1])
    ax.axhline(y = 0, color = 'grey', linestyle = '--')

# give individual plots their labels
ax1.set_ylabel("Wave 1")
ax2.set_ylabel("Wave 2")
ax3.set_ylabel("Resulting")

# Move the three subplots up and to the left to make room for buttons and sliders
plt.subplots_adjust(left=0.3, bottom=0.25)




#-----------------Make initial waves---------------------
t = np.arange(0.0, 1.0, 0.001)
a1 = a2 = 5
f1 = f2 = 3

w1 = a1*np.sin(2*np.pi*f1*t)  # wave 1
w2 = a2*np.sin(2*np.pi*f2*t)  # wave 2
w3 = w1+w2                    # Resultant wave

l, = ax1.plot(t, w1, lw=2, color='red')    # line 1
l2, = ax2.plot(t, w2, lw=2, color='green') # line 2
l3, = ax3.plot(t, w3, lw=2, color='blue')  # line 3
# --------------------------------------------------------


# ------------------set up sliders -----------------------
axcolor = 'darkgray'


axfreq = plt.axes([0.3, 0.1, 0.6, 0.03], facecolor=axcolor)
axamp = plt.axes([0.3, 0.15, 0.6, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f1, color = 'red')
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a1, color = 'red')

def update(val): #updates the frequency and amplitude values
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    l3.set_ydata(l2.get_ydata() + amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)
#----------------------------------------------------------


#-------------------configure reset button-----------------
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='navy')
def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
#------------------------------------------------------------


#---------------Radio buttons (wave 2 select)----------------
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('Sine', 'Cosine', 'Gaussian'), active=0, activecolor='green')


def gaussian(x, mu, sig):
    return 10 * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def WaveFunc(label): #changes the wave being plotted in panel #2
    if label == 'Sine':
        l2.set_ydata(a1*np.sin(2*np.pi*f1*t))
    if label == 'Cosine':
        l2.set_ydata(a1*np.cos(2*np.pi*f1*t))
    elif label == "Gaussian":
        l2.set_ydata(gaussian(t, mu = 0.5, sig = 0.2))
    fig.canvas.draw_idle()
    update(samp.val)
radio.on_clicked(WaveFunc)
#------------------------------------------------------------


#display plot
plt.show()
