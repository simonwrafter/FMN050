# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 08:43:39 2015

@author: simon
"""

from  scipy import *
from  scipy.optimize import fsolve
from  pylab import *

ab0 = array([0.7, 0.7])

def F(ab):
    a=ab[0]
    b=ab[1]
    return array([(5*cos(a) + 6*cos(a+b)) - 10.,
                  (5*sin(a) + 6*sin(a+b)) - 4.])

def Jack(F, xab):
    xa = xab[0]
    xb = xab[1]
    eps = np.finfo(float).eps * 10000

    deriva = (F([xa + eps, xb]) - F([xa, xb])) / eps #dF1 / dx1  &  dF2 / dx1
    derivb = (F([xa, xb + eps]) - F([xa, xb])) / eps #dF1 / dx2  &  dF2 / dx2

    return array([[deriva[0], derivb[0]], [deriva[1], derivb[1]]])

def ourqr(A):
    v1 = A[:,0]
    v2 = A[:,1] - (dot(A[:,1], v1)/(norm(v1)**2))*v1

    q1 = v1/norm(v1)
    q2 = v2/norm(v2)
    Q = array([[q1[0], q2[0]],[q1[1], q2[1]]])
    R = dot(transpose(Q), A)
    return Q, R

def noninvert(J, Fx):
    Q, R = qr(J)

    Qtb = dot(transpose(Q), Fx)
    x2 = Qtb[1] / R[1,1]
    x1 = (Qtb[0] - R[0,1]*x2) / R[0,0]

    return array([x1,x2])


def newton(F, x0, xtol = 1e-4):
    xn = x0
    for i in range(2000):
        J = Jack(F, xn)
        xnp1 = xn - noninvert(J, F(xn))
        if abs(norm(xn-xnp1)) < xtol:
            return xnp1
        else:
            xn = xnp1
    else:
        return xnp1

print(newton(F, ab0, 1e-14) - fsolve(F, ab0))

