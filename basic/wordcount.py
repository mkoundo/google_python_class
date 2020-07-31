#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2# +++your code here+++
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def print_words(filename):
  # f = open(filename, 'rU')
  # alltext_str = f.read()          #read in file content into a string
  # f.seek(0)                       #go back to beginning of file
  # all_words = alltext_str.split()
  
  # alltextstream_str = ""
  # for line in f:
    # alltextstream_str = alltextstream_str + line #read in file content into a string (alternate way)
  # f.seek(0)
  
  # alltext_list = f.readlines()    #read in each line into a list
  # f.close()
  
  # print alltext_str
  # print alltextstream_str
  # print alltext_list
  # print all_words
  
  all_words = word_list(filename)
#  print all_words
  
  word_dict = wordcountdict(all_words)
  
  for key in sorted(word_dict.keys()):  
    print key, word_dict[key]


def print_top(filename):
  all_words = word_list(filename)
  word_dict = wordcountdict(all_words)
  
  count_dict = {}
  for key in sorted(word_dict.keys()):  
    count_dict[word_dict[key]] = key
  
  i=0
  j=0
  for key in sorted(count_dict.keys(), reverse=True): 
    while i < 20 and j == 0:    
      print count_dict[key], key
      j = 1
    i+=1
    j=0
  
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def word_list(filename):
  f = open(filename, 'rU')
  alltext_str = f.read()
  all_words = alltext_str.lower().split() #ensure all words are lower case and split them into a list
  f.close()
  return all_words

def wordcountdict(all_words):
  word_dict = {}
  for word in all_words:
    word_dict[word] = all_words.count(word)
  return word_dict

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
