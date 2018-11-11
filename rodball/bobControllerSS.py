import numpy as np
import sys
sys.path.append('..')
import bobParam as P

class bobControllerSS:


    def __init__(self):

        self.limit = P.fMax
        self.beta = P.beta
        self.Ts = P.Ts
        self.zdot = 0.0
        self.z_prev = P.z0
        self.thetadot = 0.0
        self.theta_prev = P.theta0
        self.K = P.K   # K and kr are developed assuming a equilibrium point of l/2
        self.kr = P.kr


    def u(self, z_ref, states):
        
        z = states[0]
        theta = states[2]

        F_e = P.m1*P.g*z/P.l + P.m2*P.g/2.0

        # set up the state vector x
        self.differentiateZ(z)
        self.differentiateTheta(theta)
        x = np.matrix([[z],[theta],[self.zdot],[self.thetadot]])   
        xe = np.matrix([[P.l/2],[0],[0],[0]]) # equillibrum states  

        # state feedback control
        F_til = self.kr*(z_ref-P.l/2) - self.K*(x-xe)

        F = F_til+F_e
    
        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u

    def differentiateZ(self, z):
        self.zdot = self.beta*self.zdot + \
                    (1-self.beta)*(z - self.z_prev)/self.Ts
        self.z_prev = z

    def differentiateTheta(self, theta):
        self.thetadot = self.beta*self.thetadot + \
                    (1-self.beta)*(theta - self.theta_prev)/self.Ts
        self.theta_prev = theta