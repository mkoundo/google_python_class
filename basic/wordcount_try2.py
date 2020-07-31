import sys

def print_words(filename):
  '''function that counts how often each word appears in the text and prints: word1 count1 etc.'''  
  word_dict = word_list(filename)
  
  for word in sorted(word_dict.keys()):  
    print word, word_dict[word]
#=======================

def print_top(filename):
  '''function that list top 20 occuring words in textfile'''
  word_dict = word_list(filename)
  
  items = sorted(word_dict.items(), key=count_tuple, reverse=True)  #copy dict word/count pairs into a list of tuples
                                                                    #sort by second entry (i.e. word count) in tuple using a function
                                                                    #reverse sort order so the highest word count is listed first
  #print top 20 word/count pairs:
  for item in items[:20]:
    print item[0], item[1]
  
#<---------------------------------UTILITIES--------------------------------------------------------->
  
def word_list(filename):
  # utility to read in filename and split the words into a list
  textfile = open(filename, 'r')
  word_dict = {}
  for line in textfile:
    all_words = line.split()  #read each line of filename and split out the words into a list
    
    for word in all_words:
      word = word.lower()     #ensure all words are lowercase
      if not word in word_dict:  #insert each word into a dict and count the number of occurence in the dict
        word_dict[word] = 1
      else:
        word_dict[word] = word_dict[word] + 1
  
  textfile.close()  #close text file
  return word_dict

def count_tuple(tuple_item):
  '''with a list [(word1, count1), (word2, count2), ...], this function extracts the count from each tuple'''
  return tuple_item[1]

#----------------------------------------------------------------------------------------------------
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
