# Ball on Beam Parameter File (Problem D)
import numpy as np
import control.matlab as ctl

# Physical parameters of the ball and beam
m1 = 0.35 # kg    mass of ball
m2 = 2.0 # kg       mass of rod
l = 0.5 # m      length of rod
g = 9.8 # m/s^2   gravity

# parameters for animation
diameter = .1
length = l   # rod length

# Initial conditions
z0 = 0.25   # initial position of the ball
zdot0 = 0.0
theta0 = 0*np.pi/180  # initial angle of the rod (rad)
thetadot0 = 0.0

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 30.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain


## original values
# kd_theta = 1.184285
# kp_theta = 1.860270
# kd_z = -0.032047
# kp_z = -0.005034


# tuned with saturation tr = 1.1 and .11
fMax = 15
'''
tr_theta = .11
ze = l/2.0
A = l/((m2*l**2/3.)+m1*ze**2)
zeta = .707
wn = np.pi/2./tr_theta/np.sqrt(1-zeta**2)
kd_theta = 2*zeta*wn/A
print('kd_theta',kd_theta)
# kd_theta = 10.766223
kp_theta = wn**2/A
print('kp_theta',kp_theta)
# kp_theta = 153.741311




tr_z = 12*tr_theta
wn = np.pi/2./tr_z/np.sqrt(1-zeta**2)
kd_z = 2*zeta*wn/-g
print('kd_z',kd_z)
# kd_z = -0.291340
kp_z = wn**2/-g
print('kp_z',kp_z)
# kp_z = -0.416032



ki_z = -0.1


'''





#######State Feedback Control########
ze = l/2.0
A = np.matrix([[0,0,1,0],
            [0,0,0,1],
            [0,-g,0,0],
            [-m1*g/(m2*l**2/3+m1*ze**2),0,0,0]])

B = np.matrix([[0],
                [0],
                [0],
                [l/(m2*l**2/3+m1*ze**2)]])

C = np.matrix([[1,0,0,0],
                [0,1,0,0]])

D = np.matrix([[0],
                [0]])

C_AB = ctl.ctrb(A,B)

if np.linalg.matrix_rank(C_AB) != 4:
    print('not controllable')


zeta = 0.707  # damping

tr_theta = .11
wn_th = np.pi/2./tr_theta/np.sqrt(1-zeta**2)

tr_z = 10*tr_theta
wn_z = np.pi/2./tr_z/np.sqrt(1-zeta**2)

desired_polynomial = np.convolve(np.array([1,2*zeta*wn_z,wn_z**2]),np.array([1,2*zeta*wn_th,wn_th**2]))
p = np.roots(desired_polynomial)

print( 'desired poles',p)
K = ctl.place(A,B,p)
H2ax = ctl.ss(A-B*K, B, C, D)
eigs = np.linalg.eig(H2ax.A)
print ('new poles', eigs[0])
print ('K',K)


Cz = np.matrix([[1.0,0,0,0]])    # pick off the z value of the state because that is one we are tracking
kr = -1.0/(Cz*np.linalg.inv(A-B*K)*B)
print ('kr',kr)





