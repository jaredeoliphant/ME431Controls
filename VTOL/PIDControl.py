import numpy as np


class PIDControl:

    def __init__(self, kp, kd, ki, beta, Ts, limit, initial_cond):

        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.beta = beta
        self.Ts = Ts
        self.limit = limit

        self.ydot = 0.0
        self.y_prev = initial_cond
        self.errordot = 0.0
        self.error_prev = 0.0
        self.integrator = 0.0


    def PID(self, y_r, y, satFlag=True):

        error = y_r - y
        self.integrateError(error)
        self.differentiateError(error)
        self.differentiateY(y)
        u = self.kp*error + self.ki*self.integrator - self.kd*self.ydot
        
        if satFlag == True:
            u_sat = self.saturate(u)
            self.integratorAntiWindup(u_sat, u)
        else:
            u_sat = u

        
            
        return u_sat        


    def integrateError(self, err):
            self.integrator += self.Ts*(err + self.error_prev)/2.0


    def  differentiateError(self, err):
        
        self.errordot = self.beta*self.errordot +(1-self.beta)*(err - self.error_prev)/self.Ts
        
        self.error_prev = err


    def differentiateY(self, y):
        # print(self.beta,self.ydot,self.y_prev,y,self.Ts)
        self.ydot = self.beta*self.ydot + (1-self.beta)*(y - self.y_prev)/self.Ts
        # print('in PIDcontrol',self.ydot)
        self.y_prev = y

    
    def integratorAntiWindup(self, sat, unsat):
        if self.ki != 0.0:
            self.integrator = self.integrator + self.Ts/self.ki*(sat-unsat)
        # if sat != unsat:
            # print('anti wind up is doing something %.3f' %self.errordot)



    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
        