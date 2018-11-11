import numpy as np
import random
import msdParam as P


class msdDynamics:


    def __init__(self):

        self.state = np.matrix([[P.z0],
                                [P.zdot0]])


        alpha = 0.2  # uncertainty paramter
        self.m = P.m * (1+2*alpha*np.random.rand()-alpha) # mass
        self.k = P.k * (1+2*alpha*np.random.rand()-alpha) # spring
        self.b = P.b * (1+2*alpha*np.random.rand()-alpha) # damper
        self.Ts = P.Ts  # sample time

        print('k',self.k)
        print('m',self.m)
        print('b',self.b)


    def propagateDynamics(self,u):

        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + self.Ts/2*k1, u)
        k3 = self.derivatives(self.state + self.Ts/2*k2, u)
        k4 = self.derivatives(self.state + self.Ts*k3, u)
        self.state += self.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)

        
    def derivatives(self,state,u):

        z = state.item(0)
        zdot = state.item(1)
        F = u
        # equation of motion
        zddot = (F - self.b*zdot - self.k*z) / self.m
        xdot = np.matrix([[zdot],[zddot]])
        return xdot


    def states(self):

        return self.state.T.tolist()[0]

    
