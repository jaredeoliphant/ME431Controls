import matplotlib.pyplot as plt
import sys
sys.path.append('..')
import msdParam as P
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from plotData_msd import plotData_msd
from msdDynamics import msdDynamics
from msdControllerSS import msdControllerSS

ctrl = msdControllerSS()
msd = msdDynamics()
reference = signalGenerator(amplitude = .5, frequency=0.05)


animation = msdAnimation()
dataPlot = plotData_msd()

t = P.t_start
while t < P.t_end:
    ref_input = reference.square(t)
    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        
        F = ctrl.u(ref_input, msd.states())
##        print('F ',F)
##        print('z',msd.states()[0])
        msd.propagateDynamics(F)
        t = t + P.Ts

   
    animation.drawMSD(msd.states())
    dataPlot.updatePlots(t, ref_input, msd.states(), F)
        
    plt.pause(0.0001)

##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()