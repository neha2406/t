#!/usr/local/env python

import tweepy
import twitter
from tweepy import OAuthHandler
 
consumer_key = 'gLDzwf04s32QjjIj17PGBo4WB'
consumer_secret = 'hJl8Y23S3wASY8L3KPcKUhWlGKTHmocv2BTkNzlZ1HyME4cqIX'
access_token = '933511403456970752-PAwmIub38XxQUMjOO9OspKBKb1KlW6X'
access_secret =  '3hwxqsn9dTAFDZ73YFupTmESXpOOso19Aue6rn5tfqNpb'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(1):
# print(status.text)

search = api.GetSearch("Russia") # Replace happy with your search
for tweet in search:
   print(tweet.id, tweet.text)

