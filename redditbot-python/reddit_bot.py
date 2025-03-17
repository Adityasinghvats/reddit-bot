import praw
import os
from dotenv import load_dotenv
from prawcore.exceptions import PrawcoreException

load_dotenv()

required_vars = ["REDDIT_USERNAME", "REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_PASSWORD"]

# Verify all required environment variables are set
missing_vars = [var for var in required_vars if not os.environ.get(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    exit(1)

username = os.environ.get("REDDIT_USERNAME")
client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
password = os.environ.get("REDDIT_PASSWORD")

try:
    reddit_instance = praw.Reddit(
        client_id=client_id.strip(),
        client_secret=client_secret.strip(),
        password=password.strip(),
        user_agent="windows:mybot:v1.0 (by /u/Confident-Wave-4618)",
        username=username.strip()
    )
    
    me = reddit_instance.user.me()
    print(f"Successfully logged in as: {me}")

except PrawcoreException as e:
    print(f"Reddit API Error: {e}")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

# get posts
# subreddit = reddit_instance.subreddit("cats")
# top_25 = subreddit.hot(limit=25)
# for sub in top_25:
#     print(sub.title)

# send post
# subreddit = reddit_instance.subreddit("testingground4bots")
# subreddit.submit(title="this is like anyother testpost", selftext="Hi fellow developers")

# get comments
submission = reddit_instance.submission("1j64bt6")
print(len(submission.comments))
comments = submission.comments
for comment in comments:
    if "arms" in comment.body:
        print(comment.body)
# comment
# for comment in comments:
#     if "arms" in comment.body:
#         comment.reply("You are right!")