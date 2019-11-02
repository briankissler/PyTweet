# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:08:58 2019

@author: bk
"""

import json, requests

#url ='http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams'

def getTeamScore(myTeam):
    
    url ='http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/' + myTeam 
    response = requests.get(url)
    response.raise_for_status()

#teamData = json.loads(response.text)

#t = teamData['sports']

#print(t[0]['leagues'][0]['teams'][2]['team']['record']['items'][0]['stats'] )


    teamData = json.loads(response.text)

    t = teamData['team']
  
#nextEvent= t['nextEvent'][0]['id'] 
    logo = t['logos'][0]['href']
    nextEvent= t['nextEvent'][0]['name']
    return nextEvent,logo
#print(t['nextEvent'][0]['name'] )
#print(nextEvent )