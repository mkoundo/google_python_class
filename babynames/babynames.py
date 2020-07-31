#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename, summary):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  htmlfile = open(filename, 'r')  #open html file for reading
  alltext = htmlfile.read()       #read entire file into a string
  htmlfile.close()
#  print alltext
  
  #create file name for writing and call it <filename>--summary.txt
  if summary:
    summary_name = re.search(r'\w+',filename)
    summary_filename = summary_name.group() + '-summary.txt'
  
    txtoutput = open(summary_filename, 'w')
  
  year = re.search(r'Popularity in (\d\d\d\d)',alltext) #extract year
  
  if summary:
    txtoutput.write(str(year.group(1) + '\n'))
  else:
    print year.group(1)
  
  # copy each rank, boy's name and girl's name into a list of tuples size 3
  rank_bname_gname = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', alltext)
#  print rank_bname_gname
  
  #create dict with boy's name/rank
  name_rank = {}
  for tuple_item in rank_bname_gname:
    name_rank[tuple_item[1]] = tuple_item[0]       #add to dict: tuple_item[1] (boy's name) key, tuple_item[0] (rank) value
  
  # add girl's names/rank to dict
  for tuple_item in rank_bname_gname: 
    if not tuple_item[2] in name_rank.keys():     #check if girl's name is already in dict
      name_rank[tuple_item[2]] = tuple_item[0]    #add to dict: tuple_item[2] (girl's name) key, tuple_item[0] (rank) value
    elif int(name_rank[tuple_item[2]]) > int(tuple_item[0]): #if girl's name already exist, then retain highest rank
      name_rank[tuple_item[2]] = tuple_item[0]
      
  for key in sorted(name_rank.keys()):
    if summary:
      line = str(key + " " + name_rank[key] + '\n')
      txtoutput.write(line)
    else:
      print key, name_rank[key]
    
  if summary:  
    txtoutput.close()
  
  return


def main():
  # # This command-line parsing code is provided.
  # # Make a list of command line arguments, omitting the [0] element
  # # which is the script itself.
  args = sys.argv[1:]

  if not args: # if no argument is given then print error
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  
  # # For each filename, get the names, then either print the text output
  # # or write it to a summary file

  for filename in args:
    extract_names(filename, summary) 
  
if __name__ == '__main__':
  main()
