import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import vtolParam as P
import matplotlib.transforms as mtran

class vtolAnimation():

    def __init__(self):
        self.flagInit = True
        self.fig, self.ax = plt.subplots()
        self.handle = []
        self.boxheight = P.boxheight
        self.boxwidth = P.boxwidth
        self.length = P.length
        self.targetsize = P.targetsize
        plt.axis([0,6,-1,6])
        plt.plot([0,0,6], [6,0,0], 'k')
        


    def drawVtol(self,u,reference):
        state = u[0]
        zv = state[0]
        h = state[1]
        theta = state[2]
        zt = u[1]
        
        self.drawBox(zv,h,theta)
        self.drawRotorLines(zv,h,theta)
        self.drawTarget(zt,reference)
        self.drawLine(h)
        self.drawRotors(zv,h,theta)
        self.ax.axis('equal')
        if self.flagInit == True:
            self.flagInit = False

        
    def drawBox(self,zv,h,theta):
        pts = np.matrix([[-self.boxwidth/2.0, -self.boxheight/2.0],
                         [-self.boxwidth/2.0, self.boxheight/2.0],
                         [self.boxwidth/2.0, self.boxheight/2.0],
                         [self.boxwidth/2.0, -self.boxheight/2.0]]).T # non rotated points
        R = np.matrix([[np.cos(theta), -np.sin(theta)],
                             [np.sin(theta), np.cos(theta)]])
        pts = R*pts
        xy = np.array([zv,h]) + np.array(pts.T)
        if self.flagInit == True:
            self.handle.append(mpatches.Polygon(xy,ec='black'))
            self.ax.add_patch(self.handle[0])
        else:
            self.handle[0].set_xy(xy) 

    def drawRotorLines(self,zv,h,theta):

        X1 = [zv,zv+self.length*np.cos(theta)]
        Y1 = [h,h+self.length*np.sin(theta)]
        X2 = [zv,zv-self.length*np.cos(theta)]
        Y2 = [h,h-self.length*np.sin(theta)]

        if self.flagInit == True:
            line, = self.ax.plot(X1,Y1,'k--',lw=1.5)
            self.handle.append(line)
            line, = self.ax.plot(X2,Y2,'k--',lw=1.5)
            self.handle.append(line)
        else:
            self.handle[1].set_xdata(X1)
            self.handle[1].set_ydata(Y1)
            self.handle[2].set_xdata(X2)
            self.handle[2].set_ydata(Y2)

    def drawTarget(self,zt,reference):

        xy = (zt-self.targetsize/2.0,0)
        zvh = (reference[0]-self.targetsize/2.0,reference[1]-self.targetsize/2.0)
        if self.flagInit == True:
            self.handle.append(mpatches.Rectangle(xy,self.targetsize,self.targetsize,fc='red',ec='black'))
            self.ax.add_patch(self.handle[3])
            self.handle.append(mpatches.Rectangle(zvh,self.targetsize,self.targetsize,fc='red',ec='black'))
            self.ax.add_patch(self.handle[4])
        else:
            self.handle[3].set_xy(xy)
            self.handle[4].set_xy(zvh)


    def drawLine(self,h):

        if self.flagInit == True:
            line, = self.ax.plot([-0.5,6.5],[h,h], 'k:',lw=1)
            self.handle.append(line)
        else:
            self.handle[5].set_ydata([h,h])

    def drawRotors(self,zv,h,theta):
        pts = np.matrix([[0.1000, 0],
                        [0.0968,    0.0109],
                        [0.0874,    0.0212],
                        [0.0724,    0.0301],
                        [0.0527,    0.0370],
                        [0.0297,    0.0416],
                        [0.0048,    0.0435],
                       [-0.0205,    0.0427],
                       [-0.0444,    0.0391],
                       [-0.0655,    0.0329],
                       [-0.0824,    0.0247],
                       [-0.0940,    0.0149],
                       [-0.0995,    0.0041],
                       [-0.0987,   -0.0069],
                       [-0.0916,   -0.0175],
                       [-0.0786,   -0.0269],
                       [-0.0606,   -0.0347],
                       [-0.0386,   -0.0402],
                       [-0.0142,   -0.0431],
                       [0.0111,  -0.0433],
                       [0.0357,  -0.0407],
                       [0.0580,  -0.0355],
                       [0.0766,  -0.0280],
                       [0.0903,  -0.0187],
                       [0.0982,  -0.0082]]).T
        R = np.matrix([[np.cos(theta), -np.sin(theta)],
                             [np.sin(theta), np.cos(theta)]])
        pts = R*pts
        xyR = np.array([zv+self.length*np.cos(theta),h+self.length*np.sin(theta)]) + np.array(pts.T)
        xyL = np.array([zv-self.length*np.cos(theta),h-self.length*np.sin(theta)]) + np.array(pts.T)
        if self.flagInit == True:
            self.handle.append(mpatches.Polygon(xyR,ec='black'))
            self.ax.add_patch(self.handle[6])
            self.handle.append(mpatches.Polygon(xyL,ec='black'))
            self.ax.add_patch(self.handle[7])
        else:
            self.handle[6].set_xy(xyR)
            self.handle[7].set_xy(xyL)
