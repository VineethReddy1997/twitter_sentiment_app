from transformers import pipeline

# Load pre-trained Hugging Face model for Twitter sentiment
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

# Label mapping because cardiffnlp uses numeric labels
label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def analyze_sentiment(text):
    result = sentiment_pipeline(text, truncation=True, max_length=512)[0]
    label = result["label"]
    sentiment = label_mapping.get(label, "Neutral")
    return sentiment
