import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
import vtolParam as P
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData_vtol import plotData_vtol
from vtolDynamics import vtolDynamics



firstsignal = signalGenerator(amplitude=.25, frequency=.6)
slowersignal = signalGenerator(amplitude = .25, frequency=.1)
vtol = vtolDynamics()


choice = int(input('animate(1) or plot(2)?'))
if choice == 1:
    animation = vtolAnimation()
elif choice == 2:
    dataPlot = plotData_vtol()


t = P.t_start
while t < P.t_end:
    
    ref_input = [0,0,0] # zv_ref, h_ref, theta_ref

    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        zt = 0
        f_l = 7.36
        f_r = f_l +.00001
        F = [f_l,f_r]
        vtol.propagateDynamics(F)
        t = t + P.Ts
        
    if choice == 1:
        u = [vtol.states(),zt]
        animation.drawVtol(u)  #zv,h,theta,zvd,hd,thetad,zt
    elif choice == 2:
        dataPlot.updatePlots(t,ref_input,vtol.states(),F)
        
    plt.pause(0.0001)

print('Press key to close')
plt.show()
plt.waitforbuttonpress()
plt.close()
