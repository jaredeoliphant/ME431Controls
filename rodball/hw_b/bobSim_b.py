import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import bobParam as P
from signalGenerator import signalGenerator
from bobAnimation import bobAnimation
from plotData import plotData
from bobDynamics import bobDynamics

firstsignal = signalGenerator(amplitude=0.1, frequency=.6)
bob = bobDynamics()

choice = int(input('animate(1) or plot(2)?'))
if choice == 1:
    animation = bobAnimation()
elif choice == 2:
    dataPlot = plotData()
else:
    animation = bobAnimation()
    dataPlot = plotData()

t = P.t_start
while t < P.t_end:

    
    ref_input = [0, 0]   # z and theta
    
    t_next_plot = t+P.t_plot
    
    while t < t_next_plot:
        ## F = 11.5149 ## near equillibrium is ball is halfway down the beam
        F = 23
        bob.propagateDynamics(F)
##        print(bob.states())
        t = t+P.Ts


        
    if choice == 1:
        animation.drawbob(bob.states())
    elif choice == 2:
        dataPlot.updatePlots(t, ref_input, bob.states(), F)
    else:
        animation.drawbob(bob.states())
        dataPlot.updatePlots(t, ref_input, bob.states(), F)
                
        

    plt.pause(0.0001)


print('Press key to close')
plt.waitforbuttonpress()
plt.close()

