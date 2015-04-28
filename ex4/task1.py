# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from  scipy import *
from  pylab import *
from  numpy import *

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
    
    #coeff di!
    di = yint[0:m] #make di the correct length; length = m!
    
    #solving for sigmas
    s = sigma(h, yint)
    
    # compute ci
    ci = []
    for i in range(m):    #i = 0 -> m-1
        ci.append(((yint[i+1]-yint[i])/h) - ((h*(2*s[i] + s[i+1])/6)))
    
    # compute bi
    bi = s[0:m]/2. #make bi the correct length; length = m!
    
    # compute ai
    ai = []       
    for j in range(m):
        ai.append((s[j+1]-s[j])/(6.*h))
   
    # Put the Coeff matrix together    
    coeff = zeros([m, 4])
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
    
y = [1, 3, -2, 0, 1, 0, 1]
x = [0, 1, 2, 3, 4, 5, 6]

coeff = cubspline(x,y)
yval = []
xplot = array(linspace(0, x[-1], 200))
for i in range(len(xplot)):
    yval.append(cubsplineval(coeff, x, xplot[i]))
yval[-1] = y[-1]
figure(1)
clf()
grid(1)

plot(x, y, 'r*', xplot, yval, 'b')