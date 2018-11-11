# Planar VTOL Parameter File (Problem F)
import numpy as np
import control.matlab as ctl

# Physical parameters of the ball and beam
mc = 1.0 # kg    mass of center
Jc = 0.0042 # kg m^2   inertia of center
mr = 0.25 # kg       mass of right rotor
ml = 0.25 # kg       mass of left rotor
d = 0.3  #m        distance to rotors
mu = 0.1  # kg/s    drag
g = 9.8 # m/s^2   gravity

# parameters for animation
boxheight = 0.1
boxwidth = 0.15
targetsize = 0.1
length = d   # rod length

# Initial conditions
zv0 = 1.5  # initial position of the box
h0 = 2.5
theta0 = 0.0
zvdot0 = 0.0
hdot0 = 0.0
thetadot0 = 0.0

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 40.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain


## altitude for poles at -.2,-.3
##kp = 0.09
##kd = 0.75


## altitude for tr = 8 seconds
##kp_h = 0.115624509130103
##kd_h = 0.588870762606469
##
##
#### inner loop (theta); tr = 0.8 seconds
##kp_theta = 0.379248386154254
##kd_theta = 0.193149608203426
##
##
#### outer loop (zv); tr = 8 seconds
##kp_zv = -0.00785759483342561
##kd_zv = -0.0332226134364772





####################################
#tr_h = 1.825  tr_theta = .1825  tr_zv = 1.825
fMax = 10  #N

"""
tr_h = 1.25
zeta = .707
wn = np.pi/2/tr_h/np.sqrt(1-zeta**2)
kd_h = 2*zeta*wn/.66666666
print('kd_h',kd_h)
# kd_h = 2.581351
kp_h = wn**2/.66666666
print('kp_h',kp_h)
# kp_h = 2.221796


tr_zv = 2
B = mc+2*mr
Fe = 9.81*(mc+2*mr)
wn = np.pi/2/tr_zv/np.sqrt(1-zeta**2)
kd_zv = (2*zeta*wn-(mu/B))/(-Fe/B)
print('kd_zv',kd_zv)
# kd_zv = -0.168627
kp_zv = wn**2/(-Fe/B);
print('kp_zv',kp_zv)
# kp_zv = -0.150988



tr_theta = tr_zv/10.0
A = 1/(Jc+2*mr*d**2);
wn = np.pi/2/tr_theta/np.sqrt(1-zeta**2)
kd_theta = 2*zeta*wn/A
print('kd_theta',kd_theta)
# kd_theta = 0.846683
kp_theta = wn**2/A
print('kp_theta',kp_theta)
# kp_theta = 7.287490




### integral gains
ki_h = 0.55
ki_zv = -0.04

"""




#####################STATE FEEDBACK####################
mtot = mc + ml + mr
Alon = np.matrix([[0,1],
                [0,0]])

Blon = np.matrix([[0],
            [1/mtot]])

Clon = np.matrix([[1,0]])

Dlon = np.matrix([[0]])


C_ABlon = ctl.ctrb(Alon,Blon)


## altitude rise time
tr_h = 1.25
zeta = .707
wn = np.pi/2/tr_h/np.sqrt(1-zeta**2)
p = np.roots([1,2*zeta*wn,wn**2])

Klon = ctl.place(Alon,Blon,p)

krlon = -1/(Clon*np.linalg.inv(Alon-Blon*Klon)*Blon)



F = mtot*g
Alat = np.matrix([[0,0,1,0],
        [0,0,0,1],
        [0,-F/mtot,-mu/mtot,0],
        [0,0,0,0]])

Blat = np.matrix([[0],
    	[0],
        [0],
        [1/(Jc+2*mr*d**2)]])

Clat = np.matrix([[1,0,0,0],
        [0,1,0,0]])

Dlat = np.matrix([[0],
        [0]])


C_ABlat = ctl.ctrb(Alat,Blat)



# lateral rise time
tr_zv = 2.0
wn_zv = np.pi/2/tr_zv/np.sqrt(1-zeta**2)


# angle rise time (should be much faster than lateral rise time)
tr_theta = tr_zv/10.0
wn_theta = np.pi/2/tr_theta/np.sqrt(1-zeta**2)

polynomial = np.convolve(np.array([1,2*wn_zv*zeta,wn_zv**2]), np.array([1,2*wn_theta*zeta,wn_theta**2]))

p = np.roots(polynomial)

Klat = ctl.place(Alat,Blat,p)

Czv = np.matrix([[1,0,0,0]])
krlat = -1/(Czv*np.linalg.inv(Alat-Blat*Klat)*Blat)



print ('Klat',Klat,'Klon',Klon,'krlat',krlat,'krlon',krlon)
