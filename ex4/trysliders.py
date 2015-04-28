# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:44:03 2015

@author: Alex
"""
from __future__ import division
from scipy import *
from matplotlib.pyplot import *
import numpy
from numpy import linalg as LA
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

def f(x):
    return 1./(1.+25.*x**2)

def Chebpts(n):
    cnodes = zeros(n)
    for i in range(0,n):
        cnodes[i] = cos((2*i+1)*pi/(2*n))
    return cnodes

#the lagrange bais functions
def Lagbasis(x,n,xval):
    lnxval=1.
    for i in range(len(x)):
        if (i!=n):
            lnxval*=(xval-x[i])/(x[n]-x[i])
    
    return lnxval

#The Lagrange interpolation method
def LagInter(x,y,xval):
    yval=0.
    #xx=linspace(x[0],x[-1],100)
    #yy=zeros(len(xx))
    for basis in range(len(x)):
        #yy+=y[basis]*Lagbasis(x,basis,xx)
        yval+=y[basis]*Lagbasis(x,basis,xval)
    return yval

def LagChebfun(n):
    xl = linspace(-1,1,n) # equidistant pts in [-1,1]
    xc = Chebpts(n)       # Chebyshev pts in [-1,1]
    yl = f(xl)            # y data for x equidistant
    yc = f(xc)            # y data for x Chebyshev
    
    xx =linspace(xl[0],xl[-1],100)
    yyl=LagInter(xl,yl,xx)
    yyc=LagInter(xc,yc,xx)
    return xx,xl,yyl,xc,yyc

x = [  0.0,   1.0,   2.0,   3.0,  4.0]
y = [27.93, 46.98, 31.95, 31.68, 21.0]
#y = [27.93, 47.98, 31.95, 31.68, 21.0]
#y = [-0.80000, -0.50000, -0.20000, 0.00000,0.20000, 0.50000, 0.80000]

method = '6' #input("try sliders = 6:")

    
if method=='6':
    #Task 4
    n=6
    xx,xl,yyl,xc,yyc=LagChebfun(n)
    #ax = subplot(111)
    fig1=figure()
    subplots_adjust(left=0.10, bottom=0.15)
    grid()
    #x = linspace(-1,1,n)
    #t = arange(-1.0, 1.0, 0.01)
    #z = zeros(len(xx))
    plot(xx,f(xx),'k',label='function')
    l, = plot(xx,yyl, lw=2, color='green',label='Lagrange')
    w, = plot(xl,f(xl),'go',markersize=10,label='Lagrange nodes')
    m, = plot(xx,yyc,color='red',label='Chebyshev')
    z, = plot(xc,f(xc), 'ro',markersize=10,label='Chebyshev nodes')
    legend(loc='upper right')
    #axis('tight')    
    axis([-1, 1, -.15, 1.1])
    
    axcolor = 'lightgoldenrodyellow'
    loc = .10

    ax =  axes([.10, loc, 0.80, 0.05], axisbg=axcolor)
    #loc +=.02
    sl = (Slider(ax, 'nodes',1, 19, valinit=n))

    def update(val):
        xx,xl,yy,xc,yyc=LagChebfun(int(sl.val))
        l.set_ydata(yy)#(t-x[0])*(t-sl[0].val)*(t-sl[1].val)*(t-sl[2].val)*(t-x[-1]))
        w.set_xdata(xl)
        w.set_ydata(f(xl))
        z.set_xdata(xc)
        z.set_ydata(f(xc))
        m.set_ydata(yyc)
        grid()
        #axis('tight')
        draw()
        
    sl.on_changed(update)
