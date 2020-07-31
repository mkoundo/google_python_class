#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_key(img_url):
  #given a file name like p-biai-bacj.jpg, use the last four letters to sort the list
  match = re.search(r'(\w\w\w\w).jpg', img_url)
  return match.group(1)
  
  
def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  
  # read logfile. Capture and print error message if can't read logfile
  try:  
    logfile = open(filename, 'r')
    logtext = logfile.read() #read all its text
  except:
    print 'Problem reading logfileS:', filename
    sys.exit(1)
  logfile.close()
  
  #search urls containing "puzzle"
  all_img_urls = re.findall(r'GET\s(\S*puzzle\S*)\s', logtext)
  
  servername = re.search(r'\w+_(\S+)', filename).group(1)
  print servername
  
  img_url = []
  unique_url =''
  #remove duplicate urls
  for all_img_url in all_img_urls:
    unique_url = 'http://' + servername + all_img_url
    if unique_url not in img_url:
      img_url.append(unique_url)
  
  result = sorted(img_url, key=sort_key)
  return result

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  #check directory for image download exists; if not, then create it
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  
  #download image file to destination directory
  i = 0
  img_files = []
  img_filenames = []
  for img_url in img_urls:
    imgfilename = 'img' + str(i)
    imgfile = os.path.join(dest_dir, imgfilename)
    img_files.append(imgfile)
    img_filenames.append(imgfilename)
    print 'Retrieving file: ', img_url
    urllib.urlretrieve(img_url, imgfile)
    i += 1

  #create index.html to recombine images
  html = '<verbatim>\n<html>\n<body>\n'
  for imgfilename in img_filenames:
    html = html + '<img src="'+imgfilename+'">'
  html = html + '\n</body>\n</html>\n'
    
  #write html file to index.html in directory todir  
  indexfilename = os.path.join(dest_dir, 'index.html')
  indexfile = open(indexfilename,'w')    
  indexfile.write(html)
  indexfile.close()
  
    
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
