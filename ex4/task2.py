# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:59:34 2015

@author: simon
"""
from  scipy import *
from  pylab import *
from  task1 import *

y = [1, 3, -2, 0, 1, 0, 1]
x = [0, 1, 2, 3, 4, 5, 6]

coeff = cubspline(x,y)
yval = []
xplot = array(linspace(0, x[-1], 200))
for i in range(len(xplot)):
    yval.append(cubsplineval(coeff, x, xplot[i]))

figure(1)
clf()
grid(1)

plot(xplot, yval)