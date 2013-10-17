# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:29:47 2013

@author: Agtek
"""

import serial

portti = serial.Serial("com18", 57600)

while True:
    b = ord(portti.read())
    if b == 255:
        x = ord(portti.read())
        y = ord(portti.read())
        z = ord(portti.read())
        print x, y, z