#!/usr/bin/python

# this python program is to stream tweets and record the tweet arriving rate in local redis database for rate calculation
# monitoring rates allow the deverloper team to respond to hot topic changes.

# code below import the necessary modules to support the streaming of data
# partial code reference to http://stats.seandolinar.com/collecting-twitter-data-using-a-python-stream-listener/
# partial code reference to http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
# partial code reference to http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# partial code reference to https://github.com/mikedewar/RealTimeStorytelling

# the first line is to enable linux/Mac system to run this script as server script using "websocketd --port==8080 ./story.py" command
# 'tweepy' is the python module for Twitter data extraction/processing

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor
from tweepy.streaming import StreamListener
import time
import json
import sys
import redis


# the Listener class is used to stream tweets live.
class Listener(StreamListener): 
    def on_data(self, data):
        try:
            global last_arr
            global con
            current=float(time.time())
            if last_arr==0:
                last_arr=current
                con.set(last_arr,last_arr,300)
            else:
                con.setex(current,current-last_arr,300)
                last_arr=current

        # catching exception where the utf-8 code endoding error occurs, as the target streaming data is english, the relatively rare tweets with rare character being ignored should be okay
        except BaseException, e:
            print e
            pass

 
    # the function below prints error code of errors during the use of twitter API  
    def on_error(self, status):
        print "error code:"+status


# run main function to start streaming tweet data
if __name__ == '__main__':

    # the following four lines are setting the credentials to authorize the program to retrieve tweets from twitter.
    # the credentials are consumer key, consumer secret, access token, access secret.
    ckey="GVkuYv7N4B3G6GzruD2uCM9C0"
    csecret="obT4SpMgkIfUwbm2l5mYGIHUpCD3sfR9QH63PAKZ1Vxib6Zp4N"
    atoken="488346238-0A9NqkBr4Cli7BFx2Ro7023b0yeQTuwiUBDwD9od"
    asecret="vZdQ3CgKGB0b1lsmk2XLSkNSrORCaNZMYjhWH055sB02b"
    
    #establish connection to local redis database to store time stamps for another python program to calculate the streaming rate
    con =redis.Redis()
    last_arr=0

    # setup the streaming process by inputing the credentials object 'auth'
    auth = OAuthHandler(ckey, csecret) 
    auth.set_access_token(atoken, asecret)
    keywords = ['superbowl','nfl','football'] #track list

    # code to actually start the streaming by intializing the Listener class 
    twitterStream = Stream(auth, Listener())
    # thie code below search through live tweets containing the keyword_lists in english from new york region
    twitterStream.filter(track=keywords, languages=['en'],locations=[-74,40,-73,41])    

    









