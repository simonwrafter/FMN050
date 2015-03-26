# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:31:58 2015

@author: simon
"""

from  scipy import *
from  pylab import *

def f(x):
    return x**2 - 2

def plotter(fun, a, b):
    x = linspace(a,b, 1000)
    y = fun(x)
    plot(x,y)

def bisec(f,a,b,tol):

    if f(a)*f(b) > 0:
        raise Exception("no root in interval")

    for i in range(2000):
        if abs(a-b) < tol:
            return a, i
        else:
            h= (a+b)/2
            if f(a)*f(h) <= 0:
                b=h
            elif f(h)*f(b) <= 0:
                a=h
            else:
                raise Exception("no root in interval")



print(bisec(f,-4,0,0.001))