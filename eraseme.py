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

# prompt user for which tweets/retweets/likes to keep
master = Tk()

listbox_label = Label(text="Select the twitter activity to KEEP:\n (all unselected tweets, retweets and likes will be deleted)", width=150)
listbox = Listbox(selectmode=EXTENDED, height=30)
button = Button(text="Delete Other Tweets", bg = "#%02x%02x%02x" % (228, 190, 190), command=handle_button_click)

i = 0
for twt in tweet_list:
    i += 1
    type = "tweet"
    if twt["retweet"]:
        type = "retweet"
    if twt["like"]:
        type = "like"

    tweet_list_item = str(twt["tweet_id"]) + " (" + type + "): " + twt["tweet_text"]

    # strip out extra unrecognized characters from tweet - step need for tkinter gui
    char_list = [tweet_list_item[j] for j in range(len(tweet_list_item)) if ord(tweet_list_item[j]) in range(65536)]
    tweet_list_item=""
    for j in char_list:
        tweet_list_item=tweet_list_item+j
    listbox.insert(i, tweet_list_item)

listbox_label.pack()
listbox.pack(side=LEFT, fill=BOTH, expand=1)
button.pack()
master.protocol("WM_DELETE_WINDOW", on_closing)
master.mainloop()
