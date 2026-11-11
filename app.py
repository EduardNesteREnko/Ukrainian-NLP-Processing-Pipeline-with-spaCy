import spacy

nlp = spacy.load("uk_core_news_sm")
doc = nlp("Супер Український текст.")
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)
