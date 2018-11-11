import numpy as np
import sys
sys.path.append('..')
import vtolParam as P
from PIDControl import PIDControl



class vtolController:


    def __init__(self):
        # kp, kd, ki, beta, Ts, limit, initial_cond)
        self.hCtrl = PIDControl(P.kp_h, P.kd_h, P.ki_h, P.beta, P.Ts, P.fMax, P.h0)
        self.thetaCtrl = PIDControl(P.kp_theta, P.kd_theta, 0.0, P.beta, P.Ts, P.fMax, P.theta0)
        self.zvCtrl = PIDControl(P.kp_zv, P.kd_zv, P.ki_zv, P.beta, P.Ts, P.fMax, P.zv0)
        self.limit = P.fMax


    def u(self, reference, states):
        
        zv = states[0]
        h = states[1]
        theta = states[2]
        
        zv_ref = reference[0]
        h_ref = reference[1]
        
        F_e = (P.mc+2*P.mr)*P.g

        #Longitudinal controller
        F_til = self.hCtrl.PID(h_ref, h)

        #Successive loop lateral controller
        theta_ref = self.zvCtrl.PID(zv_ref, zv, False)
        Tau = self.thetaCtrl.PID(theta_ref, theta)
        
        F = F_til+F_e
        
        f_r = 0.5*F + Tau/(2.0*P.d)
        f_l = 0.5*F - Tau/(2.0*P.d)
        
        f_r = self.saturate(f_r)
        f_l = self.saturate(f_l)
        return [f_l,f_r]


    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
