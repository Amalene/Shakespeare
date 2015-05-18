from __future__ import division
from collections import namedtuple
import cPickle as pickle
from textblob import TextBlob

f = open('TitusAndronicus.pkl', 'r+')
play = pickle.load(f)

playName = "Titus Andronicus"

allwomen = pickle.load(open('allWomen.pkl', 'r+'))
allmen = pickle.load(open('allMen.pkl', 'r+'))

#print allwomen.keys()

play['type'] = 'History'
play['women'] = allwomen[playName]
play['men'] = allmen[playName]

women = play['women']
men = play['men']

data = play[playName]

femaleLines = 0
maleLines = 0
SD = 0
unknownLines = 0


femaleSubjectivity = open('femaleSubjectivity.pkl', 'r+')
maleSubjectivity = open('maleSubjectivity.pkl', 'r+')
femalePolarity = open('femalePolarity.pkl', 'r+')
malePolarity = open('malePolarity.pkl', 'r+')
netFemalePol = open('netFemalePol.pkl', 'r+')
netMalePol = open('netMalePol.pkl', 'r+')

fs = pickle.load(femaleSubjectivity)
ms = pickle.load(maleSubjectivity)
fp = pickle.load(femalePolarity)
mp = pickle.load(malePolarity)
fa = pickle.load(netFemalePol)
ma = pickle.load(netMalePol)

fpol = 0
mpol = 0
fabs = 0
mabs = 0
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
            fpol += abs(sentiment.polarity)
            fabs += sentiment.polarity
        elif line['speaker'].lower() in men:
            maleLines += 1
            line['gender'] = 'm'
            msub += sentiment.subjectivity
            mpol += abs(sentiment.polarity)
            mabs += sentiment.polarity
        elif line['speaker'].lower() == "stage directions":
            SD += 1
            line['gender'] = 'sd'
        else:
            unknownLines += 1
            line['gender'] = 'u'


print play.keys()

print femaleLines
print maleLines
print SD
print unknownLines

averagemalesubj = msub/maleLines
averagemalepol = mpol/maleLines
averagefemalesubj = fsub/femaleLines
averagefemalepol = fpol/femaleLines
averagenetfemalepol = fabs/femaleLines
averagenetmalepol = mabs/maleLines

fs[playName] = averagefemalesubj
fp[playName] = averagefemalepol
ms[playName] = averagemalesubj
mp[playName] = averagemalepol
fa[playName] = averagenetfemalepol
ma[playName] = averagenetmalepol

print str(fs.keys()) + "      these are keys"


femaleSubjectivity.seek(0)
femalePolarity.seek(0)
maleSubjectivity.seek(0)
malePolarity.seek(0)
netFemalePol.seek(0)
netMalePol.seek(0)
f.seek(0)

pickle.dump(fs, femaleSubjectivity)
pickle.dump(fp, femalePolarity)
pickle.dump(ms, maleSubjectivity)
pickle.dump(mp, malePolarity)
pickle.dump(fa, netFemalePol)
pickle.dump(ma, netMalePol)
pickle.dump(play, f)

print "female subjectivity: " + str(averagefemalesubj)
print "male subjectivity: " + str(averagemalesubj)           
print "female polarity: " + str(averagefemalepol)
print "male polarity: " + str(averagemalepol)
print "netfemale polarity: " + str(averagenetfemalepol)
print "netmale polarity: " + str(averagenetmalepol)
