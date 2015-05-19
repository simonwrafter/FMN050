# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:28:12 2015

@author: claus
"""

def read_acc_data(file='garden.txt'):
    r"""
    reads coordinates from a file (default: garden.txt)
    and returns three lists:
    
    t time  (sec)
    
    x acceleration in x-direction $(m/sec^2)$
    
    y acceleration in y-direction $(m/sec^2)$
    
    
    Call
    
    t,xacc,yacc=read_acc_data()
    """
    fi=open(file,'r')
    x,y,t=[],[],[0]
    for line in fi.readlines():
        if line.startswith('#') or line=='\n': continue
        xi,yi,zi,ti=line.split()
        x.append(float(xi))
        y.append(float(yi))
        t.append(t[-1]+float(ti)/1000.)  # in seconds
    t=t[:-1]
    return t,x,y