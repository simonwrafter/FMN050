# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:33:05 2015

@author: simon
"""
from  scipy import *
from  pylab import *


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

from scipy import polyval, sqrt

def s1002(S):
     #Polynom coefficients:
     #-------------------- 
     #Section A:    
     AA =  1.364323640
     BA =  0.066666667

     #Section B:     
     AB =  0.000000000;
     BB =  3.358537058e-02;
     CB =  1.565681624e-03;
     DB =  2.810427944e-05;
     EB =  5.844240864e-08;
     FB =  1.562379023e-08;
     GB =  5.309217349e-15;
     HB =  5.957839843e-12;
     IB =  2.646656573e-13;
     #Section C:     
     AC =  4.320221063e+03;
     BC =  1.038384026e+03;
     CC =  1.065501873e+02;
     DC =  6.051367875;
     EC =  2.054332446e-01;
     FC =  4.169739389e-03;
     GC =  4.687195829e-05;
     HC =  2.252755540e-07;
     #Section D:     
     AD = 16.446;
     BD = 13.;
     CD = 26.210665;
     #Section E: 
     AE = 93.576667419;
     BE =  2.747477419;
     #Section F:     
     AF =  8.834924130;
     BF = 20.;
     CF = 58.558326413;
     #Section G:   
     AG = 16.;
     BG = 12.;
     CG = 55.;
     #Section H:   
     AH =  9.519259302;
     BH = 20.5;
     CH = 49.5;
     circarc = lambda S, A,B,C: A + sqrt(B**2 - ( S + C )**2)

     YS=[-70.0,-62.764705882,-49.662510381,
             -39.764473993, -38.426669071, -35.0,
             -26.0,32.15796,60.0];

     if (S < YS[1]):                        #  Section H (Circular arc) 
        wheel = circarc(S,AH,BH,CH)
     elif (S  < YS[2]):                     #  Section G (Circular arc) 
        wheel = circarc(S,AG,BG,CG)
     elif (S < YS[3]):                      #  Section F (Circular arc) 
        wheel = circarc(S,AF,BF,CF)
     elif (S < YS[4]):                      #        Section E (LINEAR)
        wheel   = -BE*S-AE;
     elif (S < YS[5]):                      #  Section D (Circular arc) 
        wheel = -circarc(S,-AD,BD,CD)   
     elif (S < YS[6]):                      #                 Section C 
        wheel = - polyval([HC,GC,FC,EC,DC,CC,BC,AC],S)  
     elif (S < YS[7]):                      #                 Section B
        wheel = polyval([IB,-HB,GB,-FB,EB,-DB,CB,-BB,AB],S)
     else:                                  #        Section A (LINEAR)            
        wheel   =   -BA*S + AA;
     return -wheel

#real
x = linspace(-69, 60, 3000);
y = []
for i in x:
    y.append(s1002(i))

#spline
p = 5

xs = linspace(-69, 60, p)
ys = []
for i in xs:
    ys.append(s1002(i))

coeff = cubspline(xs,ys)
ysplot = []
xsplot = array(linspace(-69, 60, 3000))
for i in range(len(xsplot)):
    ysplot.append(cubsplineval(coeff, xs, xsplot[i]))
    
#plot
figure(1)
clf()
grid(1)
axis([-69,60, -30, 5])

plot(x,y, 'b', xsplot, ysplot, 'r', xs, ys, 'r*')