import eraseme

def test_timeline_retrieve():
    result = len(tweet_list)
    assert result == 1

def test_date(cutoff_date="06/25/2018"):
    result = datetime.strptime(cutoff_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    result = datetime.strptime(cutoff_date, "%Y-%m-%d")
    assert result == datetime.datetime(2018, 6, 25, 0, 0)
