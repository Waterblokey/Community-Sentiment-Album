import os
import praw
import pandas as pd
import numpy as np
import re #RegEx : Regular expression


reddit = praw.Reddit(
 client_id=os.environ.get("REDDIT_CLIENT_ID"),
 client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
 user_agent=os.environ.get("REDDIT_USER_AGENT"),
)

# Hot new rising topics
headlines = set()
for submission in reddit.subreddit("hiphopheads").hot(limit=None):
    print(submission.title)#Subreddit Title
    print(submission.id) #ID
    print(submission.author) #Author of the subreddit
    print(submission.created_utc) #Date and time being created
    print(submission.score) # Average Score
    print(submission.upvote_ratio) # Upvote ratio
    print(submission.url) # Like to the Subreddit
    break
    headlines.add(submission.title)
print(len(headlines))
