import numpy as np
import vtolParam as P



class vtolDynamics:


    def __init__(self):

        self.state = np.matrix([[P.zv0],
                                [P.h0],
                                [P.theta0],
                                [P.zvdot0],
                                [P.hdot0],
                                [P.thetadot0]])

        alpha = 0.2
        self.mc = P.mc * (1+2*alpha*np.random.rand()-alpha)
        self.Jc = P.Jc * (1+2*alpha*np.random.rand()-alpha)
        self.mr = P.mr
        self.ml = P.ml
        self.mtot = self.mc+self.mr+self.ml
        self.d = P.d * (1+2*alpha*np.random.rand()-alpha)
        self.mu = P.mu * (1+2*alpha*np.random.rand()-alpha)
        self.g = P.g
        self.Ts = P.Ts

        print('mc',self.mc)
        print('Jc',self.Jc)
        print('d',self.d)
        print('mu',self.mu)

    def propagateDynamics(self,u):


        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + self.Ts/2*k1, u)
        k3 = self.derivatives(self.state + self.Ts/2*k2, u)
        k4 = self.derivatives(self.state + self.Ts*k3, u)
        self.state += self.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)


    def derivatives(self,state,u):

        zv = state.item(0)
        h = state.item(1)
        theta = state.item(2)
        zvdot = state.item(3)
        hdot = state.item(4)
        thetadot = state.item(5)
        
        f_l = u[0]
        f_r = u[1]

        
        # equations of motion
        zvddot = (-(f_l+f_r)*np.sin(theta) - self.mu*zvdot) / self.mtot
        hddot  = ((f_l+f_r)*np.cos(theta) - self.mtot*self.g ) / self.mtot
        thetaddot = self.d*(f_r-f_l) / (self.Jc+2*self.ml*self.d**2)
        
        xdot = np.matrix([[zvdot],
                          [hdot],
                          [thetadot],
                          [zvddot],
                         [hddot],
                         [thetaddot]])
        return xdot


    def states(self):

        return self.state.T.tolist()[0]
