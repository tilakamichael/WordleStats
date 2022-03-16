import tweepy
import config

def getClient():
    #Initializes Tweepy client with tokens from Twitter developer account
    client = tweepy.Client(bearer_token=config.bearer_token, 
                           consumer_key=config.consumer_key,
                           consumer_secret=config.consumer_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)
    
    print ("Using Tweepy version " + tweepy.__version__)
    return client

def scrapeQuery(query):
    client = getClient()
        
    tweetList = []

    #Goes through multiple pages and pulls tweets from each of those pages
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=5000):
        tweetList.append(tweet.text)
    
    return tweetList