"""
SECTION 1: INTRODUCTION ON TOPIC IDENTIFICATION
"""
# Import the necessary modules
import os
from collections import Counter
from nltk import word_tokenize
from  nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from itertools import chain
from collections import defaultdict
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel


# Get current working directory and import text sources
directory = os.getcwd()

directory += "\\03_Topic_Identification\\article_debugging.txt"

with open(directory, "r",encoding="utf8") as article_file:
    article = article_file.read()


# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [token.lower() for token in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

"""
SECTION 2: LEMMATIZATION
"""

# Define English Stopwords

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
SECTION 3: WORD VECTORIZATION
"""

# The Dictionary function maps each token to an ID
# dictionary.token2id can be used to see the mapping
# In the Corpus each document is transformed in it's BOW representation ( token_id: frequency )

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a Corpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[0][:10])

"""
SECTION 4: MOST FREQUENT WORDS
"""

# Save the first document: doc
doc = corpus[0]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

# Create the defaultdict: total_word_count containing total word count in all corpus

total_word_count = defaultdict(int)
for word_id, word_count in chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True) 

# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)


"""
SECTION 5: TF-IDF
"""
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[corpus[0]]

# Print the first five weights
print(tfidf_weights[:5])