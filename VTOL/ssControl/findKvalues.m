clc
clear
close
% BALL ON BEAM SYSTEM
mtot = 1.5;
theta = 0;
g = 9.81;
F = mtot*g;
mu = 0.1;
Jc = 0.0042;
mr = 0.25;
d = 0.3;

Alon = [0,1;
        0,0];

Blon = [0;
    1/mtot];

Clon = [1,0];

Dlon = [0];


C_ABlon = ctrb(Alon,Blon)
% CC = [B,A*B,A*A*B,A*A*A*B]
Rank = rank(C_ABlon)



% aA = [0,0,0,-m1*g^2/(m2*l^2/3+m1*ze^2)]
% AA = eye(4)

% 
% tr_z = 2
% tr_th = 2
% zeta = 0.7;
% wn_z = pi/2.0/tr_z/sqrt(1-zeta^2);
% wn_th = pi/2.0/tr_th/sqrt(1-zeta^2);
% 
% p = roots([1,2*zeta*wn,wn^2])
%      
% K = place(A,B,p)
% alpha = [2*zeta*wn,wn^2,2*zeta*wn,wn^2]
% Ktest = (aA-alpha)*AA^-1*CC^-1
% check = eig(A-B*K)
% kr = -1/(C*inv(A-B*K)*B)
% 
% sys = ss(A,B,C,D)
% systf = tf(sys)
% 

Alat = [0,0,1,0;
        0,0,0,1;
        0,-F/mtot,-mu/mtot,0;
        0,0,0,0];

Blat = [0;
    	0;
        0;
        1/(Jc+2*mr*d^2)];

Clat = [1,0,0,0;
        0,1,0,0];

Dlat = [0;
        0];


C_ABlat = ctrb(Alat,Blat)
% CC = [B,A*B,A*A*B,A*A*A*B]
Rank = rank(C_ABlat)


