import re
import tweepy
from creds import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

new_tweets = api.user_timeline(screen_name='realdonaldtrump', count=200)

with open('text_data/trumpy.txt', 'w') as f:
    for tweet in new_tweets:
        tweet = tweet.text
        tweet = re.sub("https?\:\/\/", "", tweet)          # links
        tweet = re.sub("t.co\/([a-zA-Z0-9]+)", "", tweet)
        tweet = re.sub("bit.ly\/([a-zA-Z1-9]+)", "", tweet)
        tweet = re.sub("Video\:", "", tweet)               # Videos
        tweet = re.sub("\n", " ", tweet)                   # new lines
        tweet = re.sub("\s+", " ", tweet)                  # extra whitespace
        tweet = re.sub("&amp;", "and", tweet)              # encoded ampersands
        f.write(tweet + '\n')
