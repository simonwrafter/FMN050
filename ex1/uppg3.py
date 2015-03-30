# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:49:36 2015

@author: simon
"""

from  scipy import *
from  pylab import *

def g(x):
    return x * (x**2 + 6)/(3 * x**2 + 2)

def fpi(g, x, tol):
    err_list = []
    guess_list = []
    for i in range(2000):
        xnp1 = g(x)
        guess_list.append(xnp1)
        err_list.append(abs(x - xnp1))
        if err_list[i] < tol:
            return xnp1, i, err_list, guess_list
        x = xnp1
    else:
        return xnp1, i, err_list, guess_list

res, it, err, guess = fpi(g,-10, 0.001)
print(res, it)
plot(range(size(err)), err)
plot(range(size(guess)), guess)