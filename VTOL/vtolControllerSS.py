import numpy as np
import sys
sys.path.append('..')
import vtolParam as P


class vtolControllerSS:


    def __init__(self):
        # kp, kd, ki, beta, Ts, limit, initial_cond
        self.limit = P.fMax
        self.beta = P.beta
        self.Ts = P.Ts

        self.zvdot = 0.0
        self.zv_prev = P.zv0
        self.thetadot = 0.0
        self.theta_prev = P.theta0
        self.hdot = 0.0
        self.h_prev = P.h0

        self.Klat = P.Klat   
        self.krlat = P.krlat
        self.Klon = P.Klon   
        self.krlon = P.krlon



    def u(self, reference, states):
        
        zv = states[0]
        h = states[1]
        theta = states[2]
        
        zv_ref = reference[0]
        h_ref = reference[1]
        
        F_e = (P.mc+2*P.mr)*P.g

        self.differentiateZv(zv)
        self.differentiateTheta(theta)
        self.differentiateH(h)


        x = np.matrix([[h],[self.hdot]])   
        
        # state feedback control lon
        F_til = self.krlon*(h_ref) - self.Klon*x


        x = np.matrix([[zv],[theta],[self.zvdot],[self.thetadot]])   

        # state feedback control lat
        Tau = self.krlat*(zv_ref) - self.Klat*x


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


    def differentiateZv(self, zv):
        self.zvdot = self.beta*self.zvdot + \
                    (1-self.beta)*(zv - self.zv_prev)/self.Ts
        self.zv_prev = zv

    def differentiateTheta(self, theta):
        self.thetadot = self.beta*self.thetadot + \
                    (1-self.beta)*(theta - self.theta_prev)/self.Ts
        self.theta_prev = theta
    
    def differentiateH(self, h):
        self.hdot = self.beta*self.hdot + \
                    (1-self.beta)*(h - self.h_prev)/self.Ts
        self.h_prev = h