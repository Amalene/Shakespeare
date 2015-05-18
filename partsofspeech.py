from __future__ import division
import plotly.plotly as py
import cPickle as pickle
from plotly.graph_objs import *
from textblob import TextBlob
import operator

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

fm = pickle.load(open('malepos.pkl', 'r+'))
ff = pickle.load(open('femalepos.pkl', 'r+'))

##allmpos = {}
##allfpos = {}
##
##mpos = {}
##fpos = {}
##
##count = 0
##
##for i in range(0,len(playkeys)):
##    f = open(str(filenames[i]) + '.pkl', 'r+')
##    play = pickle.load(f)
##    playname = playkeys[i]
##    data = play[playname]
##    print playname
##    for j in data:
##        blob = TextBlob(j['text_entry'])
##        for tag in blob.tags:
##            if count < 10:
##                print tag[1]
##                count += 1
##            if j['gender'] == 'm':
##                if tag[1] == '\n':
##                    print tag
##                    print tag[1]
##                if tag[1] in mpos:
##                    mpos[tag[1]] += 1
##                else:
##                    mpos[tag[1]] = 1
##            elif j['gender'] == 'f':
##                if tag[1] in fpos:
##                    fpos[tag[1]] += 1
##                else:
##                    fpos[tag[1]] = 1
##    allmpos[playname] = mpos
##    allfpos[playname] = fpos
##    mpos = {}
##    fpos = {}
##
##fm.seek(0)
##ff.seek(0)
##        
##pickle.dump(allmpos, fm)
##pickle.dump(allfpos, ff)            

totalm = {}
totalf = {}
comedym = {}
comedyf = {}
tragedym = {}
tragedyf = {}
historym = {}
historyf = {}
wordsm = 0
wordsf = 0

count = 0
            
for play in fm:
    print play
    for key in fm[play]:
        wordsm += fm[play][key]
        if count < 10:
            count+= 1
        if key in totalm:
            totalm[key] += fm[play][key]
        else:
            totalm[key] = fm[play][key]
        if play in comedies:
            if key in comedym:
                comedym[key] += fm[play][key]
            else:
                comedym[key] = fm[play][key]
        elif play in tragedies:
            if key in tragedym:
                tragedym[key] += fm[play][key]
            else:
                tragedym[key] = fm[play][key]
        elif play in histories:
            if key in historym:
                historym[key] += fm[play][key]
            else:
                historym[key] = fm[play][key]
        
for play in ff:
    for key in ff[play]:
        wordsf += ff[play][key]
        if key in totalf:
            totalf[key] += ff[play][key]
        else:
            totalf[key] = ff[play][key]
        if play in comedies:
            if key in comedyf:
                comedyf[key] += ff[play][key]
            else:
                comedyf[key] = ff[play][key]
        elif play in tragedies:
            if key in tragedyf:
                tragedyf[key] += ff[play][key]
            else:
                tragedyf[key] = ff[play][key]
        elif play in histories:
            if key in historyf:
                historyf[key] += ff[play][key]
            else:
                historyf[key] = ff[play][key]
            
sorted_m = sorted(totalm.items(), key=operator.itemgetter(1))
sorted_f = sorted(totalf.items(), key=operator.itemgetter(1))
