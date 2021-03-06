
"""
SECTION 1: INTRODUCTION ON NAMED ENTITY RECOGNITION
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import spacy

# Get current working directory and import article sources
directory = os.getcwd()

directory += "\\02_Named_Entity_Recognition\\article_taxi.txt"

with open(directory, "r",encoding="utf8") as article_file:
    article = article_file.read()



# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences,binary = True)

# Binary = True means that any token is either a named entity or not

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)




"""
SECTION 2: IDENTIFY HOW MANY TOKENS PRESENT A NER CATEGORY
"""

# Create the defaultdict: ner_categories
ner_categories = defaultdict(int)


# Create the nested for loop, I increase the count of the laber per each time I encounter that type
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label'):
            ner_categories[chunk.label()] += 1
            
# Create a list from the dictionary keys for the chart labels: labels
labels = list(ner_categories.keys())


# Create a list of the count values for each label: values
values = [ner_categories.get(v) for v in labels]

# Create the pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# Display the chart
plt.show()

"""
SECTION 3: INTRODUCTION TO spaCy
"""

# Instantiate the English model: nlp
nlp = spacy.load('en_core_web_sm')

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)



