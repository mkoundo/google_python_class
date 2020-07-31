#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
#function to list absolute paths of all files with name 
#containing pattern __\w+__ in directory <dirname>

def get_special_paths(dirname):
  filenames = os.listdir(dirname)
  specialpaths = {}
  for filename in filenames:
    if re.search(r'__\w+__', filename):
    #print filename ##foo.txt
    #print os.path.join(dirname, filename) ##dir/foo.txt (relative to current dir
      specialpaths[filename] =  os.path.abspath(os.path.join(dirname, filename)) ##abs paths to files
  return specialpaths

#given input option --todir, copy files to given directory
def copy_to(paths, todir):
  dir_exists(os.path.abspath(todir))
  
  for path in paths:
    shutil.copy(path, todir_path)

#given input option --tozip, zip files to given zipfile    
def zip_to(paths, zippathfile):
  zippath = os.path.abspath(os.path.dirname(zippathfile)) #strip out filename and determine abs path
#  dir_exists(zippath)
  
  for path in paths:
    cmd = 'zip -j ' + zippathfile + ' ' + path
    print 'About to run:', cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status: #Error case, print command's output to stderr and exit
      sys.stderr.write(output)
      sys.exit(status)
    print output 

# utility to check if directory exists; if it doesn't, then create it
def dir_exists(path):
  if not os.path.exists(path):
    os.makedirs(path)

# Write functions and modify main() to call them

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  all_special_paths = {}
  for dirs in args:
    special_paths = get_special_paths(dirs)
    for filename in special_paths.keys():
      if filename not in all_special_paths.keys():
        all_special_paths[filename] = special_paths[filename]
      else:
        print 'duplicate file found!'
        sys.exit(1)
  
  if not todir == '':
    copy_to(all_special_paths.values(), todir)
  elif not tozip == '':
    zip_to(all_special_paths.values(), tozip)
  else:
    for path in sorted(all_special_paths.values()):
      print path
    
    
if __name__ == "__main__":
  main()
