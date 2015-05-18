from __future__ import division
import cPickle as pickle
import plotly.plotly as py
from plotly.graph_objs import *

playkeys = ['AllsWellThatEndsWell', 'AntonyAndCleopatra', 'AsYouLikeIt',
            'ComedyOfErrors', 'Coriolanus', 'Cymbeline', 'Hamlet', 'HenryIV',
            'HenryV', 'HenryVIII', 'HenryVIPart1', 'HenryVIPart2', 'HenryVIPart3',
            'JuliusCaesar', 'King John', 'King Lear', 'LovesLaboursLost', 'Macbeth',
            'Measure For Measure', 'MerchantOfVenice', 'MerryWivesOfWindsor',
            'Midsummer Nights Dream', 'Much Ado About Nothing', 'Othello',
            'Pericles', 'Richard II', 'Richard III', 'Romeo and Juliet',
            'Taming Of The Shrew', 'The Tempest',
            'Timon of Athens', 'Titus Andronicus', 'Troilus and Cressida',
            'Twelfth Night', 'Two Gentlemen of Verona', "The Winter's Tale"]

filenames = ['AllsWellThatEndsWell', 'AntonyAndCleopatra', 'AsYouLikeIt',
             'ComedyOfErrors', 'Coriolanus', 'Cymbeline', 'Hamlet', 'HenryIVPart1',
             'HenryV', 'HenryVIII', 'HenryVIPart1', 'HenryVIPart2', 'HenryVIPart3',
             'JuliusCaesar', 'KingJohn', 'KingLear', 'LovesLaboursLost', 'Macbeth',
             'MeasureForMeasure', 'MerchantOfVenice', 'MerryWivesOfWindsor',
             'MidsummerNightsDream', 'MuchAdoAboutNothing', 'Othello', 'Pericles',
             'RichardII', 'RichardIII', 'RomeoAndJuliet', 'TamingOfTheShrew',
             'TheTempest', 'TimonOfAthens', 'TitusAndronicus', 'TroilusAndCressida',
             'TwelfthNight', 'TwoGentlemenofVerona', 'WintersTale']

comedies = ['AllsWellThatEndsWell', 'AsYouLikeIt','ComedyOfErrors', 'Cymbeline',
            'LovesLaboursLost', 'Measure For Measure', 'MerchantOfVenice',
            'MerryWivesOfWindsor', 'Midsummer Nights Dream', 'Much Ado About Nothing',
            'Pericles', 'Taming Of The Shrew', 'The Tempest', 'Troilus and Cressida',
            'Twelfth Night', 'Two Gentlemen of Verona', "The Winter's Tale"]

tragedies = ['AntonyAndCleopatra', 'Coriolanus', 'Hamlet', 'JuliusCaesar', 'King Lear', 'Macbeth',
            'Othello', 'Romeo and Juliet', 'Timon of Athens', 'Titus Andronicus']

histories = ['HenryIV', 'HenryV', 'HenryVIII', 'HenryVIPart1', 'HenryVIPart2', 'HenryVIPart3',
           'King John', 'Richard II', 'Richard III']


allwomen = pickle.load(open('allWomen.pkl', 'r+'))
allmen = pickle.load(open('allMen.pkl', 'r+'))

femalewordsperline = {}
malewordsperline = {}

for i in range(0,len(playkeys)):
    f = open(str(filenames[i]) + '.pkl', 'r+')
    play = pickle.load(f)
    playname = playkeys[i]
    data = play[playname]
    malewords = 0
    femalewords = 0
    malelines = 0
    femalelines = 0
    for j in data:
        if j['text_entry'] not in allwomen[playkeys[i]] and j['text_entry'] not in allmen[playkeys[i]]:
            words = j['text_entry'].split(' ')
            if j['gender'] == 'm':
                malewords += len(words)
                malelines += 1
            elif j['gender'] == 'f':
                femalewords += len(words)
                femalelines += 1
    femalewordsperline[playkeys[i]] = femalewords/femalelines
    malewordsperline[playkeys[i]] = malewords/malelines
    #print str(playkeys[i]) + ' male    ' + str(malewords/malelines)
    #print str(playkeys[i]) + ' female    ' + str(femalewords/femalelines)

totalw = 0
totalm = 0

for i in tragedies:
    totalw += femalewordsperline[i]
    totalm += malewordsperline[i]

avgw = totalw/len(tragedies)
avgm = totalm/len(tragedies)

print avgw
print avgm

y1 = []
y2 = []
for i in histories:
    y1.append(malewordsperline[i])
    y2.append(femalewordsperline[i])

trace1 = Bar(x=histories, y=y1, name='men')
trace2 = Bar(x=histories, y=y2, name='women')

data = Data([trace1, trace2])
layout=Layout(
    barmode='group',
    title="Words Per Line in Shakespeare's Histories")
fig=Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Words Per Line - Histories')
