import tweepy
import config
from datetime import datetime 

def getClient():
    #Initializes Tweepy client with tokens from Twitter developer account
    client = tweepy.Client(bearer_token=config.bearer_token, 
                           consumer_key=config.consumer_key,
                           consumer_secret=config.consumer_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)
    
    print ("Using Tweepy version " + tweepy.__version__)
    return client

def scrapeQuery(query, startTime, endTime):
    client = getClient()
        
    tweetList = []
    
    #Time values
    if (startTime == '' and endTime == ''):
        startTime = datetime.today().strftime("%Y-%m-%d") + "T00:00:00Z"
        endTime = datetime.today().strftime("%Y-%m-%d") + "T23:59:59Z"
        print (startTime)
    else:
        startTime = str(startTime)
        endTime = str(endTime)
        print (startTime)

    #Goes through multiple pages and pulls tweets from each of those pages
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, start_time=startTime, end_time=endTime, max_results=100).flatten(limit=10):
        tweetList.append(tweet.text)
    
    return tweetList