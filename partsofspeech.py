from __future__ import division
import plotly.plotly as py
import cPickle as pickle
from plotly.graph_objs import *
from textblob import TextBlob

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

fm = open('malepos.pkl', 'w')
ff = open('femalepos.pkl', 'w')

allmpos = {}
allfpos = {}

mpos = {}
fpos = {}

for i in range(0,len(playkeys)):
    f = open(str(filenames[i]) + '.pkl', 'r+')
    play = pickle.load(f)
    playname = playkeys[i]
    data = play[playname]
    print playname
    for j in data:
        blob = Textblob(j['text_entry'])
        for tag in blob.tags:
            if j['gender'] == 'm':
                if tag[1] in mpos:
                    mpos[tag[1]] += 1
                else:
                    mpos[tag[1]] = 1
            elif j['gender'] == 'f':
                if tag[1] in fpos:
                    mpos[tag[1]] += 1
                else:
                    fpos[tag[1]] = 1
    allmpos[playname] = mpos
    allfpos[playname] = fpos
    mpos = {}
    fpos = {}


        
pickle.dump(allmpos, open('malepos.pkl', 'r+'))
pickle.dump(allfpos, open('femalepos.pkl', 'r+'))            
            
