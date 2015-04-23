# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:22:37 2015

@author: simon
"""

from  scipy import *
from  pylab import *

day    = array([ 7.,    8.,    9.,   10.,   11.])
energy = array([27.93, 46.98, 31.95, 31.68, 21.])
enEdit = energy + array([0., 0., 0., -0.01, 0.])

dayExtreme = linspace(min(day), max(day)+4, 1000)

figure(1)
clf()
grid(1)

pFit = polyfit(day, energy, len(day)-1)
pVal = polyval(pFit, dayExtreme)
print(pFit)
plot(dayExtreme, pVal)
plot(day, energy, '*')

figure(2)
clf()
grid(1)

V = vander(day)
a = solve(V, energy)
print(a)
pVal = polyval(a, dayExtreme)

plot(dayExtreme, pVal)
plot(day, energy, '*')

figure(3)
clf()
grid(1)

def L(x, xm, i):
    prod = 1
    for j in range(len(xm)):
        if i != j:
            prod *= (x - xm[j]) / (xm[i]- xm[j])
    return prod

def interpol(x, xm, ym):
    prod = 0
    for i in range(len(xm)):
        prod += ym[i]*L(x, xm, i)
    return prod

lagY = [interpol(i, day, energy) for i in dayExtreme]

plot(dayExtreme, lagY, 'g')
plot(day, energy, '*g')

lagYedit = [interpol(i, day, enEdit) for i in dayExtreme]

plot(dayExtreme, lagYedit, 'r')
plot(day, enEdit, '*r')

index = 3
print(abs((abs(energy[index] - enEdit[index])/max(energy[index], enEdit[index])) / (abs(lagY[-1] - lagYedit[-1])/max(lagY[-1], lagYedit[-1]))))
