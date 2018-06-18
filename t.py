




import twitter


api = twitter.Api(consumer_key = 'gLDzwf04s32QjjIj17PGBo4WB' ,
consumer_secret='hJl8Y23S3wASY8L3KPcKUhWlGKTHmocv2BTkNzlZ1HyME4cqIX' ,
access_token_key= '933511403456970752-PAwmIub38XxQUMjOO9OspKBKb1KlW6X' ,
access_token_secret='3hwxqsn9dTAFDZ73YFupTmESXpOOso19Aue6rn5tfqNpb')

print(api.VerifyCredentials())

search = api.GetSearch("sridevi") 
for tweet in search:
    print(tweet.id, tweet.text)
