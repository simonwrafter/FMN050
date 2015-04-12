# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:12:15 2015

@author: simon
"""
from  scipy import *
from  pylab import *

from uppg1 import bisec
from uppg3 import fpi
from uppg4 import newton
from uppg4 import secant


def f(x):
    return x**2 - 2

def g(x):
    return x * (x**2 + 6)/(3 * x**2 + 2)

tol = 1e-14
x0 = 5
x1 = 0

res1, it1, err1, guess1 = bisec(f, x0, x1, tol)
res2, it2, err2, guess2 = fpi(g, x0, tol)
res3, it3, err3, guess3 = newton(f, x0, tol)
res4, it4, err4, guess4 = secant(f, x0, x1, tol)

figure(1)
clf()
grid(1)

p11 = plot(range(size(guess1)), guess1, label='bisec')
p12 = plot(range(size(guess2)), guess2, label='fpi')
p13 = plot(range(size(guess3)), guess3, label='newton')
p14 = plot(range(size(guess4)), guess4, label='secant')

xlabel('iterations')
ylabel('guess')
legend(shadow=True)
axis([0,10,0,5])

figure(2)
clf()
grid(1)

plot(range(size(err1)), err1, label='bisec')
plot(range(size(err2)), err2, label='fpi')
plot(range(size(err3)), err3, label='newton')
plot(range(size(err4)), err4, label='secant')

xlabel('iterations')
ylabel('error')
legend(shadow=True)
#axis([0,8,0,5])

print("bisec:  {}".format(it1))
print("fpi:    {}".format(it2))
print("newton: {}".format(it3))
print("secant: {}".format(it4))
