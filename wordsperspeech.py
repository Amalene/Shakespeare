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

malesentences={}
femalesentences={}
currentmalelist = []
currentfemalelist = []
wordcount = 0
lastspeech = 0
lastgender = ''

avgmale = {}
avgfemale = {}
count = 0

for i in range(0,len(playkeys)):
    f = open(str(filenames[i]) + '.pkl', 'r+')
    play = pickle.load(f)
    playname = playkeys[i]
    data = play[playname]
    #print data[1:10]
    for j in data:
        count+=1
        sentences = j['text_entry'].split('.')
        if j['speech_number'] != lastspeech:
            if lastgender == 'f':
                currentfemalelist.append(wordcount)
            elif lastgender == 'm':
                currentmalelist.append(wordcount)
            wordcount = 0
        wordcount += len(j['text_entry'].split(' '))
        lastgender = j['gender']
        lastspeech = j['speech_number']
    malesentences[playname] = currentmalelist
    femalesentences[playname] = currentfemalelist
    currentmalelist = []
    currentfemalelist = []
    wordcount = 0
    lastspeech = 0



totalm = 0
totalf = 0

for j in playkeys:
    for i in malesentences[j]:
        totalm += i
    for i in femalesentences[j]:
        totalf += i
    avgmale[j] = (totalm/len(malesentences[j]))
    avgfemale[j] = (totalf/len(femalesentences[j]))
    totalm = 0
    totalf = 0
    
print avgmale


y1 = []
y2 = []
x1 = tragedies
for i in x1:
    y1.append(avgmale[i])
    y2.append(avgfemale[i])

trace1 = Bar(x=x1, y=y1, name='men')
trace2 = Bar(x=x1, y=y2, name='women')

data = Data([trace1, trace2])
layout=Layout(
    barmode='group',
    title="Words per Speech in Tragedies")
fig=Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Words per Speech - Tragedies')
