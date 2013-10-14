# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 09:10:45 2013

@author: Agtek
"""

from pylab import *

#Kuvaaja funktiosta
x =  linspace(0, 10, 100)
sx = sin(x)
plot(x, sx)
xlabel("x")
ylabel("sin(x)")

#Voltage divider

def vdivide(R1, R2, U = 5):
    Uadc = (R2/(R1+R2))*U
    return(Uadc)
    
#Lasketaan arvot KTY:lle
kty = array([1508, 1640, 1779, 1924, 2000, 2077, 2237, 2404, 2578, 2759])
u = vdivide(kty, 2000)
plot(kty, u)
u2 = vdivide(kty, 1000)
plot(kty, u2)

#files
data = loadtxt("kavely.txt")
data2 = data*2
savetxt("kavely2.txt", data2)

plot(data)
plot(data[:, 0])
x = data[:,0]
data.mean(axis = 0)


x0 = x - x.mean()
t = linspace(0, 25.608, 6402)
plot(t, x)
show()

#Luetaan kuva
kuva = imread("Koala.jpg")
imshow(kuva)

subplot(2, 1, 1)
plot(data)

subplot(2, 1, 2)
imshow(kuva)



