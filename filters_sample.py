# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:11:20 2013

@author: mpastell
"""

from pylab import *
from agtek import *

data = loadtxt("kavely.txt")
x = data[:,0]
x0 = x - x.mean()

plot(x0)
xma = ma(x0, 10)
plot(xma)

#Tasks

#1. Suodata x0 liukuvalla keskiarvolla, jossa on 5, 11 ja 19 pistettä
# Piirrä tulokset samaan kuvaan.

#2. Vertaa 11 pisteen suodatusta mediaanisuodattimeen


#3. Suodata aineisto x0 FIR ja IIR suodattimella 10Hz alipäästösuodattimella

#4. Laske suodatetusta aineistosta (valitse 1) FFT, AR ja Welch estimaatit

