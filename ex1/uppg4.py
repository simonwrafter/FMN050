# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:08:35 2015

@author: simon
"""

from  scipy import *
from  pylab import *

def f(x):
    return x**2 - 2

def new_sec(f, fp, xn, xnm1=0, xtol=1e-7):
    err_list = [nan]
    guess_list = [xn]
    for i in range(2000):
        deriv = fp(f,xn,xnm1)
        if deriv == 0:
            raise Exception("Derivative is zero at x={}".format(xn))
        xnp1 = xn - f(xn)/deriv
        guess_list.append(xnp1)
        err_list.append(abs(xn-xnp1))
        if err_list[i] < xtol:
            return xnp1, i, err_list, guess_list
        else:
            xnm1 = xn
            xn = xnp1
    else:
        return xnp1, i, err_list, guess_list


def newton(f,x0, tol):
    eps = np.finfo(float).eps * 10000
    return new_sec(f, (lambda fl, x0l, x1l : ((fl(x0l + eps) - f(x0l))/eps)), x0, xtol=tol)

def secant(f, x0, x1, tol):
    return new_sec(f, (lambda fl, x0l, x1l : ((fl(x1l) - fl(x0l)) / (x1l - x0l))), x0, x1, tol)
