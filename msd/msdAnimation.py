import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import msdParam as P
from scipy import signal

plt.ion()

class msdAnimation():

    def __init__(self):
        self.flagInit = True
        self.fig, self.ax = plt.subplots()
        self.handle = []
        self.width = P.width
        plt.axis([-6.0*P.width-.1, 6.0*P.width+.1, -.1, 12.0*P.width+.1])
        plt.plot([-6.0*P.width,-6.0*P.width, 6.0*P.width], [12.0*P.width,0,0], 'k',lw=1.5)

    def drawMSD(self,u):
        z = u[0]
        self.drawBox(z)
        self.drawSpring(z)
        self.drawDamper(z)

        if self.flagInit == True:
            self.flagInit = False

        plt.show()
        plt.draw()
        
    def drawBox(self,z):

        X = z-self.width/2
        Y = .007
        xy = (X,Y)
        if self.flagInit == True:
            self.handle.append(mpatches.Rectangle(xy,self.width,self.width,ec='black',fc='red'))
            self.ax.add_patch(self.handle[0])
        else:
            self.handle[0].set_xy(xy)


    def drawSpring(self,z):
        bumps = 3
        dist = z+0.8
        period = ((dist-self.width/2)-.01)/bumps
        freq= 1/period
        amplitude = .02
        t = np.arange(period/4,period*bumps-period/4,.001)
        x = []
        for i in t:
            x.append(.15+amplitude*signal.sawtooth(2*np.pi*freq*i, 0.5))

        if self.flagInit == True:
            line, = self.ax.plot(t-1.2,x,'k')
            self.handle.append(line)
            line, = self.ax.plot([-1.2,t[0]-1.2],[.15,.15],'k')
            self.handle.append(line)
            line, = self.ax.plot([t[len(t)-1]-1.2,z-self.width/2],[.15,.15],'k')
            self.handle.append(line)
        else:
            self.handle[1].set_xdata(t-1.2)
            self.handle[1].set_ydata(x)
            self.handle[2].set_xdata([-1.2,t[0]-1.2])
            self.handle[2].set_ydata([.15,.15])
            self.handle[3].set_xdata([t[len(t)-1]-1.2,z-self.width/2])
            self.handle[3].set_ydata([.15,.15])

    def drawDamper(self,z):
        
        if self.flagInit == True:
            line, = self.ax.plot([-1.2,z-self.width/2],[.1,.1],'k')
            self.handle.append(line)
            line, = self.ax.plot([-1.2,z-self.width/2],[.05,.05],'k')
            self.handle.append(line)
            line, = self.ax.plot([z-self.width/2,z-self.width/2-.05,z-self.width/2-.05,z-self.width/2-.05],
                                 [.075,.075,.075+.005,.075-.005],'k')
            self.handle.append(line)
        else:
            self.handle[4].set_xdata([-1.2,z-self.width/2])
            self.handle[4].set_ydata([.1,.1])
            self.handle[5].set_xdata([-1.2,z-self.width/2])
            self.handle[5].set_ydata([.05,.05])
            self.handle[6].set_xdata([z-self.width/2,z-self.width/2-.05,z-self.width/2-.05,z-self.width/2-.05])
            self.handle[6].set_ydata([.075,.075,.075+.009,.075-.009])


if __name__ == "__main__":

    simAnimation = msdAnimation()
    z = 0.0
    simAnimation.drawMSD([z])

    print('Press key to close')
    plt.waitforputtonpress()
    plt.close()
    
