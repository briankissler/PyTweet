# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:43:32 2019

@author: bk
"""

import pytz

from datetime import datetime

local_tz = pytz.timezone('America/Phoenix')

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary

def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S')

#print(aslocaltimestr(datetime(2010,  6, 6, 17, 29, 7, 730000)))
#print(datetime.strptime(aslocaltimestr(datetime.strptime('2019-11-10T18:00Z', '%Y-%m-%dT%H:%MZ')),'%Y-%m-%d %H:%M:%S'))
#print(datetime.strptime(aslocaltimestr(datetime.utcnow()),'%Y-%m-%d %H:%M:%S'))

#gameTime = datetime.strptime(aslocaltimestr(datetime.strptime('2019-11-11T01:20Z', '%Y-%m-%dT%H:%MZ')),'%Y-%m-%d %H:%M:%S')
#rightNow = datetime.strptime(aslocaltimestr(datetime.utcnow()),'%Y-%m-%d %H:%M:%S')
#
#print(gameTime)
#print(rightNow)
#
#if gameTime <=  rightNow:
#    print('Game HAS started')
#else: print('Game has NOT started')
