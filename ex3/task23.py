# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:10:53 2015

@author: simon
"""

from  scipy import *
from  pylab import *
from random import *

"""
x = []
for i in range(15):
    x.append(random()*2 - 1)
x.sort()
"""

def cX(n):
    x = []
    for i in range(1, n+1):
        x.append(cos((2*i-1)/(2*n) * pi))
    return x

def omega(x, xm):
    prod = 1
    for i in range(len(xm)):
        prod *= (x - xm[i])
    return prod


figure(1)
clf()
grid(1)

x = cX(50)
xmega = linspace(-1., 1., 1000)

plot(x, [0 for i in range(len(x))], '*')
plot(xmega, [omega(i, x) for i in xmega])