import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import bobParam as P
from signalGenerator import signalGenerator
from bobAnimation import bobAnimation
from plotData import plotData
from bobDynamics import bobDynamics
from bobControllerSS import bobControllerSS

refsig = signalGenerator(amplitude=0.25/2, frequency=0.1)
ctrl = bobControllerSS()
bob = bobDynamics()


animation = bobAnimation()
dataPlot = plotData()

t = P.t_start
while t < P.t_end:

    ref_input = refsig.square(t) + 0.25
    t_next_plot = t+P.t_plot
    
    while t < t_next_plot:

        F = ctrl.u(ref_input, bob.states())
        bob.propagateDynamics(F)
        t = t+P.Ts


    
    animation.drawbob(bob.states())
    dataPlot.updatePlots(t, ref_input, bob.states(), F)
                
        

    plt.pause(0.0001)

##
##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()

