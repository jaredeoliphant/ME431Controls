import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import bobParam as P
from signalGenerator import signalGenerator
from bobAnimation import bobAnimation
from plotData import plotData
from bobDynamics import bobDynamics
from bobController import bobController

refsig = signalGenerator(amplitude=0.25/2, frequency=0.1)
ctrl = bobController()
bob = bobDynamics()

# choice = int(input('animate(1) or plot(2)?'))
choice = 3
if choice == 1:
    animation = bobAnimation()
elif choice == 2:
    dataPlot = plotData()
else:
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


        
    if choice == 1:
        animation.drawbob(bob.states())
    elif choice == 2:
        dataPlot.updatePlots(t, ref_input, bob.states(), F)
    else:
        animation.drawbob(bob.states())
        dataPlot.updatePlots(t, ref_input, bob.states(), F)
                
        

    plt.pause(0.0001)

##
##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()

