
# This live streaming backend rate monitor 
It is current for tweets from New York City on football/SuperBowl 

Name: Yao Yang

Date: Feb 19, 2016  1:00 pm


#Instruction to execute the streaming application 

 this application utilizes Websocket Server running on python script
 
 - Files include:  stream.py(record stream data into redis),monrate.py(calculate rate from redis data)  monitor.html(human-readable system)   sample.jpg(to show how the monitor.html looks like when running the app)
 
 - require websocketd installed, can use command "brew install websocketd" for Mac or  mannual add path to websocketd file into the environment path in Linux

after "chmod +x ./monrate.py"

run in command line 

"python stream.py"

"websocketd --port=8080 ./monrate.py"

open monitor.html in chrome browser and the streaming rate monitoring should start.



1.  Build a system to track the rate of a stream of data. You can use the stream of data you found in exercise 1 or a new stream. (40%)

  The stream data used is twitter tweets from New York City region on SuperBowl/football topics.
  
  Why does the rate of twitter stream mean?
  
  The rate of the streams is one method to represente how popular a topic is on the social media/internet.
  
  Monitoring the rate of tweets on a certain topic allows us to have a straightforward idea whether a topic is trending or dieing out.
  Knowding the current popularity of certain topic, we can modify the topic to be streamed or put in more resources to build more
  detailed and more comprehensive reports on the trending topic to attract more public audience to our streaming application.
  
  The current rate of tweets on football/superbowl topics is ~ 0.2 sec/tweet


2.  Build an alerting system to let you know when the rate does something interesting to you. This could be that the rate has increased above a threshold, or decreased, or demonstrates "unlikely" behaviour. (40%)
    - if it takes more than 5 sec to receive a related tweet, it means people may not be as interested on the current topic we are monitoring now. trigger a human investigation to make sure the streaming website is catching up with the hot topic.

    - if a tweet comes in every less than 0.1 sec, so many people are talking about this event and maybe it's a good idea to provide more details to the current topic by requesting some human being to look into the current trend
 
    - if the rate is within a normal range of its usual fluctuation, just show the current rate on the webpage


3.  Connect the alerting system to a human-readable system. This could be, for example, a webpage, a slack channel, or a twitter bot. (20%)
  
  open monitor.html in chrome after starting the Websocketd server by following the guideline in the instruction section

  The tweet streaming rate will diplayed on the webpage.
  
  if anything goes wrong with the rates, an alert will be shown on the webpage instead of the simple current rate message
  a new rate message/rate alert is inserted every 5 sec.
  
  once the total amount of message on the webpage reaches 100, the webpage will clear all old messages.




*possible error and solutions:
-- InsecurePlatformWarning,  python does not have certificate module, use the following line to install for python.
pip install pyopenssl ndg-httpsclient pyasn1

-- Error: couldn't find file at \user\xxx\xxx\story.py^M    error,  need to "vi story.py" and delete "^M" characters at the end of each line to fit back into linux environment
