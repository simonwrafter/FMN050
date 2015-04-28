# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:31:58 2015

@author: Alex
"""
from scipy import *
from matplotlib.pyplot import *
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


def Bsplbasis(xi,di,dx):
    """
    This code evaluates a cubic spline given by its knots and de Boor points
    at equidistant points
    On input:
    =========
    xi.... list or array of length m+7 where 
           xi is composed out of the m+1 knots x and 6 additional 
           points at both boundaries. Preferably one takes the first and last
           knot and repeats it so that it gets multiplicity 4 each.
    di.... list or an array of m+3 de Boor points
    dx.... float which is used to define the evaluation points, which form an
           equidistant grid starting at xi[3]=x[0] and having an interval length dx
    On return:
    ==========
    q..... list with the values of the spline evaluated at
           xi[3]+i*dt, i=0,... as long as xi[3]+i*dt <= xi[-4]  

    """
    eps = 1.e-14
    m = len(xi) 
    i = 4      #index of first knot
    q=[]
    for u in arange(xi[3],xi[m-3]+dx,dx):
        
        # check if u value has moved to the next knot interval
        # include small tolerance on knots to avoid round-off error in comparisons.
        
        while (u>(xi[i]+eps)):
            i+=1
        # Now evaluate the spline at u using the deBoor algorithm.
        # Start with the relevant control points.
        # w used here to simplify indices.
        im4 = i-4
        qq = zeros(len(di))
        for j in range(1,5,1):
            qq[j-1]=di[im4+j-1]
        for j in range(1,4,1):
            for k in range(1,4-j+1,1):
                qq[k-1] = ((xi[im4 + k + 4-1] - u)/(xi[im4 + k + 4-1] - xi[im4 + k + j-1])) * qq[k-1] + \
                            ((u - xi[im4 + k + j-1])/(xi[im4 + k + 4-1] - xi[im4 + k + j-1])) * qq[k+1-1]
        #Create vector of points on the B-spline curve.
        q.append(qq[0])
    return q


x = [0, 1,  2, 3, 4, 5, 6]
y = [1, 3, -2, 0, 1, 0, 1]

xi = [0,   0,   0,    0, 1, 2, 3, 4, 5, 6,6,6,6]
yi = [1, 2.5, 5.3, -4.5, 0.8, 1.4, -0.55, 0.4, 1] # d
dx = 0.01

yb = Bsplbasis(xi,yi,dx)
xb = linspace(x[0], x[-1], len(yb))

figure(1)
clf()
grid(1)

plot(xplot, yval, 'b')
plot(xb,yb, 'r', x, y, '*')
