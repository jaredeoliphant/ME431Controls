clc
clear
close
% BALL ON BEAM SYSTEM
m1 = 0.35;
g = 9.8;
m2 = 2;
l = 0.5; 
ze = 0.5;


A = [0,0,1,0;
    0,0,0,1;
    0,-g,0,0;
    -m1*g/(m2*l^2/3+m1*ze^2),0,0,0];

B = [0; 0; 0; l/(m2*l^2/3+m1*ze^2)];

C = [1,0,0,0;
    0,1,0,0];

D = [0;0];


C_AB = ctrb(A,B)
CC = [B,A*B,A*A*B,A*A*A*B]
Rank = rank(C_AB)



aA = [0,0,0,-m1*g^2/(m2*l^2/3+m1*ze^2)]
AA = eye(4)


tr_z = 2
tr_th = 2
zeta = 0.7;
wn_z = pi/2.0/tr_z/sqrt(1-zeta^2);
wn_th = pi/2.0/tr_th/sqrt(1-zeta^2);

p = roots([1,2*zeta*wn,wn^2])
     
K = place(A,B,p)
alpha = [2*zeta*wn,wn^2,2*zeta*wn,wn^2]
Ktest = (aA-alpha)*AA^-1*CC^-1
check = eig(A-B*K)
kr = -1/(C*inv(A-B*K)*B)

sys = ss(A,B,C,D)
systf = tf(sys)

syms 