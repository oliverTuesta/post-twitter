import tweepy 
import configparser
import pandas as pd

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_secret = config['twitter']['api_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# posts a tweet
content = input('What would you like to tweet? ')
api.update_status(content)
print('Tweeted: {}'.format(content))
