# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:15:10 2019

@author: bk
"""
import tweepy, time, sys, cred_twitter, requests, os, espnTeams, testGetTeam, myDateTime

from datetime import datetime

#argfile = str(sys.argv[1])

def twitter_api():
    
    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = cred_twitter.CONSUMER_KEY#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = cred_twitter.CONSUMER_SECRET#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = cred_twitter.ACCESS_KEY#'#'#keep the quotes, replace this with your access token
    ACCESS_SECRET = cred_twitter.ACCESS_SECRET#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api


def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")
        
        
asu = testGetTeam.myTeam('ORST')

print( asu.nextEventName )
print( asu.nextEvent )
print( asu.nextEventComplete )
print( asu.nextEventDate )


        
#nextEvent,nextEventDate,nextEventComplete,logo = espnTeams.getTeamInfo('ASU')       

#DriveTeam, DriveDesc, isScore, ScoreWhat =  espnTeams.getTeamScore(eventid)

#for line in f:
 #   api.update_status(line)
 #   time.sleep(900)#Tweet every 15 minutes
 
 #loop through until ScoreType = 'End of Game'
 
ScoreWhat = '' 

#nextEventDate =aslocaltimestr(datetime.strptime(asu.nextEventDate, '%Y-%m-%dT%H:%MZ'))

nextEventDate = datetime.strptime(asu.nextEventDate, '%Y-%m-%dT%H:%MZ')

print(myDateTime.aslocaltimestr(nextEventDate))
print(myDateTime.aslocaltimestr(datetime.utcnow()))

gScoreis = 0
while not asu.nextEventComplete and  myDateTime.aslocaltimestr(nextEventDate) <  myDateTime.aslocaltimestr(datetime.utcnow()):
    
    url, DriveTeam, DriveDesc, isScore, ScoreWhat, Scoreis =  espnTeams.getTeamScore(asu.nextEvent)
    
    if isScore and gScoreis != Scoreis:
        tweet_image(url,ScoreWhat + '!!!! ' +  DriveTeam + ' ~ ' + DriveDesc + '   ' + Scoreis)
        
    if ScoreWhat == 'End of Game':
        winTeam, winTeamLogo = espnTeams.getWinner(asu.nextEvent)
        tweet_image(winTeamLogo,winTeam + ' WIN ~    ' + Scoreis)
        break
    gScoreis = Scoreis    
    time.sleep(60)#Tweet every 6 minutes
