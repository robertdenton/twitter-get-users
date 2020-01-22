#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter, csv, os
from datetime import datetime
from pytz import timezone
from functions import getSecret

# Set current dir
dir_path = os.path.dirname(os.path.realpath(__file__))

secrets = getSecret("twitter")

api = twitter.Api(consumer_key = secrets['consumer_key'],
                  consumer_secret = secrets['consumer_secret'],
                  access_token_key = secrets['access_token'],
                  access_token_secret = secrets['access_token_secret'])

# Test user list
users = ["denverpost","dptv","dpostsports"]
# Prime time user list
#users = ["denverpost","DPostSports","thknwco","coloradoutdoors","PostBroncos","cannabist","postpreps","denveropinion","avsnews","DPRockies","nuggetsnews","prepfootball","prepbasketball","pueblonews","arvadanews","aspennews","brightonnews","thorntonnews","wheatridge","vailnews","sterlingnews","steamboatnews","parkernews","longmontnews","CherryHills","centennialnews","DenverPostBrk","bouldernews","castlepines","denverpolitics","westernslope","denverlacrosse","GoldenNews","greeleynews","glendalenews","evergreennews","erienews","Englewood","commercecity","lakewoodnews","prepwrestling","denvercrime","rapidsnews","auroranews","broomfieldnews","castlerock","denverbusiness","DenverCycling","durangonews","denvereducation","denvernews","thespot","DPOlympics","AFAnews","conifernews","denverpostlite","greendenver","littletonnews","lovelandnews","prepsoccer","edgewaternews","prepxctrack","prephockey","coloradoeconomy","westminsternews","cospringsnews","denverpostvideo","denverphotos","CapturedBlog","yourhub","denverfood","denverentertain","eletters","stealthistrack","vivacolorado"]
# No @prepbasketballco, @dptv, @auroratheatertrial

data = {}
success = True
#pp = pprint.PrettyPrinter(width=41,compact=True)

def mountain(orig=None):
    orig_dt = datetime.strptime(orig, "%a %b %d %H:%M:%S %z %Y")
    mtn_dt = orig_dt.astimezone(timezone("America/Denver"))
    formatted_mtn_dt = mtn_dt.strftime("%a %b %d %Y %H:%M:%S %z")
    return formatted_mtn_dt

for i in users:
    try:
        user = api.GetUser(screen_name=i)
    except Exception:
        print("User not found: " + i)
        success = False

    if success == True:
        tweetjson = api.GetUserTimeline(screen_name=i, count=1)
        tweet = tweetjson[0]

        data[i] = {
            "name": user.name,
            "followers": user.followers_count,
            "url": user.url,
            "verified": user.verified,
            "created": mountain(user.created_at),
            "last_tweet": tweet.text,
            "last_tweet_time": mountain(tweet.created_at)
        }
    # Else skip it and error is printed

#print(data)

with open('test.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['handle', 'name', 'url', 'followers', 'created', 'verified', 'last_tweet_time', 'last_tweet'])
    for key, value in data.items():
        writer.writerow([key, value['name'], value['url'], value['followers'], value['created'], value['verified'], value['last_tweet_time'], value['last_tweet']])