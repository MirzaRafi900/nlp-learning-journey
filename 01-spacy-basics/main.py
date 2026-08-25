import spacy

nlp = spacy.load("en_core_web_sm")

text = """
        Microsoft is  investing havily in artificial intelligence
        """
doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_)