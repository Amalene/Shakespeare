import cPickle as pickle
import json
import os
from textblob import TextBlob
from collections import namedtuple


Line = namedtuple('Line', 'line_number speech_number play_name text_entry line_id speaker')
x = pickle.load(open("TheWintersTale.p", 'rb'))

meow = ""

#print len(x)

for i in x:
    if i.speaker != '"Stage Directions"':
        meow += i.text_entry + " "


#f = open("WintersTale.txt", "w+")
#f.write(meow)

#print f.readline()
#print os.stat('WintersTale.txt').st_size

blobby = TextBlob(meow);
blobby1 = blobby[0:1000]
