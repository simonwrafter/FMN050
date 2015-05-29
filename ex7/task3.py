# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:18:05 2015

@author: simon
"""
from  scipy import *
from  pylab import *

l = 1.0
g = 9.81
h = 0.001
t = [0]

a0 = [pi/4, 0]
w = [a0]
#w.append(a0)
t.append(t[-1] + h)
w.append(w[0] + h * afunk(w[0]))

def afunk (a):
    return array([a[1], -g/l*sin(a[0])])

def bdf2 ():
    while (t[-1]<5):
        t.append(t[-1]+h)
        u = fpi(4.0/3.0 * array(w[-1]) - 1.0/3.0 * array(w[-2]), array(w[-1]), h * 2.0/3.0, 0.00001)
        w.append([ u[0], u[1]])

def fpi(c, wn, h, tol):
    u = wn
    up1 = 0
    for i in range(2000):
        up1 = c + h * afunk(u)
        err = norm(u - up1)
        if err < tol:
            return up1
        u = up1
    else:
        return up1


bdf2()

figure(1)
clf()
grid(1)
plot(t, w)

figure(2)
clf()
grid(1)
plot([row[0] for row in w], [row[1] for row in w])
