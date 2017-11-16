import tweepy
from creds import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do."

api.update_status(status)