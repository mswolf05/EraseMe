import tweepy
import os
from dotenv import load_dotenv
import pdb
import csv
from tkinter import *
from datetime import datetime, timedelta
from subprocess import Popen

consumer_key = input("Consumer Key (API Key): ")
consumer_secret = input("Consumer Secret (API Secret): ")
access_token = input("Acess Token: ")
access_token_secret = input("Acess Token Secret: ")

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
timeline = tweepy.Cursor(api.user_timeline).items()

cutoff_date = input("Perform action on all Twitter activity prior to which date (MM/DD/YYYY): ")

cutoff_date = datetime.strptime(cutoff_date, "%m/%d/%Y").strftime("%Y-%m-%d")
cutoff_date = datetime.strptime(cutoff_date , '%Y-%m-%d')

print("Please wait while we gather your Twitter activity...")

tweet_list = []
for tweet in timeline:
    if tweet.created_at <= cutoff_date:
        info = {
        "tweet_id": tweet.id,
        "tweet_text": tweet.text,
        "tweet_created": tweet.created_at.strftime('%m/%d/%Y'),
        "retweet": tweet.retweeted,
        "like": tweet.favorited,
        "tweet_delete": True
        }
        tweet_list.append(info)
