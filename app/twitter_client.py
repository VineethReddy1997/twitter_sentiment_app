import os
import tweepy

bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(query, max_results=5):
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
        return ["Rate limit hit. Try again later."]
    except Exception as e:
        return [f"Error fetching tweets: {str(e)}"]
