#!/usr/bin/python

# this program is for the developers to monitor the rate of tweets incoming
# alert will be triggered to request some human being to look at the current topics and conduct a more detailed report/ find other popular topics for the streaming app
import redis
import json
import time
import sys

# connect to the local redis server to retrieve data for streaming rate calculation
conn = redis.Redis()

# continuously calculate the rate and output the result to the monitoring website
while True:
    #  retrieve the time intervals between each tweets in last 300 secs
    keys = conn.keys()
    values = conn.mget(keys)

    # store the intervals between each tweet into the variable intervals
    try:
        intervals = [float(v) for v in values]
    # handle type error by skipping current loop in case something went wrong when the data is stored
    except TypeError:
        continue

    # if there is data in variable "intervals", calculate the rate of streming base on avaible data
    if len(intervals):
        rate = sum(intervals)/float(len(intervals))
    # if there is no data in varaible "intervals", output streaming rate of max integer
    else:
        rate = float(sys.maxint)

    # if it takes more than 5 sec to receive a related tweet, it means people may not be as interested on the current topic we are monitoring now. trigger a human investigation to make sure the streaming website is catching up with the hot topic.
    if rate > 5: 
        print " current rate is:"+str(round(rate,2))+".  People seems to be less excited about superbowl now, shall we take a look and find some other topic?"
    # if a tweet comes in every less than 0.1 sec, so many people are talking about this event and maybe it's a good idea to provide more details to the current topic by requesting some human being to look into the current trend
    elif rate<0.1:
        print "current rate is:"+str(round(rate,2))+".  Everyone in New York is so excited about Superbowl, let's build another section on the website to catach the most recent important updates on the trend!"
    else:
        print "Current Tweet Streaming Rates on Superbowl is:"+str(round(rate,2))+"sec/tweet"
    
    # make sure the output is transmitted to the server instantly 
    sys.stdout.flush()
    # update the rate every 5 sec
    time.sleep(5)
