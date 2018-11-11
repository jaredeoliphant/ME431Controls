import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import bobParam as P


class bobAnimation():

    def __init__(self):
        self.flagInit = True
        self.fig, self.ax = plt.subplots()
        self.handle = []
        self.diameter = P.diameter
        self.length = P.length
        plt.axis([0, .7, -.7, .7])
##        self.ax.axis('equal')
        plt.plot([-0.2, P.length+.1], [0,0], 'k--')


    def drawbob(self,u):
        z = u[0]
        theta = u[2]
        self.drawRod(theta)
        self.drawBall(z,theta)
        plt.axis([-.7, .7, -.7, .7])
        self.ax.axis('equal')
        if self.flagInit == True:
            self.flagInit = False

        
    def drawRod(self,theta):

        X = [0.0, np.cos(theta)*self.length]
        Y = [0.0, np.sin(theta)*self.length]
        if self.flagInit == True:
            line, = self.ax.plot(X,Y, lw=6, c='blue')
            self.handle.append(line)
        else:
            self.handle[0].set_xdata(X)
            self.handle[0].set_ydata(Y)


    def drawBall(self,z,theta):

        X = np.cos(theta)*z - np.sin(theta)*(self.diameter/2)
        Y = np.sin(theta)*z + np.cos(theta)*(self.diameter/2+.005)
        xy = (X,Y)
        if self.flagInit == True:
            self.handle.append(mpatches.CirclePolygon(xy,radius = P.diameter/2,ec='black',fc='red'))
            self.ax.add_patch(self.handle[1])
        else:
            self.handle[1]._xy=xy


