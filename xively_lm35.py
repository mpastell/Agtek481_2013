# -*- coding: utf-8 -*-
"""
A simple program to upload data to Xively
See feed at https://xively.com/feeds/106775
xively-python documentation: http://gnublade.github.io/xively-python/
@author: Matti Pastell
"""

import xively
from scipy import randn
import time
import u3

KEY = "G2_KFCfVBlTht9IkIMQH4PXjd3qSAKxxdmVNalRZM2NaYz0g"
FEED = 106775


api = xively.XivelyAPIClient(KEY)
feed = api.feeds.get(FEED)

LJ = u3.U3()

try: #Try to create a feed
    datastream = feed.datastreams.create("Matti", tags="teacher", unit= xively.Unit(symbol = u"\u2103"))
except: #If creating fails try to get existing feed
    datastream = feed.datastreams.get("Matti")

while True:
    datastream.current_value = round(LJ.getAIN(0) * 100, 2)
    datastream.update(fields=['current_value'])
    time.sleep(10)
 

