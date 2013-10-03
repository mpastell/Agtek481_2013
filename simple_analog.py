# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 13:12:40 2013

@author: Matti Pastell
"""

import u3
import time

LJ = u3.U3()

while True:
    V = LJ.getAIN(0)
    print V
    time.sleep(1)