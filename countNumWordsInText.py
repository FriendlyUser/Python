# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:09:52 2017

@author: wu
"""

# Count the characters in text file
# Count the lines in text file
# Call split with no arguments
# Assume user has downloaded stopwords from NLTK

# Program assumes user has downloaded an imported stopwords from NLTK
from nltk.corpus import stopwords # Import the stop word list
from nltk.tokenize import wordpunct_tokenize

from collections import Counter

# Number of words to be outputted
NUM_WORDS = 50
# Program will display a welcome message to the user
print("Welcome! This program will analyze your file to provide a word count, the top 30 words and remove the following stopwords.")

# Open the input file
try:
    with open('README.Md') as open_file:
        contents = open_file.read()
except IOError:
    print("Could not read from file")
    exit(1) # Non-zero means failure

# Program will count the characters in text file
num_chars = len(contents)

# Program will count the lines in the text file
num_lines = contents.count('\n')

# Program will call split with no arguments
words = contents.split()
word_counts = Counter(words)

num_words = sum(word_counts.values())

lst = [(value, key) for key, value in word_counts.items()]
lst.sort(reverse=True)

stop_words = set(stopwords.words('english')) # creating a set makes the searching faster
print ([word for word in lst if word not in stop_words])

# Program will print the results
print('Your input file has characters = '+str(num_chars))
print('Your input file has lines = '+str(num_lines))
print('Your input file has the following words = '+str(num_words))

print('\n The 50 most frequent words are \n')

for i, (count, word) in enumerate(lst[:NUM_WORDS], 1):
    print('{:>2}. {:>4} {}'.format(i, count, word))

print('Thank You! Goodbye.')