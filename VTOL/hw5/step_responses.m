clc;
close all
clear
tr = 8


zeta = .707;
wn = pi/2/tr/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];
kp = denom(3)/.66666666
kd = denom(2)/.66666666
num = [.666666*kp];
sys = tf(num,denom);
step(sys)
hold on
