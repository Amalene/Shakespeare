from __future__ import division
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

comedies = ['AllsWellThatEndsWell', 'AsYouLikeIt','ComedyOfErrors', 'Cymbeline',
            'LovesLaboursLost', 'Measure For Measure', 'MerchantOfVenice',
            'MerryWivesOfWindsor', 'Midsummer Nights Dream', 'Much Ado About Nothing',
            'Pericles', 'Taming Of The Shrew', 'The Tempest', 'Troilus and Cressida',
            'Twelfth Night', 'Two Gentlemen of Verona', "The Winter's Tale"]

tragedies = ['AntonyAndCleopatra', 'Coriolanus', 'Hamlet', 'JuliusCaesar', 'King Lear', 'Macbeth',
            'Othello', 'Romeo and Juliet', 'Timon of Athens', 'Titus Andronicus']

histories = ['HenryIV', 'HenryV', 'HenryVIII', 'HenryVIPart1', 'HenryVIPart2', 'HenryVIPart3',
           'King John', 'Richard II', 'Richard III']

malelines = {'AllsWellThatEndsWell':2008, 'AsYouLikeIt': 1830,
             'AntonyAndCleopatra': 2214,
             'ComedyOfErrors': 1345, 'King Lear': 2726,
             'MerchantOfVenice': 1911, 'Timon of Athens': 2390,
             'AsYouLikeIt': 1827, 'Romeo and Juliet': 2024,
             'Much Ado About Nothing': 2131, 'The Tempest': 1870,
             'HenryVIII': 2297, "The Winter's Tale": 2344,
             'Taming Of The Shrew': 2351, 'JuliusCaesar': 2340,
             'Coriolanus': 3054, 'Richard II': 2489, 'Cymbeline': 2562,
             'HenryV': 3030, 'Twelfth Night': 1925, 'HenryIV': 3085,
             'Othello': 2656, 'King John': 2300, 'HenryVIPart2': 2725,
             'HenryVIPart3': 2809, 'HenryVIPart1': 2344,
             'Titus Andronicus': 2183, 'LovesLaboursLost': 2232,
             'Midsummer Nights Dream': 1550, 'MerryWivesOfWindsor': 2277,
             'Measure For Measure': 2302, 'Pericles': 1973,
             'AllsWellThatEndsWell': 1918, 'Macbeth': 1548,
             'Hamlet': 3509, 'Two Gentlemen of Verona': 1752,
             'AntonyAndCleopatra': 2214, 'Troilus and Cressida': 3134,
             'Richard III': 2797}

femalelines = {'AllsWellThatEndsWell': 977, 'AsYouLikeIt': 1057,
               'AntonyAndCleopatra':854,
               'ComedyOfErrors': 442, 'King Lear': 490,
               'MerchantOfVenice': 758, 'Timon of Athens': 10,
               'AsYouLikeIt': 1057, 'Romeo and Juliet': 937,
               'Much Ado About Nothing': 512, 'The Tempest': 215,
               'HenryVIII': 523, "The Winter's Tale": 735,
               'Taming Of The Shrew': 305, 'JuliusCaesar': 119,
               'Coriolanus': 363, 'Richard II': 267, 'Cymbeline': 788,
               'HenryV': 150, 'Twelfth Night': 786, 'HenryIV': 106,
               'Othello': 667, 'King John': 376,
               'AllsWellThatEndsWEll': 977, 'HenryVIPart2': 440,
               'HenryVIPart3': 364, 'HenryVIPart1': 333,
               'Titus Andronicus': 339, 'LovesLaboursLost': 568,
               'Midsummer Nights Dream': 569, 'MerryWivesOfWindsor': 762,
               'Two Gentlement of Verona': 550, 'Measure For Measure': 536,
               'Pericles': 481, 'Macbeth': 534, 'Hamlet': 325,
               'Two Gentlemen of Verona': 550, 'AntonyAndCleopatra': 854,
               'Troilus and Cressida': 371, 'Richard III': 812}

ratios = {}
lowest = 100
lowestplay = ''
highest =0
highestplay= ''
totalm = 0
totalf = 0

##for play in playkeys:
##    f = femalelines[play]
##    m = malelines[play]
##    totalm += m
##    totalf += f
##    ratio = f/(f+m)
##    if ratio < lowest:
##        lowest = ratio
##        lowestplay = play
##    if ratio > highest:
##        highest = ratio
##        highestplay=play
##    ratios[play] = ratio

##totalr = totalf/(totalf + totalm)
##
##print ratios
##print lowest
##print lowestplay
##print highest
##print highestplay

comedydatam = []
comedydataf = []
tragedydatam = []
tragedydataf = []
historydatam = []
historydataf = []
dummy = []

for play in comedies:
    comedydatam.append(malelines[play] + femalelines[play])
    comedydataf.append(femalelines[play])
    dummy.append(' ')
for play in histories:
    historydatam.append(malelines[play] + femalelines[play])
    historydataf.append(femalelines[play])
for play in tragedies:
    tragedydatam.append(malelines[play] + femalelines[play])
    tragedydataf.append(femalelines[play])

trace1 = Area(
    r=historydataf,
    t=histories,
    name='female',
    marker=Marker(
        color='rgb(242,240,247)'
    )
)

trace2 = Area(
    r=historydatam,
    t=histories,
    name='male',
    marker=Marker(
        color='rgb(158,154,200)'
    )
)
data = Data([trace2, trace1])
layout = Layout(
    title='Line Distribution in Histories',
    legend=Legend(
        font=Font(
            size=16
        )
    ),
    radialaxis=RadialAxis(
    ),
    orientation=270
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='history-num-lines')

