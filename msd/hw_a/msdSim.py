import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import msdParam as P
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from plotData_msd import plotData_msd


## start up the signalGenerator(s)
firstsignal = signalGenerator(amplitude=0.1, frequency=.6)


## start up the plotData class and the msdAnimation class
dataPlot = plotData_msd()
animation = msdAnimation()



## main animation and simulation loop
t = P.t_start
while t < P.t_end:

    ## location of the MSD (z) is generated
    z = firstsignal.sin(t)

    ## update the animation
    animation.drawMSD([z])

    ## update the data plots
    dataPlot.updatePlots(t,z,[z],z)

    ## increment time and pause
    t = t + P.t_plot
    plt.pause(0.1)


    
## end conditions
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
