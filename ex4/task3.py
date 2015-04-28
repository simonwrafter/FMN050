# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:30:49 2015

@author: simon
"""
from  scipy import *
from  pylab import *
from splbasis_1 import *

y = [1, 3, -2, 0, 1, 0, 1]
x = [0,0,0,0, 1, 2, 3, 4, 5, 6,6,6,6]
d = [1,1,1,1,1,1,1,1,1]
dx = 0.1

Bsplbasis(x,d,dx)