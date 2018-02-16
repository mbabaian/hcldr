import tweepy
from tweepy.streaming import StreamListener
from time import sleep
from credentials import *

# https://stream.twitter.com/1.1/search/tweets.json?q=%23hcldr
# Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

# You can limit number of tweets returned in .items()
for tweet in tweepy.Cursor(api.search,q='#hcldr').items(1):
	try:
		print('\nTweet by: @' + tweet.user.screen_name)

		#Retweet tweets as they are found
		tweet.retweet()
		print('Retweeted the tweet')

		#sleep(60)

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break

#api.update_status(status="Hello World")
