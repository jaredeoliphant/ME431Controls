import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

plt.ion()  ## turns on interactive mode. not sure if it is needed


## this is a class that enables the data plot to update along with the animation

class plotData_msd:


    def __init__(self):

        self.fig, self.ax = plt.subplots(2,1,sharex=True) #time (x values) are shared across all subplots


        self.time_history = []   # time history
        self.z_ref_history = []   # reference position history
        self.z_history = []       # actual position history
        self.force_history = []   # force input

        self.handle = []
        self.handle.append(myPlot(self.ax[0],
                                  ylabel='z (m)',
                                  title='Mass Spring Damper Data'))
        self.handle.append(myPlot(self.ax[1],
                                  xlabel='time (s)',
                                  ylabel='force (N)'))

        ## after this initial code the self.handle is a array of 2 myPlot objects
        

    def updatePlots(self,t,reference,states,ctrl):
        self.time_history.append(t)
        self.z_ref_history.append(reference)
        self.z_history.append(states[0])
        self.force_history.append(ctrl)

        
        self.handle[0].updatePlot(self.time_history, [self.z_history, self.z_ref_history])
        self.handle[1].updatePlot(self.time_history, [self.force_history])
        plt.draw()
        plt.show()


class myPlot:

    def __init__(self,ax,xlabel='',ylabel='',title='',legend=None):

        
        self.legend = legend
        self.ax = ax
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
        self.line_styles = ['-','-','--','-.',':']

        self.line = []


        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_title(title)
        self.ax.grid(True)

        self.init = True

    def updatePlot(self,time,data):

        if self.init == True:
            for i in range(len(data)):
                self.line.append(Line2D(time,
                                        data[i],
                                        color=self.colors[np.mod(i, len(self.colors) - 1)],
                                        ls=self.line_styles[np.mod(i, len(self.line_styles) - 1)],
                                        label=self.legend if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False

            if self.legend != None:
                plt.legend(handles=self.line)

                
        else:
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])

        plt.draw()
        plt.show()
        self.ax.relim()
        self.ax.autoscale()
