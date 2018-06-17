# Project Planning

## Problem Statement

### Primary User

Any social media account holder that is trying to restart his or her social media presence.

### User Needs Statement 

Some social media platforms such as Facebook and Twitter have been around for over 14 years.
Users 14 years ago vs. now have very different personalities, behaviors, beliefs, etc.
Posts, comments and other activity that users once performed may not be an accurate representation of these users today. 
To help these users recreate their social media presence, there needs to be a quick and easy way to get rid of the social media
activity described above on one platform.

### As-is Process Description

#### Twitter
  1. Log into twitter.com
  2. Click "Tweets"
  3. For each Tweet:
    + Click on the downward arrow
    + Click on "Delete Tweet"
  4. For each Retweet:
    + Click on the retweet arrows icon
  5. For each Like:
    + Click on the like heart icon
    
#### Facebook
  1. Log into facebook.com
  2. Click "Activity Log"
  3. For each Like:
    + Click on the edit pencil icon
    + Click on "Unlike"
  4. For each Post:
    + Click on the edit pencil icon
    + Click on "Delete"
  5. For each Tagged Photo:
    + Click on the edit pencil icon
      + To remove:
        + Click on "Remove Tag/Report"
        + Answer the survey - "Whats going on here?"
        + Click continue
      + To hide:
        + click "Hide from timeline"
   6. For all other activity:
    + Click on the edit pencil icon
    + Click on "Hide from timeline"

### To-be Process Description
  
  1. Select which platforms to remove activity from.
  2. Provide credentials for the chosen platforms.
  3. Gather a date input from the user.
  3. Run a script that will gather and categorize activity from prior to the date provided in dictionaries as outlined below:
  + Twitter: tweets, retweets, likes.
  + Facebook: posts, likes, tags, other.
  4. Present the activity to the user in a pop-up that allows the user to unselect certain activity that he or she would like to keep.
  5. Run a script that will remove all selected social media activity.

## Information Requirements

### Information Inputs

  1. Twitter and Facebook usernames and passwords.
  2. Selection of social media activity to perform action on.
  3. Date.
  
### Information Outputs

  1. None.

## Technology Requirements

### APIs and Web Service Requirements

Twitter API. Facebook Graph API.

### Python Package Requirements

`virtualenv`

### Hardware Requirements

The application will be running on my own local machine. 
I have no plans to deploy this application to a public server (at this time).
