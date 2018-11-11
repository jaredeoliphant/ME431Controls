import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import msdParam as P
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from plotData import plotData

firstsignal = signalGenerator(amplitude=0.1, frequency=.6)


##dataPlot = plotData()
animation = msdAnimation()


t = P.t_start
while t < P.t_end:
    z = 0.4 + firstsignal.sin(t)
    animation.drawMSD([z])
#    dataPlot.updatePlots()
    t = t + P.t_plot
    plt.pause(0.1)

print('Press key to close')
plt.waitforbuttonpress()
plt.close()
