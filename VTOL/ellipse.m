close all
clc
clear
x1 = -.1;
x2 = .1;
y1 = 0;
y2 = 0;
e = .9;
a = 1/2*sqrt((x2-x1)^2+(y2-y1)^2);
 b = a*sqrt(1-e^2);
 t = linspace(0,2*pi);
 X = a*cos(t);
 Y = b*sin(t);
 w = atan2(y2-y1,x2-x1);
 x = (x1+x2)/2 + X*cos(w) - Y*sin(w);
 y = (y1+y2)/2 + X*sin(w) + Y*cos(w);
 x = x(1:4:end);
 y = y(1:4:end);
 plot(x,y,'k-')
 axis equal
 
 [x' y']
 