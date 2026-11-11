# Ukrainian NLP Processing Pipeline with spaCy

This repository contains a Python script demonstrating natural language processing (NLP) tokenization, Part-of-Speech (POS) tagging, and dependency parsing for the Ukrainian language using the `spacy` library and the `uk_core_news_sm` model pipeline.

## 📋 Overview of the Pipeline

1. **Model Loading**:
   * Loads the small Ukrainian pipeline (`uk_core_news_sm`) via spaCy for linguistic analysis.
2. **Text Processing**:
   * Processes a sample Ukrainian sentence through the NLP pipeline (`nlp`).
3. **Token Analysis**:
   * Iterates through each token to extract its surface text, syntactic Part-of-Speech tag (`POS`), and syntactic dependency relation (`dep_`).

## 🛠️ Code Implementation

```python
import spacy

# Load the Ukrainian spaCy language model
nlp = spacy.load("uk_core_news_sm")

# Process sample text
doc = nlp("Супер Український текст.")
print(doc.text)

# Iterate through tokens and print linguistic attributes
for token in doc:
    print(token.text, token.pos_, token.dep_)
```

## 🚀 Key Features

* **Multilingual NLP Support**: Demonstrates how to leverage spaCy's pre-trained pipelines for Slavic and specifically Ukrainian linguistic tasks.
* **Linguistic Feature Extraction**: Inspects part-of-speech categories and dependency structures essential for advanced text analysis and syntax parsing.