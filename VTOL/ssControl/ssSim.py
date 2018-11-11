import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import vtolParam as P
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData_vtol import plotData_vtol
from vtolDynamics import vtolDynamics
from vtolControllerSS import vtolControllerSS


ctrl = vtolControllerSS()
vtol = vtolDynamics()
refsig = signalGenerator(amplitude = 1.5, frequency=0.06)



animation = vtolAnimation()
dataPlot = plotData_vtol()


t = P.t_start
while t < P.t_end:
    
    
    zv_ref_input = refsig.square(t)+3
    h_ref_input = .5*refsig.square(2.0*t)+1.5
    reference = [zv_ref_input,h_ref_input]

    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        
        Forces = ctrl.u(reference, vtol.states())
        vtol.propagateDynamics(Forces)
        t = t + P.Ts
        

    zt = 0
    u = [vtol.states(),zt]
    animation.drawVtol(u,reference)  #zv,h,theta,zvd,hd,thetad,zt
    dataPlot.updatePlots(t,reference,vtol.states(),Forces)
        
    plt.pause(0.0001)

##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()
##