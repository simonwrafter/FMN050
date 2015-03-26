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
    for i in range(2000):
        xnp1 = g(x)
        if abs(x - xnp1) < tol:
            return xnp1, i
        x = xnp1

print(fpi(g,-10, 0.001))