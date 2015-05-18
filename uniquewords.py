from __future__ import division
import plotly.plotly as py
import cPickle as pickle
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


malewords = {}
femalewords = {}

uniquewordsm = {}
uniquewordsf = {}

allplaysuniquem = {}
allplaysuniquef = {}

mcount = 0
fcount = 0

for i in range(0,len(playkeys)):
    f = open(str(filenames[i]) + '.pkl', 'r+')
    play = pickle.load(f)
    playname = playkeys[i]
    data = play[playname]
    print playname
    for j in data:
        if fcount > 5000 and mcount > 5000:
            break
        text_entry = j['text_entry']
        line = "".join(c for c in text_entry if c not in ('!','.',':',',',';','"'))
        words = line.split(' ')
        for word in words:
            if j['gender'] == 'm':
                mcount += 1
                if word in malewords and mcount < 5000:
                    malewords[word] += 1
                elif mcount < 5000:
                    malewords[word] = 1
                #if word not in allplaysuniquem:
                    #allplaysuniquem[word] = True
            elif j['gender'] == 'f':
                fcount += 1
                if word in femalewords and fcount < 5000:
                    femalewords[word] += 1
                elif fcount < 5000:
                    femalewords[word] = 1
##                if word not in allplaysuniquef:
##                    allplaysuniquef[word] = True
    #uniquewordsm[playname] = malewords
    #uniquewordsf[playname] = femalewords
    #malewords = {}
    #femalewords = {}

#pickle.dump(uniquewordsm, open('uniquewordsm.pkl', 'r+'))
#pickle.dump(uniquewordsf, open('uniquewordsf.pkl', 'r+'))            
            
