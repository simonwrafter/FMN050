# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:08:35 2015

@author: simon
"""

from  scipy import *
from  pylab import *

def f(x):
    return x**2 - 2

def new_sec(f, fp, xn, xnm1, tol):
    err_list = []
    guess_list = []
    for i in range(2000):
        xnp1 = xn - f(xn)/fp(f,xn,xnm1)
        print(xnp1)
        guess_list.append(xnp1)
        err_list.append(abs(xn-xnp1))
        if err_list[i] < tol:
            return xnp1, i, err_list, guess_list
        else:
            xnm1 = xn
            xn = xnp1
    else:
        return xnp1, i, err_list, guess_list


def newton(f,x0, tol):
    return new_sec(f, (lambda fl, x0l, x1l : ((fl(x0l + 1e-7) - f(x0l))/1e-7)), x0, 0, tol)

def secant(f, x0, x1, tol):
    return new_sec(f, (lambda fl, x0l, x1l : ((fl(x1l) - fl(x0l)) / (x1l - x0l))), x0, x1, tol)


res, it, err, guess = newton(f,10, 1e-14)
print(res, it)
plot(range(size(err)), err)
plot(range(size(guess)), guess)