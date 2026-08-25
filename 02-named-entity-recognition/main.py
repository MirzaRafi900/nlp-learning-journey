import spacy

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

text = """
Microsoft announced a new AI initiative...
"""

article = input("Paste an Article: ")

doc = nlp(article)

print("\nNamed Entities")
print("_" * 30)

for ent in doc.ents:
    print(f"🔹 Text: {ent.text}")
    print(f"🏷️ Text: {ent.label_}")
    print("_" * 30)