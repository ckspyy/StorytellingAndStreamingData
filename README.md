# StorytellingAndStreamingData
HW1

This live streaming is for tweets about SuperBowl  (frequency every 10mins)

Name: Yao Yang
Date: Feb 10, 2016  1:00 am


-Instruction to execute the streaming application 

*Websocket Server running on python script

*files include:  story.py,  index.html

*require websocketd installed, can use command "brew install websocketd" for Mac or  mannual add path to websocketd file into the environment path in Linux

after "chmod +x ./story.py" 

run in command line "websocketd --port=8080 ./story.py"

open index.html in chrome browser and the streaming should start.



- Find, or create, a stream of data. This can be anything you find compelling, and can be an event stream or a polled API. Write a README.md describing what an individual message in the stream represents in the real world, and therefore what volume of messages you expect in the stream. (40%)

each individual message in the stream is composed of the sender userid of tweet, tweet content, time and the device on which the tweet is created.
The real world meaning of these individual messages are public opinions about the recent hot topic event Super Bowl from social media. be it from a 10 years old or a 80 years old, a man or a women, positive or negative, all these opinions get collected.  
In later assignments, such information/opinions could go through sentiment analysis or filtering and provide us a unique view on current affairs.

The estimated volume of messges are ~1500 related tweets/hr (based on observation using this streaming application)
The message volume could be increased by incorporating more search key words if needed. 


- Consume the messages in the stream using technology of your choice. (40%) Your solution should expect to stay on forever. It should:
  
  * consume the stream from its source
  
  story.py utilizes Twitter API to search recent tweets pertaining to the topic "Superbowl"

  * perform any basic cleaning, transformations, or filters (optional)
  
  story.py reorganize the retrieved tweet information and rearrange them into the desired format as displayed in the index.html/printed in the terminal

  * writes the output of the consumer to stdout so we can see it in a terminal
  
  story.py uses print command to print out each of the rephrased tweets.

- Create a websocket server that emits the messages and webpage that consumes them. The webpage can be as simple or as complex as you'd like; we simply want to make sure everyone can get data onto a webpage. Plese use the Chrome web browser. (20%)
  
  open index.html in google after starting the Websocketd server by following the guideline in the instruction section
  
  All tweets are displayed in chronological order. 100 tweets are displayed in each round.
  
  Streaming data refreshed every 10 mins (this can be changed by modifying the story.py code last line  "time.sleep(xx)"  refresh time xx sec)




*possible error and solutions:
-- InsecurePlatformWarning,  python does not have certificate module, use the following line to install for python.
pip install pyopenssl ndg-httpsclient pyasn1

-- Error: couldn't find file at \user\xxx\xxx\story.py^M    error,  need to "vi story.py" and delete "^M" characters at the end of each line to fit back into linux environment
