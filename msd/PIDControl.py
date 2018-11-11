import numpy as np


class PIDControl:

    def __init__(self, kp, kd, ki, beta, Ts, limit):

        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.beta = beta
        self.Ts = Ts
        self.limit = limit

        self.zdot = 0.0
        self.z_prev = 0.0
        self.errordot = 0.0
        self.error_prev = 0.0
        self.integrator = 0.0


    def PID(self, z_r, z):

        error = z_r - z
        self.integrateError(error)
        self.differentiateError(error)
        self.differentiateZ(z)
        u = self.kp*error + self.ki*self.integrator - self.kd*self.zdot

        u_sat = self.saturate(u)
        self.integratorAntiWindup(u_sat, u)
        return u_sat        


    def integrateError(self, err):
        self.integrator += self.Ts*(err + self.error_prev)/2.0


    def  differentiateError(self, err):
        self.errordot = self.beta*self.errordot + \
                        (1-self.beta)*(err - self.error_prev)/self.Ts
        self.error_prev = err


    def differentiateZ(self, z):
        self.zdot = self.beta*self.zdot + \
                    (1-self.beta)*(z - self.z_prev)/self.Ts
        self.z_prev = z


    def integratorAntiWindup(self, sat, unsat):
        if self.ki != 0.0:
            self.integrator = self.integrator + self.Ts/self.ki*(sat-unsat);

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
        
