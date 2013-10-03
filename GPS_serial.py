# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 08:40:11 2013
Solution to GPS programming exercise
@author: Matti Pastell
"""

import serial
from haversine import distance
old = (0,0)
gps = serial.Serial("com20", 4800)

while True:
    raw = gps.readline().strip()
    #print raw
    
    #1. kohta
    f = open("gps.txt", "a")
    f.write(raw + "\n")
    f.close()
    
    #2. kohta
    lista = raw.split(",")
    lat = lista[2]
    longi = lista[4]    
    #print lat + " " +  longi
    
    #3. kohta
    kello = lista[1]
    aika = kello[0:2] + ":" + kello[2:4] + ":" + kello[4:6]
    #print kello[0:2] + ":" + kello[2:4] + ":" + kello[4:6]
    
    #4. kohta
    latD = float(lat[0:2]) + float(lat[2:])/60
    longD = float(longi[0:3]) + float(longi[3:])/60
    #print latD, longD
    
    #5. kohta
    current = (latD, longD)
    dist = distance(current, old)
    old = current
    
    print "kello:", aika, "koordinaatit:", latD, longD, "nopeus", "{:.2f}".format(dist*1000.0), "m/s" 
    
    