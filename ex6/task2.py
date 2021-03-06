# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:36:03 2015

@author: simon
"""
from  scipy import *
from  pylab import *

def exp_euler(f, w_0, t_0, t_stop, h):
    w = w_0
    x  = list([w_0[0]])
    xp = list([w_0[1]])
    y  = list([w_0[2]])
    yp = list([w_0[3]])
    t = list([t_0])
    while t[-1] < t_stop:
        w = w + h*f(t[-1], w)
        x.append(w[0])
        xp.append(w[1])
        y.append(w[2])
        yp.append(w[3])
        t.append(t[-1] + h)
    return t, x, xp, y, yp

def imp_euler(f, u_0, t_0, t_stop, h):
    u = u_0
    x  = list([u_0[0]])
    xp = list([u_0[1]])
    y  = list([u_0[2]])
    yp = list([u_0[3]])
    t = list([t_0])
    while t[-1] < t_stop:
        t.append(t[-1] + h)
        u = fpi(f, t, u, h, 1e-6)
        x.append(u[0])
        xp.append(u[1])
        y.append(u[2])
        yp.append(u[3])
    return t, x, xp, y, yp
    
def fpi(f, t, u, h, tol):
    up1 = u
    u_old = u
    for i in range(2000):
        up1 = u_old + h * f(t, u)
        err = norm(u - up1)
        if err < tol:
            return up1
        u = up1
    else:
        return up1

def f(t, y):
    r = sqrt(y[0]**2 + y[2]**2)**3
    A = array([[   0.0, 1.0,    0.0, 0.0], 
               [-3.0/r, 0.0,    0.0, 0.0],
               [   0.0, 0.0,    0.0, 1.0],
               [   0.0, 0.0, -3.0/r, 0.0]])
    return dot(A, y)


to, xo, xpo, yo, ypo = exp_euler(f, array([0.0,1.,2.0,0.0]), 0, 100, 0.01)
figure(1)
clf()
grid(1)
#axis([-0.1, 0.1, 1.9, 2.1])
title('Explicit Euler, h=0.0001')
plot(xo, yo, label='satelite')
plot(0,0,'o',label='planet')
legend()

to, xo, xpo, yo, ypo = imp_euler(f, array([0.0,1.,2.0,0.0]), 0, 100, 0.01)
figure(2)
clf()
grid(1)
#axis([-0.1, 0.1, 1.9, 2.1])
title('Implicit Euler, h=0.0001')
plot(xo, yo, label='satelite')
plot(0,0,'o',label='planet')
legend()
