# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 10:44:27 2013

@author: mpastell
"""

#!/usr/bin/env python

# Haversine formula example in Python
# Author: Wayne Dyck

import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
    
#p1 = (60.597030,  24.729146)
#p2 = (60.597837, 24.730920)

#print distance(p1, p2)