"""
Exercise 1 
"""
import os
import sys

# Get current working directory and import text sources
directory = os.getcwd()

directory += "\\03. Topic Identification\\"

sys.path.append(directory)

from Imports import *


# Import Counter
from collections import Counter
from nltk import word_tokenize

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [token.lower() for token in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

"""
EXERCISE 2

"""

# Import WordNetLemmatizer
from  nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 
english_stops = set(stopwords.words('english'))

# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))

"""
EXERCISE 3: Word Vectorization
"""

#LDA visualization: statistical model for topic modeling

# Passing the Dictionary function: each token mapped to an ID

# dictionary.token2id to see the mapping
 
# Corpus: each document is transformed in it's BOW representation (token_id: frequency)

# Import Dictionary
from gensim.corpora.dictionary import Dictionary

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[0][:10])

"""
EXERCISE 4
"""

# Save the fifth document: doc
doc = corpus[0]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count  OJO
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

# NOW WE DO THE SAME (FIND MOST FREQUENT WORDS) FOR ALL THE CORPUS!
 
# Create the defaultdict: total_word_count containing total word count in all corpus
from itertools import chain
from collections import defaultdict

total_word_count = defaultdict(int)
for word_id, word_count in chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True) 

# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)


"""
EXERCISE 5: TF-IDF
"""
from gensim.models.tfidfmodel import TfidfModel

# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[corpus[0]]

# Print the first five weights
print(tfidf_weights[:5])