# -*- coding: utf-8 -*-
"""
A simple program to upload data to Xively
See feed at https://xively.com/feeds/106775
xively-python documentation: https://github.com/xively/xively-python
@author: Matti Pastell
"""

import xively
from scipy import randn
import time

KEY = "G2_KFCfVBlTht9IkIMQH4PXjd3qSAKxxdmVNalRZM2NaYz0g"
FEED = 106775

api = xively.XivelyAPIClient(KEY)

feed = api.feeds.get(FEED)


try: #Try to create a feed
    datastream = feed.datastreams.create("Matti", tags="teacher")
except: #If creating fails try to get existing feed
    datastream = feed.datastreams.get("Matti")

while True:
    datastream.current_value = randn()
    datastream.update(fields=['current_value'])
    time.sleep(10) 
 

