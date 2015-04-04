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
x1 = 0.0

res1, it1, err1, guess1 = bisec(f, x0, x1, tol)
res2, it2, err2, guess2 = fpi(g, x1, tol)
res3, it3, err3, guess3 = newton(f, x1, tol)
res4, it4, err4, guess4 = secant(f, x0, x1, tol)

plot(range(size(guess1)), guess1)
plot(range(size(guess2)), guess2)
plot(range(size(guess3)), guess3)
plot(range(size(guess4)), guess4)

figure()

plot(range(size(err1)), err1)
plot(range(size(err2)), err2)
plot(range(size(err3)), err3)
plot(range(size(err4)), err4)

print("bisec:  {}".format(it1))
print("fpi:    {}".format(it2))
print("newton: {}".format(it3))
print("secant: {}".format(it4))