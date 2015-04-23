# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:10:53 2015

@author: simon
"""

from  scipy import *
from  pylab import *
from random import *

xmega = linspace(-1., 1., 1000)

def omega(x, xm):
    prod = 1
    for i in range(len(xm)):
        prod *= (x - xm[i])
    return prod


def randX(n):
    x = []
    for i in range(n):
        x.append(random()*2 - 1)
    x.sort()
    return x

figure(1)
clf()
grid(1)

x = randX(15)
plot(x, [0 for i in range(len(x))], '*')
plot(xmega, [omega(i, x) for i in xmega])


def cX(n):
    x = []
    for i in range(1, n+1):
        x.append(cos((2*i-1)/(2*n) * pi))
    return x

figure(2)
clf()
grid(1)

x = cX(10)
plot(x, [0 for i in range(len(x))], '*')
plot(xmega, [omega(i, x) for i in xmega])


def linX(n):
    return linspace(-1,1,n)

figure(3)
clf()
grid(1)

number = 8
x = linX(number)
plot(xmega, [omega(i, x) for i in xmega], 'b', label='%s data points' % number)
number = 12
x = linX(number)
plot(xmega, [omega(i, x) for i in xmega], 'r', label='%s data points' % number)
number = 18
x = linX(number)
plot(xmega, [omega(i, x) for i in xmega], 'g', label='%s data points' % number)
legend(loc='lower center')
#legend()