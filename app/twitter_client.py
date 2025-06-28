import tweepy
import os

# Load environment variable
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Create tweepy client
client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(query, max_results=10):
    try:
        tweets = client.search_recent_tweets(
            query=query,
            max_results=max_results
        )
        if tweets.data:
            return [tweet.text for tweet in tweets.data]
        else:
            return []
    except tweepy.errors.TooManyRequests:
        print("Rate limit hit. Try again later.")
        return ["Rate limit hit. Try again later."]
    except Exception as e:
        print("Error fetching tweets:", e)
        return ["Error fetching tweets."]
