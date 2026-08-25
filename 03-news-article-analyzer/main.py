import spacy
from collections import Counter

# Load Model
nlp = spacy.load("en_core_web_sm")

# User Input
article = input("📰 Paste a news article here: \n\n")

# Process Text
doc = nlp(article)

print("\n" + "_" * 50)
print("📰 News Article Analyzer")
print("_" * 30)

# Name Entities
print("\n📌 Named Entities")
print("_" * 30)

for ent in doc.ents:
    print(f"{ent.text:<25} {ent.label_}")

# Important Words
words = [
    token.text.lower()
    for token in doc
    if token.is_alpha and not token.is_stop
]

counter = Counter(words)

print("\n🔥 TOP KEYWORDS")
print("_" * 30)

for word, count in counter.most_common(5):
    print(f"{word:<25} {count}")

# POS Tag Count

pos_tags = Counter(token.pos_ for token in doc)

print("\n📊 Parts of Speech")
print("_" * 30)

for pos, count in pos_tags.items():
    print(f"{pos:<10} {count}")








