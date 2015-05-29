# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:49:05 2015

@author: simon
"""
from  scipy import *
from  pylab import *
from  numpy import *

def L(x, xm, i):
    prod = 1
    for j in range(len(xm)):
        if i != j:
            prod *= (x - xm[j]) / (xm[i]- xm[j])
    return prod

def lagrange(x, xm, ym):
    prod = 0
    for i in range(len(xm)):
        prod += ym[i]*L(x, xm, i)
    return prod


def sigma(h, y):
    # constructing the A matrix
    m = len(y)-1
    A = diag((m)*[1], -1) + 4*eye(m+1) + diag((m)*[1], +1)  #Filling the whole matrix, then changeing the first and last row 
    A[0] = zeros(m+1)
    A[0][0] = 1
    A[-1] = zeros(m+1)
    A[-1][-1] = 1

    # constructing the b vector
    b = zeros(len(A))
    for i in range(1, m): # 1<= i < m
        b[i] = (y[i+1] - 2*y[i] + y[i-1])*(6./(h**2))
    
    return array(solve(A,b))

def cubspline(xint, yint):
    m = len(xint)-1      #number of splines
    h = abs(xint[1] - xint[0]) #distans between nodes
    di = yint[0:m]  #coeff di! #make di the correct length; length = m!
    s = sigma(h, yint) #solving for sigmas
    ci = [] # compute ci
    for i in range(m):    #i = 0 -> m-1
        ci.append(((yint[i+1]-yint[i])/h) - ((h*(2*s[i] + s[i+1])/6)))
    bi = s[0:m]/2.  # compute bi #make bi the correct length; length = m!
    ai = [] # compute ai
    for j in range(m):
        ai.append((s[j+1]-s[j])/(6.*h))
    coeff = zeros([m, 4]) # Put the Coeff matrix together    
    for i in range(m):
       coeff[i][0] = ai[i]
       coeff[i][1] = bi[i]
       coeff[i][2] = ci[i]
       coeff[i][3] = di[i]
    return coeff
    
def cubsplineval(coeff,xint,xval):
    knots = array([xint])
    bol = knots > xval
    k = argmax(bol) -1 #index for the index Xk < xval < Xkp1
    # get the coeffs
    ak = coeff[k][0]
    bk = coeff[k][1] 
    ck = coeff[k][2]
    dk = coeff[k][3]
    
    x = xval-xint[k]
    yval = ak*(x**3) + bk*(x**2) + ck*x + dk    
    return yval

def deriv(x,y):
    dx = []
    dy = []
    n = len(x)
    
    for i in range(n-1):
        dx.append((x[i] + x[i+1])/2)
        dy.append((y[i+1] - y[i])/(x[i+1] - x[i]))
    return dx, dy

def integrate(x, y):
    y = [i ** 2 for i in y]
    xi = []
    yi = []
    n  = len(x)
    for i in range(n-1):
        xi.append((x[i] + x[i+1])/2)
        yi.append((x[i+1] - x[i]) * (y[i] + y[i+1])/2)
    
    for i in range(n-2):
        yi[i+1] += yi[i]
        
    return xi,yi

x = [-1., -0.5, 0., 0.5, 1.]
y = [1., 2., 3., 2., 1.]
xlong = linspace(x[0], x[-1], 1000)


coeff = cubspline(x,y)
cubY = []
for i in range(len(xlong)):
    cubY.append(cubsplineval(coeff, x, xlong[i]))
cubY[-1] = y[-1]

lagY = [lagrange(i, x, y) for i in xlong]

figure(1)
clf()
grid(1)

plot(x, y, 'r*')
plot(xlong, cubY, 'b')
plot(xlong, lagY, 'g')

figure(2)
clf()
grid(1)

dxlong, dcubY = deriv(xlong, cubY)
plot(dxlong, dcubY, 'b')
dxlong, dlagY = deriv(xlong, lagY)
plot(dxlong, dlagY, 'g')

figure(3)
clf()
grid(1)

ddxlong, ddcubY = deriv(dxlong, dcubY)
plot(ddxlong, ddcubY, 'b')
ddxlong, ddlagY = deriv(dxlong, dlagY)
plot(ddxlong,ddlagY, 'g')

figure(4)
clf()
grid(1)

iddxlong, iddcubY = integrate(ddxlong, ddcubY)
plot(iddxlong, iddcubY, 'b')
iddxlong, iddlagY = integrate(ddxlong, ddlagY)
plot(iddxlong, iddlagY, 'g')

print(iddlagY[-1])
print(iddcubY[-1])