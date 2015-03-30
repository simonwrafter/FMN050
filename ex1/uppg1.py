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

    err_list = []
    guess_list = []

    for i in range(2000):
        err_list.append(abs(a-b))
        if err_list[i] < tol:
            h = (a+b)/2
            guess_list.append(h)
            return h, i, err_list, guess_list
        else:
            h = (a+b)/2
            guess_list.append(h)
            if f(a)*f(h) <= 0:
                b = h
            elif f(h)*f(b) <= 0:
                a = h
            else:
                raise Exception("possibly multiple roots in interval")
    else:
        return xnp1, i, err_list, guess_list
