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
