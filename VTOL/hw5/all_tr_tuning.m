clc;
close all
clear

% longitudinal dynamics tuning (h)
tr_h = 1.825;
zeta = .707;
wn = pi/2/tr_h/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];
kd_h = denom(2)/.66666666;
kp_h = denom(3)/.66666666;
fprintf('kd_h = %f\n',kd_h)
fprintf('kp_h = %f\n',kp_h)
num = [.666666*kp_h];
sys = tf(num,denom);
step(sys)
hold on



% lateral dynamics (outer loop) zv
tr_zv = 1.825;
%vtol parameters
mc = 1;
mr = .25;
B = mc+2*mr;
mu = .1;
Fe = 9.81*(mc+2*mr);
zeta = .707;
wn = pi/2/tr_zv/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];

kd_zv = (denom(2)-(mu/B))/(-Fe/B);
kp_zv = denom(3)/(-Fe/B);
fprintf('kd_zv = %f\n',kd_zv)
fprintf('kp_zv = %f\n',kp_zv)
num = [-Fe/B*kp_zv];
sys = tf(num,denom);
step(sys)


% lateral dynamics (inner loop) (theta) has to be ~10X faster than the
% outer loop
tr_theta = tr_zv/10;
%vtol parameters
Jc = .0042;
mr = .25;
d = .3;
A = 1/(Jc+2*mr*d^2);
zeta = .707;
wn = pi/2/tr_theta/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];

kd_theta = denom(2)/A;
kp_theta = denom(3)/A;
fprintf('kd_theta = %f\n',kd_theta)
fprintf('kp_theta = %f\n',kp_theta)
num = [A*kp_theta];
sys = tf(num,denom);
step(sys)


legend('h','z_v','\theta')
