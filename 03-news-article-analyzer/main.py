import spacy
from collections import Counter

# Import Library
nlp = spacy.load("en_core_web_sm")

# Input Article
article = input("\n📰 Paste the Article Here:\n\n")

# Process Text
doc = nlp(article)

print("\n" + "=" * 50)
print("📰 News Article Analyzer")
print("_" * 50)

# Named Entities
print("\n📌 Named Entities")
print("_" * 30)

for ent in doc.ents:
    print(f"{ent.text:<25} {ent.label_}")

# Important Word
word=[
    token.text.lower()
    for token in doc
    if token.is_alpha and not token.is_stop
]

counter = Counter(word)

print("\n🔥 Top Keywords")
print("_" * 30)

for word, count in counter.most_common(5):
    print(f"{word:<15} {count}")

# POS Tag Count
pos_tags = Counter(token.pos_ for token in doc)

print("\n📊 Parts of Speech")
print("_" * 30)

for pos, count in pos_tags.items():
    print(f"{pos:<10} {count}")






