# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:42:18 2015

@author: simon
"""

from  scipy import *
from  pylab import *
from  scipy.optimize import fsolve

def f(x):
    return x**2 - 2

print(fsolve(f, -4))
print(fsolve(f, 4))