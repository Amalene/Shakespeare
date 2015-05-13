from __future__ import division
from collections import namedtuple
import cPickle as pickle
from textblob import TextBlob

play = pickle.load(open('AllsWellThatEndsWell.pkl'))

play['type'] = 'Comedy'
play['women'] = ["countess", "helena", "diana", "mariana"]
play['men'] = ["king", "duke", "bertram", "lafeu", "parolles", "rinaldo", "clown"]

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

femaleSentiment = open('femaleSentiment.pkl', 'w')
maleSentiment = open('maleSentiment.pkl', 'w')
femalePolarity = open('femalePolarity.pkl', 'w')
malePolarity = open('malePolarity.pkl', 'w')

fpol = 0
mpol = 0
fsub = 0
msub = 0


for line in data:
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

