from flask import render_template, jsonify, request
from app import app
from app.twitter_client import fetch_tweets
from app.sentiment import analyze_sentiment

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/view")
def view():
    return render_template("tweets.html")

@app.route("/tweets")
def tweets():
    query = request.args.get("query", "Python")
    tweet_texts = fetch_tweets(query, max_results=5)
    
    tweets_with_sentiment = []
    for text in tweet_texts:
        sentiment = analyze_sentiment(text) if not text.startswith("Error") else "Neutral"
        tweets_with_sentiment.append({
            "text": text,
            "sentiment": sentiment
        })
    
    return jsonify(tweets_with_sentiment)
