# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:51:45 2015
@author: Freddie
"""
from  scipy import *
from  pylab import *

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def f(a):
    return -a**5 + 2.0*a**2-15.0*a+32.0
    

#integrate from 1 to 5 = 16
simpson = []
#simpsonerror = []
gauss = []
npoints = range(1,40, 1)
for n in npoints:
    disp(1.0*n/max(npoints))

    a=-2.0
    b= 2.0
#    n = 1000000
    h = (b-a)/n
    #simpson
    sum = f(a) + 4*f(a+h/2) + f(b)
    for i in drange(a,b,h):
        sum += 2*f(i) + 4*(f(i+h/2)) 
        
    sum *= h/6
    error = 0
    for i in drange(a,b,h):
        temp = f(i)**4
        if temp > error:
            error = temp
    error = (b-a)*h**4*error/2880
    #disp('simpson')
    #disp(sum)
    simpson.append(sum)
    #disp(error)
#    simpsonerror.append(error)
    
    
    #3 point gauss
    sum = 0
    for i in drange(a,b,h):
        sum += 5*f(i + (5-sqrt(15))*h/10) + 8*f(i+5*h/10) + 5*f(i+((5+sqrt(15))*h/10))
    
    sum *=h/18
    
    #disp('gauss')
    #disp(sum)
    gauss.append(sum)
plt.plot(npoints,gauss, 'b')
plt.hold(True)
plt.plot(npoints,simpson, 'g')
#plt.plot(npoints,simpsonerror, 'k')
plt.plot(npoints, (len(npoints))*[138.67], 'r')

