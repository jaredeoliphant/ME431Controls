import matplotlib.pyplot as plt
import busParam as P
from signalGenerator import signalGenerator
from plotData import plotData
from busDynamics import busDynamics
from busAnimation import busAnimation
import numpy as np

# intialize bus dynamics
bus = busDynamics()

# 5 meter amplitude step input, frequency 0.05 Hz
reference = signalGenerator(amplitude = 2.5, frequency = 0.15, y_offset=3.5)

# intialize data plot
dataPlot = plotData()

# intialize the animation
animation = busAnimation()

t = P.t_start
while t < P.t_end:

    # reference to track
    ref_input = reference.square(t)

    t_next_plot = t + P.t_plot
    while t < t_next_plot:

        # calculate control force based on the full state feedback gains
        F = P.kr*ref_input - np.dot(P.K,bus.states())

        # propagate the dynamics
        bus.propagateDynamics(F)
        t = t + P.Ts

    # update the plot
    dataPlot.updatePlots(t, ref_input, bus.states(), F)
    animation.drawBUS(bus.states())

        
    plt.pause(0.0001)