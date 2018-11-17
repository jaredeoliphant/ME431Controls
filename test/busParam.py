import numpy as np
import control.matlab as ctl


# Physical parameters of the double mass spring damper
m1 = 2500 #  kg
m2 = 320 # kg
k1 = 80000 # N/m
k2 = 500000 #  N/m
b1 = 350  #  N-s/m
b2 = 15020 #  N-s/m

# Initial conditions
z10 = 0.0   
z20 = 0.0  
z30 = 0.0
z40 = 0.0


# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 20.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate


#######State Feedback Control########
A = np.array([[0,1,0,0],
            [-(b1*b2)/(m1*m2),0,((b1/m1)*((b1/m1)+(b1/m2)+(b2/m2)))-(k1/m1),-(b1/m1)],
             [b2/m2,0,-((b1/m1)+(b1/m2)+(b2/m2)),1],
              [k2/m2,0,-((k1/m1)+(k1/m2)+(k2/m2)),0]])

B = np.array([[0],
              [1/m1],
               [0],
           [(1/m1)+(1/m2)]])


# this Cr matrix will allow us to track the 3rd state
Cr = np.array([[0,0,1,0]])

# confirm that the system in controllable
C_AB = ctl.ctrb(A,B)
if np.linalg.matrix_rank(C_AB) != 4:
    print('not controllable')


# two rise times (one set slightly higher than the other)
tr1 = 0.5  # rise time 1 
zeta = 0.707  # damping
print('tr1',tr1)
wn1 = np.pi/2.0/tr1/np.sqrt(1-zeta**2)

tr2 = 0.1  # rise time 2 
zeta = 0.707  # damping
print('tr2',tr2)
wn2 = np.pi/2.0/tr2/np.sqrt(1-zeta**2)

# find desired poles based on the rise times and damping ratios
poly = np.convolve([1,2*zeta*wn1,wn1**2],[1,2*zeta*wn2,wn2**2])
p = np.roots(poly)
print( 'desired poles',p)

# place the poles at the desired locations
K = ctl.place(A,B,p)
print ('K',K)

# find kr gain to ensure the DC gain is zero
kr = -1.0/(np.dot(Cr,np.dot(np.linalg.inv(A-B*K),B)))
print ('kr',kr)













