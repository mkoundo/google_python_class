#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    textfile = open(filename, 'r')
    text = textfile.read()
    text = text.lower()
    textfile.close()
    text_list = []
    text_list = text.split()

    # create a list of a list of words that follow each word
    next_word_list = []
    all_next_words = []
    for nextword in text_list[:-1]:
        i = 0
        next_word_list = []
        for word in text_list:
            if nextword == word:
                next_word_list.append(text_list[i + 1])
            i += 1
        all_next_words.append(next_word_list)

    # create dictionary, key is each word, value is a list of words that follow the key word
    word_dict = {}
    i = 0
    for word in text_list[:-1]:
        if word not in word_dict.keys():
            word_dict[word] = all_next_words[i]
        i += 1
    # add empty string as primer and assume it is followed by the first word
    word_dict[' '] = [text_list[0]]

    return word_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    random_word = str()
    for count in range(200):
        new_word = random.choice(mimic_dict[word])
        random_word = random_word + new_word + ' '
        word = new_word
        if word not in mimic_dict.keys():
            word = ' '

    print(random_word)
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])

    print_mimic(dict, ' ')


if __name__ == '__main__':
    main()
