# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:32:24 2015

@author: simon
"""

from  scipy import *
from  pylab import *

x1 = linspace(-1, 1, 3)
x2 = linspace(-1, 1, 9)
x3 = linspace(-1, 1, 15)
x4 = linspace(-1, 1, 100)
xmega = linspace(-1, 1, 5000)

def f(x):
    return 1/(1 + 25 * x**2)

y1 = [f(i) for i in x1]
y2 = [f(i) for i in x2]
y3 = [f(i) for i in x3]
y4 = [f(i) for i in x4]

figure(1)
clf()
grid(1)

plot(x1, y1, '*b', xmega, polyval(polyfit(x1, y1, len(x1)-1), xmega), 'b')
plot(x2, y2, '*g', xmega, polyval(polyfit(x2, y2, len(x2)-1), xmega), 'g')
plot(x3, y3, '*r', xmega, polyval(polyfit(x3, y3, len(x3)-1), xmega), 'r')
#plot(xmega, polyval(polyfit(x4, y4, len(x4)-1), xmega), 'k', label='black')

title('Equidistant samples')
xlabel('x')
ylabel('p(x)')


def cX(n):
    x = []
    for i in range(1, n+1):
        x.append(cos((2*i-1)/(2*n) * pi))
    return x

xc1 = cX(3)
xc2 = cX(9)
xc3 = cX(15)
xc4 = cX(100)

yc1 = [f(i) for i in xc1]
yc2 = [f(i) for i in xc2]
yc3 = [f(i) for i in xc3]
yc4 = [f(i) for i in xc4]

legend()

figure(2)
clf()
grid(1)

plot(xc1,yc1,'*b', xmega, polyval(polyfit(xc1, yc1, len(xc1)-1), xmega), 'b')
plot(xc2,yc2,'*g', xmega, polyval(polyfit(xc2, yc2, len(xc2)-1), xmega), 'g')
plot(xc3,yc3,'*r', xmega, polyval(polyfit(xc3, yc3, len(xc3)-1), xmega), 'r')
#plot(xc4,yc4,'*k', xmega, polyval(polyfit(xc4, yc4, len(xc4)-1), xmega), 'k')


title('Chebyshev samples')
xlabel('x')
ylabel('p(x)')