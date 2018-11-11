clc
clear
close
% MASS SPRING DAMPER SYSTEM
k = 3;
m = 5;
b = 0.5;

A = [0,1;
    -k/m,-b/m];

B = [0;
	1/m];

C = [1,0];

D = [0];


C_AB = ctrb(A,B)
CC = [B,A*B]
Rank = rank(C_AB)



aA = [b/m,k/m]
AA = [1,b/m;0,1]


tr = 2
zeta = 0.7;
wn = pi/2.0/tr/sqrt(1-zeta^2);

p = roots([1,2*zeta*wn,wn^2])
alpha = [2*zeta*wn,wn^2]
K = place(A,B,p)
Ktest = -(aA-alpha)*inv(AA)*inv(CC)
check = eig(A-B*K)
kr = -1/(C*inv(A-B*K)*B)

sys = ss(A,B,C,D)
systf = tf(sys)