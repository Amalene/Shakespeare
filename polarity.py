from __future__ import division
from collections import namedtuple
import cPickle as pickle
from textblob import TextBlob

f = open('AllsWellThatEndsWell.pkl', 'r+')
play = pickle.load(open('AllsWellThatEndsWell.pkl'))

#play['type'] = 'Comedy'
#play['women'] = ['aemilia', 'adriana', 'luciana']
#play['men'] = ['solinus', 'aegeon', 'of ephesus', 'of syracuse', 'dromio of ephesus',
#               'balthasar', 'angelo', 'pinch']

play['type'] = 'Comedy'
play['women'] = ["countess", "helena", "diana", "mariana"]
play['men'] = ["king", "duke", "bertram", "lafeu", "parolles", "rinaldo", "clown"]

play['type'] = 'Comedy'

women = play['women']
men = play['men']

data = play['AllsWellThatEndsWell']

count = 0
femaleLines = 0
maleLines = 0
SD = 0
unknownLines = 0

fs = {}
ms = {}
fp = {}
mp = {}

femaleSubjectivity = open('femaleSubjectivity.pkl', 'r+')
maleSubjectivity = open('maleSubjectivity.pkl', 'r+')
femalePolarity = open('femalePolarity.pkl', 'r+')
malePolarity = open('malePolarity.pkl', 'r+')

fpol = 0
mpol = 0
fsub = 0
msub = 0


for line in data:
    if line['text_entry'] in women or line['text_entry'] in men:
        pass
    else:
        blob = TextBlob(line['text_entry'])
        sentiment = blob.sentiment
        line['subjectivity'] = sentiment.subjectivity
        line['polarity'] = sentiment.polarity
        if line['speaker'].lower() in women:
            femaleLines += 1
            line['gender'] = 'f'
            fsub += sentiment.subjectivity
            fpol += sentiment.polarity
        elif line['speaker'].lower() in men:
            maleLines += 1
            line['gender'] = 'm'
            msub += sentiment.subjectivity
            mpol += sentiment.polarity
        elif line['speaker'].lower() == "stage directions":
            SD += 1
            line['gender'] = 'sd'
        else:
            unknownLines += 1
            line['gender'] = 'u'

            
        if count < 10:
            print line['polarity']
            print sentiment.subjectivity
        count += 1

print play.keys()

print femaleLines
print maleLines
print SD
print unknownLines

averagemalesubj = msub/maleLines
averagemalepol = mpol/maleLines
averagefemalesubj = fsub/femaleLines
averagefemalepol = fpol/femaleLines

fs['Alls Well That Ends Well'] = averagefemalesubj
fp['Alls Well That Ends Well'] = averagefemalepol
ms['Alls Well That Ends Well'] = averagemalesubj
mp['Alls Well That Ends WEll'] = averagemalepol

print fs.keys()

pickle.dump(fs, femaleSubjectivity)
pickle.dump(fp, femalePolarity)
pickle.dump(ms, maleSubjectivity)
pickle.dump(mp, malePolarity)
pickle.dump(play, f)

print "female subjectivity: " + str(averagefemalesubj)
print "male subjectivity: " + str(averagemalesubj)           
print "female polarity: " + str(averagefemalepol)
print "male polarity: " + str(averagemalepol)
