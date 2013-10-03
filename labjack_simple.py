# -*- coding: utf-8 -*-
"""
A basic script to collect data from one LabJack Channel

@author: Matti Pastell
"""

import u3
import time
from datetime import datetime

LJ = u3.U3()
LJ.configIO(FIOAnalog = 0xFF) # Set FIO channels as input

#Create a header
df = open("data.txt", "w")
df.write("Otsikko\n")
df.close()

while True:
    V = LJ.getAIN(6)
    
    aika = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")    
    
    #Save data
    df = open("data.txt", "a")
    df.write(aika + "," + str(V) + "\n")
    df.close()
    
    print(aika + " " + str(V))
    time.sleep(1)