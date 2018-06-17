# Project Planning

## Problem Statement

### Primary User

Any social media account holder that is trying to restart his or her social media presence.

### User Needs Statement 

Some social media platforms such as Facebook and Twitter have been around for over 14 years.
Users of these platforms have changed significantly over these 14 years. Posts, comments and other activity that users once
conducted may not be an accurate representation of how these users feel and what these users stand for today. 
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
  2. Provide credential for the chosen platforms.
  3. Run a script that will gather and categorize activity as outlined below:
  + Twitter: tweets, retweets, likes.
  + Facebook: posts, likes, tags, other.
  4. Present the activity to the user in pop-up that allows the user to unselect certain activity that he or she would like to keep.
  5. Run a script that will remove all selected media activity.

## Information Requirements

### Information Inputs

  1. A `submissions.csv` file containing a list of student repository submissions, including github usernames and repository URLs.
  2. A `filepaths.csv` file contining a list of files expected to exist in each repository.
  
### Information Outputs

  1. Local copies of all the student repository directories.
  2. A `results.csv` file containing the results of the file-checking process.

## Technology Requirements

### APIs and Web Service Requirements

I thought I might need to use the [GitHub API](https://developer.github.com/v3/) to download all files ina given repository, 
but then I came to the conclusion it would be easier to use command-line Git.

### Python Package Requirements

The application does not require any third-party packages, except `pytest` for testing purposes.

The application does however make extensive use of the `os` and `csv` modules. 
And after performing some Internet research, 
I learned I can use the `subprocess` module to perform system commands like `git clone`.

### Hardware Requirements

The application will be running on my own local machine. I have no plans to deploy this application to a public server.
