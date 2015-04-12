# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 08:43:39 2015

@author: simon
"""

from  scipy import *
from  pylab import *

ab0 = [0.7, 0.7]

def F(a, b):
    return array([5*cos(a) + 6*cos(a+b) - 10, 5*sin(a) + 6*sin(a+b) - 4])

def Jack(F, xa, xb):
    eps = np.finfo(float).eps * 10000

    deriva = (F(xa + eps, xb) - F(xa, xb)) / eps #dF1 / dx1  &  dF2 / dx1
    derivb = (F(xa, xb + eps) - F(xa, xb)) / eps #dF1 / dx2  &  dF2 / dx2

    return array([[deriva[0], derivb[0]], [deriva[1], derivb[1]]])

print(Jack(F, *ab0))

def newton(F, x0, xtol = 1e-4):
    xn = x0
    for i in range(2000):
        J = Jack(F, *xn)
        print(J)
        print('\n')
        xnp1 = xn - inv(J) * F(*xn)
        if norm(xn-xnp1) < xtol:
            return xnp1, i, err_list, guess_list
        else:
            xn = xnp1
    else:
        return xnp1, i, err_list, guess_list

print(newton(F, ab0))