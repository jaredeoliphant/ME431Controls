import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData import plotData

firstsignal = signalGenerator(amplitude=.25, frequency=.6)
slowersignal = signalGenerator(amplitude = .25, frequency=.1)


##dataPlot = plotData()
animation = vtolAnimation()


t = P.t_start
while t < P.t_end:
    zv = .6+firstsignal.sin(.5*t)
    h = 1+slowersignal.sawtooth(t)
    theta = firstsignal.sin(t)
    ##theta = np.pi   ## in radians!
    zt = 1+firstsignal.sin(.2*t)
    animation.drawVtol([zv,h,theta,zt])
    #    dataPlot.updatePlots()
    t = t + P.t_plot
    plt.pause(0.1)

print('Press key to close')
plt.show()
##plt.waitforbuttonpress()
##plt.close()
