import tweepy
import os
from dotenv import load_dotenv
import pdb
import csv
from tkinter import *
from datetime import datetime, timedelta
from subprocess import Popen
import pytest

consumer_key = input("Consumer Key (API Key): ")
consumer_secret = input("Consumer Secret (API Secret): ")
access_token = input("Acess Token: ")
access_token_secret = input("Acess Token Secret: ")

def handle_button_click():
    item_id_keep = []
    for index in listbox.curselection():
        item = listbox.get(index)
        find_id = item.find(" (")
        item_id = item[:find_id]
        item_id_keep.append(str(item_id))

    # delete unselected twitter activity
    for dt in tweet_list:

        ids_deleted = []
        if str(dt["tweet_id"]) not in item_id_keep:
            api.destroy_status(dt["tweet_id"])
            ids_deleted.append(str(dt["tweet_id"]))

# log and report activity
    csv_file_path = "eraseme_activity_report.csv"

    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["tweet_id", "tweet_text", "activity_type", "date_created", "action"])
        writer.writeheader()

        for t in tweet_list:
            type = "tweet"
            if t["retweet"]:
                type = "retweet"
            if t["like"]:
                type = "like"

            if str(t["tweet_id"]) in item_id_keep:
                em_action = "KEPT"
            else:
                em_action = "DELETED"

            writer.writerow({"tweet_id": t["tweet_id"], "tweet_text": t["tweet_text"].encode("utf-8"), "activity_type": type, "date_created": t["tweet_created"], "action": em_action})

    #master.destroy()
    button.destroy()
    listbox.destroy()
    listbox_label.destroy()

    my_message = Message(text="SUCCESS! Your tweets have been deleted from your timeline.\nIf you would like to see the report, click 'Open Report' to the right.\nOtherwise, in keeping with the EraseMe company values, the report and all of your history will be removed from the EraseMe application.", width=1000)
    button2 = Button(text="Open Report", bg = "#%02x%02x%02x" % (112, 173, 71), command=handle_button2_click)
    my_message.pack(side=LEFT, fill=BOTH, expand=1)
    button2.pack()

def handle_button2_click():
    p = Popen("eraseme_activity_report.csv", shell=True)
    master.destroy()    

def on_closing():
    filename = "eraseme_activity_report.csv"
    if os.path.exists(filename):
        os.remove(filename)
        print("All twitter activity reports removed from the EraseMe application.")
    master.destroy()    
    
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

print("Thank you for using the EraseMe service!")
