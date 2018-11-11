import matplotlib.pyplot as plt
import sys
sys.path.append('..')
import msdParam as P
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from plotData_msd import plotData_msd
from msdDynamics import msdDynamics
from msdController import msdController

ctrl = msdController()
msd = msdDynamics()
reference = signalGenerator(amplitude = 1.0/2.0, frequency=0.05)


choice = int(input('animate(1) or plot(2)?'))
if choice == 1:
    animation = msdAnimation()
elif choice == 2:
    dataPlot = plotData_msd()

t = P.t_start
while t < P.t_end:
    ref_input = reference.square(t)+.5
    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        
        F = ctrl.u(ref_input, msd.states())
##        print('F ',F)
        msd.propagateDynamics(F)
        t = t + P.Ts

    if choice == 1:
        animation.drawMSD(msd.states())
    elif choice == 2:
        dataPlot.updatePlots(t, ref_input, msd.states(), F)
        
    plt.pause(0.0001)

##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()
