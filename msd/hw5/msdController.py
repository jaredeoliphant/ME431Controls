import numpy as np
import sys
sys.path.append('..')
import msdParam as P
from PIDControl import PIDControl



class msdController:


    def __init__(self):

        self.zCtrl = PIDControl(P.kp, P.kd, P.ki, P.beta, P.Ts, P.F_max)
        self.limit = P.F_max



    def u(self, z_r, states):
        z = states[0]
##        z_e = z
        z_e = 0   ## the answer key showed always use 0 equilib. force
        F_e = P.k * z_e
        F_til = self.zCtrl.PID(z_r, z)  # don't send it the velocity anymore
        F = F_til+F_e
        F = self.saturate(F)  ## shouldn't be necessary in this case
        
        return F


    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
