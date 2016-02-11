#!/usr/bin/python

# the first line is to enable linux/Mac system to run this script as server script using "websocketd --port==8080 ./story.py" command

# code below import the necessary modules to support the streaming of data

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor
from tweepy.streaming import StreamListener
import Unicodedata
import re
import time

# run main function
if __name__ == '__main__':

    # twitter consumer key, consumer secret, access token, access secret.
    ckey="GVkuYv7N4B3G6GzruD2uCM9C0"
    csecret="obT4SpMgkIfUwbm2l5mYGIHUpCD3sfR9QH63PAKZ1Vxib6Zp4N"
    atoken="488346238-0A9NqkBr4Cli7BFx2Ro7023b0yeQTuwiUBDwD9od"
    asecret="vZdQ3CgKGB0b1lsmk2XLSkNSrORCaNZMYjhWH055sB02b"

    # tweepy code to setup the API key for later data extraction from twitter
    auth = AppAuthHandler(ckey, csecret)
    api = API(auth)

    # the loop that keeps getting twitter data and provide it to the client index.html
    while(True):
	print "#clearcode#"
        for tweet in Cursor(api.search, q='superbowl',lang="en",count=100).pages(2):
            for subtweet in tweet:
                try:
                    # re organizing the format of tweets to fit the streaming display better
                    userid=subtweet.id
                    content=subtweet.text.lower()
                    timeline=str(subtweet.created_at)
                    source=subtweet.source
                    result= "Tweet #"+"\nuserid:"+"{0:20}".format(userid)+" tweeted\n"+"{0:160}".format(content[3:].encode('utf-8'))+"\nat "+"{0:20}".format(timeline)+ " from "+"{0:20}".format(source)+"\n"
                    print result
                except UnicodeEncodeError:
                    # catching ascii encoding errors to prevent accidental server disconnectioin
                    pass
            break
        time.sleep(600)



    









