# StorytellingAndStreamingData
HW1

This live streaming is for tweets from New York City on football/SuperBowl 

Name: Yao Yang
Date: Feb 10, 2016  1:00 am

-using stream method instead of continous search API in case search does not count as streaming. 2016/02/17


- Instruction to execute the streaming application 
 
      *Websocket Server running on python script
 
      *files include:  story.py,  index.html
 
       *require websocketd installed, can use command "brew install websocketd" for Mac or  mannual add path to websocketd file into the environment path in Linux

       after "chmod +x ./story.py" 

       run in command line "websocketd --port=8080 ./story.py"

       open index.html in chrome browser and the streaming should start.



- Find, or create, a stream of data. This can be anything you find compelling, and can be an event stream or a polled API. Write a        README.md describing what an individual message in the stream represents in the real world, and therefore what volume of messages     you expect in the stream. (40%)

    each individual message in the stream is composed of the creation timeline, sender username, tweet content.

    The real world meaning of these individual messages are public opinions expressed by people from New York city on   
    NFL/superbowl/football topics. Be the sender a 10 years old or a 80 years old, a man or a women, positive or negative, all public     opinions get collected. 

     In later assignments, such information/opinions could go through sentiment analysis or filtering and provide us a unique view on      current affairs.

     Why tweets? the giant collection of tweets from new york may seem messy at current stage. However, with certain analysis or      
     filtering we could produce more interesting updates to public about what people in new york city thinks about superbowl. 

 
     The estimated volume of messges are ~10000 tweets/hr (estmated by observation for multiple 10 secs window and take the average        using this streaming application)

     The purpose of this streaming is to eventually serve as summary of current regional opinions from New York City on the recent hot      sport topic: football.

     why this matters? 

     Football is a very popular event and many people cares about it. 

     But newspaper, TV shows have latencies when reporting public opinions on such topics as the publication process takes time.  

     By streaming and doing some prelimilary processing of regional tweets on this topic, we can provide the public a more current 
     view of the trending opinions on the topics that they care about. 


- Consume the messages in the stream using technology of your choice. (40%) Your solution should expect to stay on forever. It should:
     * consume the stream from its source
     story.py utilizes Twitter API to search recent tweets pertaining to the topic "Superbowl"

     * perform any basic cleaning, transformations, or filters (optional)
     story.py reorganize the retrieved tweet information and rearrange them into the desired format as displayed in the     
     index.html/printed in the terminal

     * writes the output of the consumer to stdout so we can see it in a terminal
     story.py uses print command to print out each of the rephrased tweets.

- Create a websocket server that emits the messages and webpage that consumes them. The webpage can be as simple or as complex as   
    you'd like; we simply want to make sure everyone can get data onto a webpage. Plese use the Chrome web browser. (20%)
  
     open index.html in google after starting the Websocketd server by following the guideline in the instruction section
     All tweets are displayed in chronological order. 100 tweets are displayed in each round.
     Streaming data refreshed every 10 mins (this can be changed by modifying the story.py code last line  "time.sleep(xx)"  refresh  
     time xx sec)




*possible error and solutions:
-- InsecurePlatformWarning,  python does not have certificate module, use the following line to install for python.
pip install pyopenssl ndg-httpsclient pyasn1

-- Error: couldn't find file at \user\xxx\xxx\story.py^M    error,  need to "vi story.py" and delete "^M" characters at the end of each line to fit back into linux environment
