
import tweepy
from tweepy import OAuthHandler

consumer_key = 'gLDzwf04s32QjjIj17PGBo4WB'
consumer_secret = 'hJl8Y23S3wASY8L3KPcKUhWlGKTHmocv2BTkNzlZ1HyME4cqIX'
access_token = '933511403456970752-PAwmIub38XxQUMjOO9OspKBKb1KlW6X'
access_secret =  '3hwxqsn9dTAFDZ73YFupTmESXpOOso19Aue6rn5tfqNpb'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)




from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
