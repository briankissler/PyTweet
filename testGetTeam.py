# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:46:34 2019

@author: bk
"""
import json, requests

class myTeam:
  def __init__(self,sport,team ):
      self.team = team
      self.sport= sport
      self.url ='http://site.api.espn.com/apis/site/v2/sports/football/'+sport+'/teams/' + self.team 
      response = requests.get(self.url)
      response.raise_for_status()
      teamData = json.loads(response.text)
      t = teamData['team']
      self.logo = t['logos'][0]['href']
      self.nextEventName = t['nextEvent'][0]['name']
      self.nextEvent= t['nextEvent'][0]['id']
      self.nextEventComplete = t['nextEvent'][0]['competitions'][0]['status']['type']['completed']
      self.nextEventDate = t['nextEvent'][0]['date']
      self.GameStatus = ''
      
  def IsComplete(self):
      self.url ='http://site.api.espn.com/apis/site/v2/sports/football/'+self.sport+'/teams/' + self.team 
      response = requests.get(self.url)
      response.raise_for_status()
      teamData = json.loads(response.text)
      t = teamData['team']
      self.nextEventComplete = t['nextEvent'][0]['competitions'][0]['status']['type']['completed']
      
  def GetGameStatus(self):
      self.url ='http://site.api.espn.com/apis/site/v2/sports/football/'+self.sport+'/teams/' + self.team 
      response = requests.get(self.url)
      response.raise_for_status()
      teamData = json.loads(response.text)
      t = teamData['team']
      self.GameStatus = t['nextEvent'][0]['competitions'][0]['status']['type']['name']
      
      
      
#asu = myTeam('college-football','ASU') 
#nebraska = myTeam('nebraska') 
#
#print( asu.nextEventName )
#print( asu.nextEvent )
#print( asu.nextEventComplete )
#print( asu.nextEventDate )
#asu.GetGameStatus()
#print(asu.GameStatus)



#print( nebraska.nextEventName )
#print( nebraska.nextEvent )
#print( nebraska.nextEventComplete )
#print( nebraska.nextEventDate )
#nextEvent,nextEventDate,nextEventComplete,logo = espnTeams.getTeamInfo('ARIZONA')

