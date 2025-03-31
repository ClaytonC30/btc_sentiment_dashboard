import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from fetch_tweets import fetch_tweets
from fetch_reddit import fetch_reddit_posts
from sentiment import analyze_sentiment

# Streamlit App Title
st.title("BTC Trading Sentiment Dashboard 💹")

# Fetch Twitter & Reddit Data
tweets = fetch_tweets("BTC", 200)
reddit_posts = fetch_reddit_posts("cryptocurrency", 100)

# Analyze Sentiment
tweet_sentiment = analyze_sentiment(tweets)
reddit_sentiment = analyze_sentiment(reddit_posts)

# Display Sentiment Metrics
st.metric(label="Twitter Sentiment", value=round(tweet_sentiment, 2))
st.metric(label="Reddit Sentiment", value=round(reddit_sentiment, 2))

# Generate Word Cloud from Combined Data
all_text = " ".join(tweets + reddit_posts)
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(all_text)

# Display Word Cloud
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
