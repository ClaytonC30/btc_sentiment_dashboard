import snscrape.modules.twitter as sntwitter
import pandas as pd

def fetch_tweets(query="Bitcoin", count=100):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(f'{query} lang:en').get_items():
        if len(tweets) == count:
            break
        tweets.append(tweet.content)
    return tweets

btc_tweets = fetch_tweets("BTC")
print(btc_tweets[:5])  # Preview tweets
