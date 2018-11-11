import matplotlib.pyplot as plt
import numpy as np


class plotData:


    def __init__(self):

        self.fig, self.ax = plt.subplots(4,1,sharex=True) #time (x values) are shared across all subplots
        self.time_history = []

        self.zv_history = []
        self.h_history = []
        self.theta_history = []
        
        self.zv_ref_history = []
        self.h_ref_history = []
        self.theta_ref_history = []

        self.fl_history = []
        self.fr_history = []
        
        self.handle = []
        self.handle.append(myPlot(self.ax[0], ylabel='zv', title=''))
        self.handle.append(myPlot(self.ax[1],ylabel='h', title=''))
        self.handle.append(myPlot(self.ax[2],ylabel='theta', title=''))
        self.handle.append(myPlot(self.ax[3], xlabel='time (s)',ylabel='force', title=''))

    def updatePlots(self,t,reference,states,ctrl):

        print(t)
        print(reference)
        print(states)
        print(ctrl)

        zvref = reference[0]
        href = reference[1]
        thetaref = reference[2]

        zv = states[0]
        h = states[1]
        theta = states[2]
        
        f_l = ctrl[0]
        f_r = ctrl[1]
        
        self.time_history.append(t)
        self.zv_history.append(zv)
        self.h_history.append(h)
        self.theta_history.append(theta)
        
        self.zv_ref_history.append(zvref)
        self.h_ref_history.append(href)
        self.theta_ref_history.append(thetaref)

        self.fl_history.append(f_l)
        self.fr_history.append(f_r)

  
        self.handle[0].updatePlot(self.time_history, [self.zv_history, self.zv_ref_history])
        self.handle[1].updatePlot(self.time_history, [self.h_history, self.h_ref_history])
        self.handle[2].updatePlot(self.time_history, [self.theta_history, self.theta_ref_history])
        self.handle[3].updatePlot(self.time_history, [self.fl_history, self.fr_history])



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
                self.line.append(Line2D(time,data[i],
                                        color=self.colors[np.mod(i,len(self.colors)-1)],
                                        ls = self.line_styles[np.mod(i,len(self.line_styles)-1)],
                                        label = self.legend if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False


            if self.legend != None:
                plt.legend(handles=self.line)
        else:
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])

        self.ax.relim()
        self.ax.autoscale()
