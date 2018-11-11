import numpy as np
import bobParam as P

class bobDynamics:


    def __init__(self):

        self.state = np.matrix([[P.z0],
                                [P.zdot0],
                                [P.theta0],
                                [P.thetadot0]])

        alpha = 0.2
        self.m1 = P.m1 * (1+2*alpha*np.random.rand()-alpha)
        self.m2 = P.m2 * (1+2*alpha*np.random.rand()-alpha)
        self.l = P.l * (1+2*alpha*np.random.rand()-alpha)
        self.g = P.g 
        self.Ts = P.Ts

        print('m1',self.m1)
        print('m2',self.m2)
        print('l',self.l)

    def propagateDynamics(self,u):

        # print('in dynamics zdot',self.state.item(1))
        # print('in dynamics thetadot',self.state.item(3))
        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + self.Ts/2*k1, u)
        k3 = self.derivatives(self.state + self.Ts/2*k2, u)
        k4 = self.derivatives(self.state + self.Ts*k3, u)
        self.state += self.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)


    def derivatives(self,state,u):

        z = state.item(0)
        zdot = state.item(1)
        theta = state.item(2)
        thetad = state.item(3)
        F = u
        
        # equations of motion

        A = np.matrix([[self.m1, 0],
                       [0, (self.m2*self.l**2/3.0 + self.m1*z**2)]])
        b = np.matrix([[self.m1*z*thetad**2-self.m1*self.g*np.sin(theta)],
                       [F*self.l*np.cos(theta)-2*self.m1*z*zdot*thetad-self.m1*self.g*z*np.cos(theta)-self.m2*self.g*self.l*np.cos(theta)/2.0]])
        A = A.reshape(2,2)
        b = b.reshape(2,1)
        answer = np.linalg.solve(A,b)
        xdot = np.matrix([[zdot],
                          [answer.item(0)],
                          [thetad],
                          [answer.item(1)]])
        return xdot


    def states(self):

        return self.state.T.tolist()[0]
