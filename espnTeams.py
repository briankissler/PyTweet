# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:08:58 2019

@author: bk
"""

import json, requests

#url ='http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams'

def getWinner(eventid):
    
    url = 'http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401114171'
   
    response = requests.get(url)
    response.raise_for_status()

    scoreData = json.loads(response.text)

    for competitors in scoreData['header']['competitions'][0]['competitors']:
        if competitors['winner']:
            print (competitors['team']['name'] )
            winnerIs = competitors['team']['name']  
            for url in competitors['team']['logos']:
                print(url['href'])        
                winnerLogo = url['href']  
    
    return winnerIs, winnerLogo
    
def getTeamInfo(myTeam):
    
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
    
    nextEventName = t['nextEvent'][0]['name']
    
    nextEvent= t['nextEvent'][0]['id'] 
    
    return nextEvent,logo

def getTeamScore(eventid):
    
    url = 'http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=' + eventid
   
    response = requests.get(url)
    response.raise_for_status()
    
    scoreData = json.loads(response.text)
    
    ScoreType = 'TEST' 
    
    #if no current use previous
    if 'current' in scoreData['drives']:    
        teamDrive = scoreData['drives']['current']['team']['name']
        url = scoreData['drives']['current']['team']['logos'][0]['href']
        teamDriveDesc = scoreData['drives']['current']['description'] 
        Score =  scoreData['drives']['current']['isScore']    
        if 'displayResult' in scoreData['drives']['current']:
            ScoreType =  scoreData['drives']['current']['displayResult'] 
            theScoreIs = str( scoreData['drives']['current']['plays'][-1]['awayScore'] )
            theScoreIs = theScoreIs + ' - ' + str ( scoreData['drives']['current']['plays'][-1]['homeScore'] ) 
        else:
            ScoreType = 'TEST'
            theScoreIs = ' '
    else:
        teamDrive = scoreData['drives']['previous'][-1]['team']['name']
        url = scoreData['drives']['previous'][-1]['team']['logos'][0]['href']
        teamDriveDesc = scoreData['drives']['previous'][-1]['description'] 
        Score =  scoreData['drives']['previous'][-1]['isScore']
        if 'displayResult' in scoreData['drives']['previous'][-1]:
            ScoreType =  scoreData['drives']['previous'][-1]['displayResult'] 
            theScoreIs = str( scoreData['drives']['previous'][-1]['plays'][-1]['awayScore'] )
            theScoreIs = theScoreIs + ' - ' + str ( scoreData['drives']['previous'][-1]['plays'][-1]['homeScore'] ) 
        else:
            ScoreType = 'TEST'
            theScoreIs = ' '
    
    return url, teamDrive, teamDriveDesc, Score, ScoreType, theScoreIs