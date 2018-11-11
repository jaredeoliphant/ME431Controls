clc
close all
clear

z = .2
bumps = 2
period = (z-.01)/bumps
freq= 1/period

amplitude = .1
t = -.8+period/4:.001:-.8+period*bumps-period/4 % end with .35
x = amplitude*sawtooth(freq*2*pi*t,.5);
% plott = linspace(0.5,period*bumps-period/4,length(t));
plot(t,x)
xlim([-.8 .8])
axis equal
pause(0.1)
