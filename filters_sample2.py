# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:15:11 2013

@author: Agtek
"""
from pylab import *
from agtek import *
from scipy import signal

x = sin(linspace(0,500,1024)) + 0.5 *cos(linspace(0,750,1024)) + \
    randn(1024)*0.2 + 0.2*cos(linspace(0, 10000 , 1024))
    
plot(x[:100])

#Spectrum with different methods

#FFT
periodogram(x)
#Welch
figure()
psd(x)
#AR model
figure()
pcov(x, 15)

## Filters

#Moving average
xma = ma(x, 5)
figure()
plot(x)
plot(xma)

#FIR low pass filter
b = signal.firwin(100, cutoff=.2, window="hamming", nyq=0.5)
#plot_filterz(b)
xfir =  signal.lfilter(b, 1, x)
figure()
plot(x)
plot(xfir)
periodogram(xfir)

subplot(2, 3, 1)
plot(x)
ylim([-2, 2])
subplot(2, 3, 2)
plot(xma)
ylim([-2, 2])
subplot(2, 3, 3)
plot(xfir)
ylim([-2, 2])
subplot(2,3,4)
psd(x)
subplot(2,3,5)
psd(xma)
subplot(2,3,6)
psd(xfir)
savefig('monta.png')

show()



