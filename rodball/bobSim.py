import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import bobParam as P
from signalGenerator import signalGenerator
from bobAnimation import bobAnimation
from plotData import plotData

firstsignal = signalGenerator(amplitude=0.1, frequency=.6)


##dataPlot = plotData()
animation = bobAnimation()


t = P.t_start
while t < P.t_end:
    z = .4 + firstsignal.sawtooth(t)
    theta = firstsignal.sin(.3*t)
    animation.drawbob([z,theta])
    #    dataPlot.updatePlots()
    t = t + P.t_plot
    plt.pause(0.1)

print('Press key to close')
plt.show()
##plt.waitforbuttonpress()
##plt.close()
