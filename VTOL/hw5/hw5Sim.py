import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import vtolParam as P
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData_vtol import plotData_vtol
from vtolDynamics import vtolDynamics
from vtolController import vtolController


ctrl = vtolController()
vtol = vtolDynamics()
refsig = signalGenerator(amplitude = 1.5, frequency=0.06)


# choice = int(input('animate(1) or plot(2)?'))
choice = 3
if choice == 1:
    animation = vtolAnimationTurtle()
elif choice == 2:
    dataPlot = plotData_vtol()
else:
    animation = vtolAnimation()
    dataPlot = plotData_vtol()


t = P.t_start
while t < P.t_end:
    
    
    zv_ref_input = refsig.square(t)+3
    h_ref_input = 2.5
    reference = [zv_ref_input,h_ref_input]

    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        
        Forces = ctrl.u(reference, vtol.states())
        vtol.propagateDynamics(Forces)
        t = t + P.Ts
        
    if choice == 1:
        zt = 0
        u = [vtol.states(),zt]
        animation.drawVtol(u,reference)  #zv,h,theta,zvd,hd,thetad,zt
    elif choice == 2:
        dataPlot.updatePlots(t,reference,vtol.states(),Forces)
    else:
        zt = 0
        u = [vtol.states(),zt]
        animation.drawVtol(u,reference)  #zv,h,theta,zvd,hd,thetad,zt
        dataPlot.updatePlots(t,reference,vtol.states(),Forces)
        
    plt.pause(0.0001)

##print('Press key to close')
##plt.waitforbuttonpress()
##plt.close()
##
