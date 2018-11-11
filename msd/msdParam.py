# Mass-Spring-Damper Parameter File (Problem D)
import numpy as np
import control.matlab as ctl
# Physical parameters of the mass spring damper
m = 5.0 # kg
k = 3.0 # N/m
b = 0.5 # N-sec/m

# parameters for animation
width = .2   # square box

# Initial conditions
z0 = 0.0   # initial position of the box
zdot0 = 0.0  # initial velocity of the box

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 40.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

### dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

## PD gains
# for poles at -1, -1.5
##kp = 4.5
##kd = 12

# for poles at -7.6985 +- .78539i
##kp = 3.04755171635377
##kd = 7.19844184366336

# saturation limits
F_max = 2.0
'''
# kp = 2.35700082832722   # 2.125 rise time perfect non-saturation
# kd = 6.74559232344787   # as long as  we calculate Fe based on z_e = 0
kp = 3.872
kd = 5.7216
#kp = 2
#kd = 6.5
##ki = 0       #steady state error
##ki = .5   #100% rise time > 20;
ki = 1.5   #100% rise time 4; overshoot .52
##ki = 1.75   #100% rise time 4; overshoot .52
##ki = 2.5  #100% rise time 3; overshoot .61
##ki = 3  #100% rise time 2.75; overshoot .63
##ki = 4  #100% rise time 2.5; overshoot .67
print ('kp',kp)
print( 'ki',ki)
print('kd',kd)
'''



#######State Feedback Control########
A = np.matrix([[0,1],[-k/m,-b/m]])
B = np.matrix([[0],[1/m]])
C = np.matrix([[1,0]])
D = np.matrix([[0]])

C_AB = ctl.ctrb(A,B)

if np.linalg.matrix_rank(C_AB) != 2:
    print('not controllable')

tr = 2.125  # rise time
zeta = 0.707  # damping
print('tr',tr)


wn = np.pi/2.0/tr/np.sqrt(1-zeta**2)
# wn = 2.2/tr

# place the poles at the desired locations
p = np.roots([1,2*zeta*wn,wn**2])
print( 'desired poles',p)
K = ctl.place(A,B,p)
H2ax = ctl.ss(A-B*K, B, C, D)
eigs = np.linalg.eig(H2ax.A)
print( 'new poles', eigs[0])
print ('K',K)

kr = -1.0/(C*np.linalg.inv(A-B*K)*B)
print ('kr',kr)













