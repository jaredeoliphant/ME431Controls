import numpy as np


class PDControl:

    def __init__(self, kp, kd):

        self.kp = kp
        self.kd = kd



    def PD(self, z_r, z, zdot):

        error = z_r - z
##        print('z_r ',z_r,' z ',z,' error ',error,' zdot ',zdot)
        u = self.kp*error - self.kd*zdot

        return u        
