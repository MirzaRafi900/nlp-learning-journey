import spacy

from textblob import TextBlob

text = input("Enter a Review: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

print("\nSentiment Score:", polarity)

if polarity > 0:
    print("😊 Positive Sentiment")

elif polarity < 0:
    print("😣 Negative Sentiment")

else:
    print("😒 Neutral Sentiment")