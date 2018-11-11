clc;
close all
clear
tr = 0.8
%vtol parameters
Jc = .0042;
mr = .25;
d = .3;
A = 1/(Jc+2*mr*d^2);
zeta = .707;
wn = pi/2/tr/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];

kd = denom(2)/A
kp = denom(3)/A
num = [A*kp];
sys = tf(num,denom);
step(sys)
hold on

k_DC = 1;



tr = 8
%vtol parameters
mc = 1;
mr = .25;
B = mc+2*mr;
mu = .1;
Fe = 9.81*(mc+2*mr);
zeta = .707;
wn = pi/2/tr/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];

kd = (denom(2)-(mu/B))/(-Fe/B)
kp = denom(3)/(-Fe/B)
num = [-Fe/B*kp];
sys = tf(num,denom);
step(sys)
hold on

legend('tr 0.8','tr 8.0')
