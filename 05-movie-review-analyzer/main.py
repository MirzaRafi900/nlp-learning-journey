import spacy

from textblob import TextBlob

reviews = [
    "The Movie was amazing",
    "I love the acting",
    "The movie was okay",
    "The Story was boring",
    "Excellent Visual Effects."
]

positive = 0
negative = 0
neutral = 0

for review in reviews:

    analysis = TextBlob(review)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        positive += 1
    elif polarity < 0:
        negative += 1
    else:
        neutral += 1

print("\nRESULTS")
print("_", 30)
print("Positive Reviews: ", positive)
print("Negative Reviews: ", negative)
print("Neutral Reviews: ", neutral)