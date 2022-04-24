"""
EXERCISE 1
"""

import re

# Match the first word or digit in a text

re.match("\w+", "this is an example")

re.match("\d", "559302")

# . is a wild card, matches any character or digit
# Adding * or + makes the researc greedy

# The Split function returns a list

re.split("\s", "Split on spaces")

""" Exercise 1: find Pattern so that it returns ['Let', 's', 'write', 'RegEx'] from my_string"""

my_string = "Let's write RegEx!"

PATTERN = "\w+" 

re.findall(PATTERN, my_string)

""" 
EXERCISE 2
"""

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.!?]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result OJO, more than one space!!
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))

# The Search function is to be used when the pattern can be foung in the middle of a word
# Viceversa the Match function is needed

""" 
EXERCISE 3
"""
scene_one = """SCENE 1: [wind] [clop clop clop] 
KING ARTHUR: Whoa there!  [clop clop clop] 
SOLDIER #1: Halt!  Who goes there?
ARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England!
SOLDIER #1: Pull the other one!
ARTHUR: I am, ...  and this is my trusty servant Patsy.  We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.  I must speak with your lord and master.
SOLDIER #1: What?  Ridden on a horse?
ARTHUR: Yes!
SOLDIER #1: You're using coconuts!
ARTHUR: What?
SOLDIER #1: You've got two empty halves of coconut and you're bangin' 'em together.
ARTHUR: So?  We have ridden since the snows of winter covered this land, through the kingdom of Mercea, through--
SOLDIER #1: Where'd you get the coconuts?
ARTHUR: We found them.
SOLDIER #1: Found them?  In Mercea?  The coconut's tropical!
ARTHUR: What do you mean?
SOLDIER #1: Well, this is a temperate zone.
ARTHUR: The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land?
SOLDIER #1: Are you suggesting coconuts migrate?
ARTHUR: Not at all.  They could be carried.
SOLDIER #1: What?  A swallow carrying a coconut?
ARTHUR: It could grip it by the husk!
SOLDIER #1: It's not a question of where he grips it!  It's a simple question of weight ratios!  A five ounce bird could not carry a one pound coconut.
ARTHUR: Well, it doesn't matter.  Will you go and tell your master that Arthur from the Court of Camelot is here.
SOLDIER #1: Listen.  In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?
ARTHUR: Please!
SOLDIER #1: Am I right?
ARTHUR: I'm not interested!
SOLDIER #2: It could be carried by an African swallow!
SOLDIER #1: Oh, yeah, an African swallow maybe, but not a European swallow.  That's my point.
SOLDIER #2: Oh, yeah, I agree with that.
ARTHUR: Will you ask your master if he wants to join my court at Camelot?!
SOLDIER #1: But then of course a-- African swallows are non-migratory.
SOLDIER #2: Oh, yeah...
SOLDIER #1: So they couldn't bring a coconut back anyway...  [clop clop clop] 
SOLDIER #2: Wait a minute!  Supposing two swallows carried it together?
SOLDIER #1: No, they'd have to have it on a line.
SOLDIER #2: Well, simple!  They'd just use a strand of creeper!
SOLDIER #1: What, held under the dorsal guiding feathers?
SOLDIER #2: Well, why not?"""

# Import necessary modules
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)


# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)


# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.+]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w+ ]+:"
print(re.match(pattern2, sentences[3]))
print(re.match(pattern2, "Arthur King : give me"))

"""
EXERCISE 4: CREATE GROUPS () AND CHARACTER CLASSES []
"""
# When you don't want to use . and - with regex meaning use escape character \

# whatever you give in brackets he will accept. Order does not matter

my_string = "match lowercase spaces nums like 12 a, but no commas"

re.match("[a-z 0-9]+", my_string)

#  regexp_tokenize fa parsing in cui TIENE solo le parole che rispettano la regex

"""
EXERCISE 5
"""

my_string = "The player #1 has been selected!"

from nltk.tokenize import regexp_tokenize

# Write a pattern that keeps words, Hashtags+number and punctuation

regexp_tokenize( my_string , r"(\w+|#\d|\?|!)")

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@|#]\w+)"

