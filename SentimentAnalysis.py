from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (only needed once)
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(texts):
    """Analyzes sentiment of a list of texts and returns an average score."""
    scores = [sia.polarity_scores(text)['compound'] for text in texts]
    avg_score = sum(scores) / len(scores) if scores else 0
    return avg_score
