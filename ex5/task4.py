# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:14:17 2015

@author: simon
"""
from  scipy import *
from  pylab import *
from garden_1 import *
from  scipy.interpolate import *

# raw data
t, xpp, ypp = read_acc_data() #import data

t = t[250: -1]
xpp = xpp[250: -1]
ypp = ypp[250: -1]

# B spline of data
t_max = linspace(t[0], t[-1], (len(t) * 10)) # larger time vector

xspl = splrep(t, xpp) # B-spline for x vector
yspl = splrep(t, ypp) # B-spline for y vector

xsev = splev(t_max, xspl) # evaluate spline to plot x
ysev = splev(t_max, yspl) # evaluate spline to plot y

figure(1)
clf()
grid(1)
plot(t, xpp, 'g*', label='x sample points') # plot data points
plot(t, ypp, 'b*', label='y sample points') # plot data points
plot(t_max, xsev, label='x spline') # plot x spline
plot(t_max, ysev, label='y spline') # plot y spline
legend(loc='lower right', fancybox=True, shadow=True)
axis([t[0], t[-1], min(min(xpp), min(ypp)) * 1.1, max(max(xpp), max(ypp)) * 1.1])
xlabel('time / [s]')
ylabel('acceleration / [m/s²]')
# polynome spline of data and twice integrated

xpol = PPoly.from_spline(xspl) # create piecewise  polynomial for x spline
xpol = xpol.antiderivative() #integrate once
xpol = xpol.antiderivative() # integrate twice
x = [xpol(i) for i in t_max] # evaluate for all time points

figure(2)
clf()
grid(1)
plot(t_max, x, 'g', label='distance moved in x')
axis([t[0], t[-1], min(x), max(x)])
legend(loc='lower right', fancybox=True, shadow=True)
xlabel('time / [s]')
ylabel('position / [m]')

ypol = PPoly.from_spline(yspl) # create piecewise  polynomial for y spline
ypol = ypol.antiderivative()
ypol = ypol.antiderivative()
y = [ypol(i) for i in t_max]

figure(3)
clf()
grid(1)
plot(t_max, y, 'b', label='distance moved in y')
axis([t[0], t[-1], min(x), max(y)])
legend(loc='lower right', fancybox=True, shadow=True)
xlabel('time / [s]')
ylabel('position / [m]')

print("x - start: ", x[0], ", end: ", x[-1], ", diff: ", x[-1] - x[0])
print("x - min: ", min(x), ", max: ", max(x), ", diff: ", max(x)-min(x))

print("y - start: ", y[0], ", end: ", y[-1], ", diff: ", abs(y[-1] - y[0]))
print("y - min: ", min(y), ", max: ", max(y), ", diff: ", max(y)-min(y))