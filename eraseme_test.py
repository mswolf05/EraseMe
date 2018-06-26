import eraseme
from datetime import datetime, timedelta

def test_timeline_retrieve():
    tweet_list = [{"tweet_id": 1011398736696823809, "tweet_text": "Just setting up my Twitter. #myfirstTweet", "tweet_created": "06/26/2018", "retweet": False, "like": False, "tweet_delete": True}]
    result = tweet_list[0]["tweet_id"]
    assert result == 1011398736696823809

def test_date():
    cutoff_date="06/25/2018"

    result = datetime.strptime(cutoff_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    result = datetime.strptime(result, "%Y-%m-%d")
    
    assert result == datetime(2018, 6, 25, 0, 0)

