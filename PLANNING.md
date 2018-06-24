# Project Planning

## Problem Statement

### Primary User

Any Twitter account holder that is trying to restart his or her social media presence.

### User Needs Statement 

Some social media platforms such as Twitter have been around for over 12 years.
Users 12 years ago vs. now have very different personalities, behaviors and beliefs.
Posts, comments and other activity that users once did may not be an accurate representation of these users today. 
To help these users recreate their social media presence, there needs to be a quick, easy and central way to get rid of unwanted social media activity. 

### As-is Process Description

  1. Log into twitter.com
  2. Click "Tweets"
  3. For each Tweet:
    + Click on the downward arrow
    + Click on "Delete Tweet"
  4. For each Retweet:
    + Click on the retweet arrows icon
  5. For each Like:
    + Click on the like heart icon

### To-be Process Description
  
  1. Provide credentials for the chosen platforms.
  2. Gather a date input from the user.
  3. Run a script that will gather and categorize activity from prior to the date provided in dictionaries as outlined tweets, retweets and likes.
  4. Present the activity to the user in a pop-up that allows the user to unselect certain activity that he or she would like to keep.
  5. Run a script that will remove all non-selected social media activity.

## Information Requirements

### Information Inputs

  1. Twitter consumer key, consumer secret key, access key and access secret key.
  2. Selection of twitter to perform action on.
  3. Date.
  
### Information Outputs

  1. Tkinter success window with option to output a csv report outlining the actions that the service has just performed.

## Technology Requirements

### APIs and Web Service Requirements

Twitter API.

### Python Package Requirements

`tweepy`, `csv`, `datetime`, `tkinter`, `subprocess`, `os`

### Hardware Requirements

The application will be running on my own local machine. 
I have no plans to deploy this application to a public server (at this time).
