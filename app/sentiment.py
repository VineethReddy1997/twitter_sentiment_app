from transformers import pipeline

# Load a small model ONCE globally
# e.g. distilbert-base-uncased-finetuned-sst-2-english (small, ~250MB)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]["label"]
