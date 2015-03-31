# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:42:18 2015

@author: simon
"""

from  scipy import *
from  pylab import *
from  scipy.optimize import fsolve
from uppg1 import bisec

def f(x):
    return x**2 - 2

tol = 1e-14

res = bisec(f, 0, 4, tol)

print(res[0])
print(fsolve(f, 4, xtol=tol))