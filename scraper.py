import tweepy
import config

def getClient():
    #Initializes Tweepy client with tokens from Twitter developer account
    client = tweepy.Client(bearer_token=config.bearer_token, 
                           consumer_key=config.consumer_key,
                           consumer_secret=config.consumer_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)
    
    return client

def scrapeQuery(query, count):
    client = getClient()
    
    #Searches recent tweets based off of parameters in tsa.py and extracts data
    tweets = client.search_recent_tweets(query=query, max_results=count)
    tweetData = tweets.data
    textList = []
    
    #If the Tweet data exists then it adds all the data received to the list for analysis
    if not tweetData is None and len(tweetData) > 0:
        for tweet in tweetData:
            textList.append(tweet.text)
            
    return textList