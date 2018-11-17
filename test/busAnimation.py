import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import busParam as P
from scipy import signal

plt.ion()

class busAnimation():

    def __init__(self):
        self.flagInit = True
        self.fig, self.ax = plt.subplots()
        self.handle = []
        self.width = 5.0
        self.height = 3.0
        plt.axis([0,25,0,25])
        self.ax.set_xticklabels([""])
        self.ax.set_yticklabels([""])
        # plt.plot([-6.0*P.width,-6.0*P.width, 6.0*P.width], [12.0*P.width,0,0], 'k',lw=1.5)

    def drawBUS(self,states):
        x1 = states[0][0]
        x2 = states[2][0]+x1
        self.drawBox1(x1)
        self.drawBox2(x2)
        
        if self.flagInit == True:
            self.textbox1 = self.ax.text(1.5,12,"z1 = %.4f" %states[0][0])
            self.textbox2 = self.ax.text(1.5,11,"z2 = %.4f" %states[1][0])
            self.textbox3 = self.ax.text(1.5,10,"z3 = %.4f" %states[2][0])
            self.textbox4 = self.ax.text(1.5,9,"z4 = %.4f" %states[3][0])
            self.flagInit = False
        else:
            self.textbox1.set_text("z1 = %.4f" %states[0][0])
            self.textbox2.set_text("z2 = %.4f" %states[1][0])
            self.textbox3.set_text("z3 = %.4f" %states[2][0])
            self.textbox4.set_text("z4 = %.4f" %states[3][0])

        plt.show()
        plt.draw()
        
    def drawBox1(self,x1):
        X = 10
        Y = x1+3
        xy = (X,Y)
        if self.flagInit == True:
            self.handle.append(mpatches.Rectangle(xy,self.width,self.height,ec='black',fc='red'))
            self.ax.add_patch(self.handle[0])
        else:
            self.handle[0].set_xy(xy)


    def drawBox2(self,x2):

        X = 10
        Y = x2+3+self.height
        xy = (X,Y)
        if self.flagInit == True:
            self.handle.append(mpatches.Rectangle(xy,self.width,self.height,ec='black',fc='blue'))
            self.ax.add_patch(self.handle[1])
        else:
            self.handle[1].set_xy(xy)

