import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Mock journal data
journal_data = {
    "user_id": "12345",
    "journal_entries": [
        {"date": "2024-11-22", "entry": "I feel really anxious about the upcoming presentation. It's overwhelming."},
        {"date": "2024-11-21", "entry": "Had a great day today! Felt accomplished after finishing all my tasks."}
    ]
}

# Initialize the VADER SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Sentiment analysis function using VADER
def analyze_sentiment(journal_entries):
    insights = []
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for entry in journal_entries:
        sentiment_score = analyzer.polarity_scores(entry["entry"])["compound"]
        # Classify sentiment based on compound score from VADER
        if sentiment_score > 0.05:
            sentiment = "positive"
            positive_count += 1
        elif sentiment_score < -0.05:
            sentiment = "negative"
            negative_count += 1
        else:
            sentiment = "neutral"
            neutral_count += 1

        insights.append({
            "date": entry["date"],
            "entry": entry["entry"],
            "sentiment": sentiment
        })

    total_entries = len(journal_entries)
    summary = {
        "positive": round((positive_count / total_entries) * 100, 2),
        "negative": round((negative_count / total_entries) * 100, 2),
        "neutral": round((neutral_count / total_entries) * 100, 2),
    }

    return insights, summary

# Generate insights
insights, summary = analyze_sentiment(journal_data["journal_entries"])

# Save insights to a file
with open("journaling_insights.json", "w") as f:
    json.dump({"entries": insights, "summary": summary}, f, indent=4)

print("Journaling insights saved to journaling_insights.json")
