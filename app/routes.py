from flask import Blueprint, jsonify, render_template
from app.twitter_client import fetch_tweets
from app.sentiment import analyze_sentiment

main = Blueprint('main', __name__)

cached_tweets = None

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/tweets')
def tweets():
    global cached_tweets

    if cached_tweets:
        tweet_texts = cached_tweets
    else:
        query = "the lang:en"
        tweet_texts = fetch_tweets(query)
        cached_tweets = tweet_texts

    result = []
    for text in tweet_texts:
        sentiment = analyze_sentiment(text)
        result.append({
            "text": text,
            "sentiment": sentiment
        })

    return jsonify(result)

@main.route('/view')
def view_tweets():
    return render_template('tweets.html')
