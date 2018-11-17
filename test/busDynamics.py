import numpy as np
import busParam as P


class busDynamics:

    def __init__(self):

        # inital conditions
        self.state = np.array([[P.z10],
                                [P.z20],
                                [P.z30],
                                [P.z40]])

        # parameters of the system
        self.m1 = P.m1
        self.k1 = P.k1
        self.b1 = P.b1
        self.m2 = P.m2
        self.k2 = P.k2
        self.b2 = P.b2
        self.Ts = P.Ts  # sample time


    def propagateDynamics(self,u):

        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + self.Ts/2*k1, u)
        k3 = self.derivatives(self.state + self.Ts/2*k2, u)
        k4 = self.derivatives(self.state + self.Ts*k3, u)
        self.state += self.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)

        
    def derivatives(self,x,u):

        # state equation
        m1 = self.m1
        m2 = self.m2
        b1 = self.b1
        b2 = self.b2
        k1 = self.k1
        k2 = self.k2
        A = np.array([[0,1,0,0],
                     [-(b1*b2)/(m1*m2),0,((b1/m1)*((b1/m1)+(b1/m2)+(b2/m2)))-(k1/m1),-(b1/m1)],
                     [b2/m2,0,-((b1/m1)+(b1/m2)+(b2/m2)),1],
                     [k2/m2,0,-((k1/m1)+(k1/m2)+(k2/m2)),0]])
        B = np.array([[0],
                    [1/m1],
                    [0],
                  [(1/m1)+(1/m2)]])
        
        # calculate xdot
        xdot = np.dot(A,x) + B*u
        return xdot


    def states(self):
        # function for returning the state vector
        return self.state

    
