# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 11:06:09 2013

@author: Agtek
"""

import u3

LJ = u3.U3()

arvot = []

for i in range(10):
    V = LJ.getAIN(0)
    arvot.append(V)
    print(V)


plot(arvot)



