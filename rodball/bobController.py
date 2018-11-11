import numpy as np
import sys
sys.path.append('..')
import bobParam as P
from PIDControl import PIDControl



class bobController:


    def __init__(self):

        self.zCtrl = PIDControl(P.kp_z, P.kd_z, P.ki_z, P.beta, P.Ts, P.fMax, P.z0)
        self.thetaCtrl = PIDControl(P.kp_theta, P.kd_theta, 0.0, P.beta, P.Ts, P.fMax, P.theta0)
        self.limit = P.fMax


    def u(self, z_ref, states):
        
        z = states[0]
        theta = states[2]

        F_e = P.m1*P.g*z/P.l + P.m2*P.g/2.0

        #Successive loop controller
        theta_ref = self.zCtrl.PID(z_ref, z, False)
        F_til = self.thetaCtrl.PID(theta_ref, theta)
        
        F = F_til+F_e
    
        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
