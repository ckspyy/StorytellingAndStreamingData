#!/usr/bin/python

# code below import the necessary modules to support the streaming of data
# partial code reference to http://stats.seandolinar.com/collecting-twitter-data-using-a-python-stream-listener/
# partial code reference to http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
# partial code reference to http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# partial code reference to http://socialmedia-class.org/twittertutorial.html

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


# the Listener class is used to stream tweets live.
class Listener(StreamListener): 
    def on_data(self, data):
        try:
            tweet=json.loads(data)
            result="{0:20}".format(tweet['created_at'])+"  user: "+"{0:15}".format(tweet['user']['screen_name'])+" tweeted:"+"{0:160}".format(tweet['text'])
            print result
            sys.stdout.flush()

        # catching exception where the utf-8 code endoding error occurs, as the target streaming data is english, the relatively rare tweets with rare character being ignored should be okay
        except BaseException, e:
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

    # setup the streaming process by inputing the credentials object 'auth'
    auth = OAuthHandler(ckey, csecret) 
    auth.set_access_token(atoken, asecret)
    keywords = ['superbowl','nfl','football'] #track list

    # code to actually start the streaming by intializing the Listener class 
    twitterStream = Stream(auth, Listener())
    # thie code below search through live tweets containing the keyword_lists in english from new york region
    twitterStream.filter(track=keywords, languages=['en'],locations=[-74,40,-73,41])    

    









