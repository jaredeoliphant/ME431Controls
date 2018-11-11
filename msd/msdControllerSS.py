import numpy as np
import sys
sys.path.append('..')
import msdParam as P

class msdControllerSS:

    def __init__(self):

        self.limit = P.F_max
        self.beta = P.beta
        self.Ts = P.Ts
        self.zdot = 0.0
        self.z_prev = 0.0
        self.K = P.K
        self.kr = P.kr
        

    def u(self, z_r, states):
        z = states[0]
##        z_e = z
        z_e = 0   ## the answer key showed always use 0 equilib. force
        F_e = P.k * z_e
        # set up state vector
        self.differentiateZ(z)
        x = np.matrix([[z],[self.zdot]])

        # state feedback control using K gains
        F_til = self.kr*z_r - self.K*x 
        F = F_til+F_e
        F = self.saturate(F)  ## shouldn't be necessary in this case
        
        return F


    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u

    def differentiateZ(self, z):
        self.zdot = self.beta*self.zdot + \
                    (1-self.beta)*(z - self.z_prev)/self.Ts
        self.z_prev = z
