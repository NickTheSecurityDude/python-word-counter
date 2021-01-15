#!/usr/bin/python3

#########################################################################################
#
# Functions:
#   add_to_hash - adds a trio to the hashmap, or increments it if it exists already
#   parse_text - parse the file (or stdin) line by line and builds trios of words
#
# Input:
#   one or more files as arguments, or stdin
#
# Output:
#   top 100 word trios
# 
##########################################################################################

import re,operator,sys,os

def add_to_hash(trio):
  # insert into hash map or increase count
  word_trio=" ".join(trio)
  try:
    word_trios[word_trio]+=1
  except:
    word_trios[word_trio]=1

  return 1

def parse_text(text,type):
  # parse the lines from the file/stdin and build the trios

  # use this so we know when to start trio 2 and 3
  total_words=0

  # indexes for the 3 trios  
  trio1_index=0
  trio2_index=0
  trio3_index=0

  # arrays/lists for the 3 trios
  trio1=[]
  trio2=[]
  trio3=[]

  # check if file or stdin
  if type=="file":
    lines=open(text, "r")
  else:
    lines=text.readlines()

  for line in lines:
    # make line lower case and read words
    for word in line.lower().rstrip('\r\n').split():
      # remove punctuation
      word=re.sub('[.?"{}\[\]\(\),!:;\*]','',word)
      #word=re.sub('[\t]',' ',word)

      # remove start or end single quotes and also -
      word=re.sub('^\'|^-|\'$|-$','',word)      

      # if we stripped the whole word, just continue
      if word == "" or word == "'":
        continue

      #add words to trio arrays
      trio1.append(word)
      if trio1_index==2:
        # add to hash
        add_to_hash(trio1)

        # reset trio
        trio1_index=0
        trio1.clear()
      else:
        trio1_index+=1

      if total_words>0:
        trio2.append(word)
        if trio2_index==2:
          # add to hash
          add_to_hash(trio2)

          trio2_index=0          
          trio2.clear()
        else:
          trio2_index+=1

      if total_words>1:
        trio3.append(word)
        if trio3_index==2:
          # add to hash
          add_to_hash(trio3)
 
          trio3_index=0
          trio3.clear()
        else:
          trio3_index+=1

      total_words+=1 

  return 1

# hash map for trio strings
word_trios={}

if not sys.stdin.isatty():
  # first check if there is stdin
  parse_text(sys.stdin,"stdin")
elif len(sys.argv)>1:
  # if not, check if files
  files=sys.argv[1:]
  for file in files:
    # check if file exists
    if os.path.isfile(file):
      parse_text(file,"file")
    else:
      print("ERROR - File Not Found:",file)
else:
  # otherwise print the usage and exit
  print("ERROR!!!! No data")
  print("Usage:")
  print("./count_words.py file1 file2")
  print("or")
  print("cat file | ./count_words.py")
  sys.exit()

# sort the list
word_trios=dict(sorted(word_trios.items(),key=operator.itemgetter(1),reverse=True))

# get top n trios and print
top_num=100
word_trios={k: word_trios[k] for k in list(word_trios)[:top_num]}
print(word_trios)
