# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:36:03 2015

@author: simon
"""
from  scipy import *
from  pylab import *

def exp_euler(f, w_0, t_0, t_stop, h):
    w = list([w_0])
    t = list([t_0])
    while t[-1] < t_stop:
        w.append(w[-1] + h*f(t, w[-1]))
        t.append(t[-1] + h)
    return t, w

def imp_euler(f, u_0, t_0, t_stop, h):
    u = list([u_0])
    t = list([t_0])
    while t[-1] < t_stop:
        t.append(t[-1] + h)
        u.append( u[-1] / (1.0 - h * 10.0))
    return t,u

def f(t, y):
    return 10.0 * y

#print("explicit euler, h = 1/10: ")
#print(exp_euler(f, 1.0, 0.0, 2.0, 0.1))
#print("\nimplicit euler, h = 1/10: ")
#print(imp_euler(f, 1.0, 0.0, 2.0, 0.1))
#print("\nexplicit euler, h = 1/2: ")
#print(exp_euler(f, 1.0, 0.0, 2.0, 0.5))
#print("\nimplicit euler, h = 0.000001: ")
#print(imp_euler(f, 1.0, 0.0, 2.0, 0.000001))

#to, wo = imp_euler(f, 1.0, 0.0, 2.0, 0.10001)

#plot(to,wo)