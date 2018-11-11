clc;
close all
clear
tr = 2.125+.074


zeta = .7;
wn = pi/2/tr/sqrt(1-zeta^2);
denom = [1 2*zeta*wn wn^2];
kp = (denom(3)-.6)/.2
kd = (denom(2)-.1)/.2
num = [.2*kp];
sys = tf(num,denom);
step(sys)
hold on
