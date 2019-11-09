# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:43:32 2019

@author: bk
"""

import pytz

local_tz = pytz.timezone('America/Phoenix')

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary

def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S')

#print(aslocaltimestr(datetime(2010,  6, 6, 17, 29, 7, 730000)))
#print(aslocaltimestr(datetime.strptime('2019-11-09T20:30Z', '%Y-%m-%dT%H:%MZ')))
#print(aslocaltimestr(datetime.utcnow()))