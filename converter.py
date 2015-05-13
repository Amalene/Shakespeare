import json
import cPickle as pickle
from collections import namedtuple
from textblob import TextBlob

Line = namedtuple('Line', 'line_number speech_number play_name text_entry line_id speaker speaker_gender')
#a list of named tuples
lines = []

f = open("AllsWellThatEndsWell.js", "r+")

allPlays = {"Alls well that ends well":"All's Well That Ends Well",
            "Antony and Cleopatra":"Antony and Cleopatra",
            "As you like it":"As You Like It",
            "A Comedy of Errors":"A Comedy of Errors",
            "Coriolanus":"Coriolanus",
            "Cymbeline":"Cymbeline",
            "Hamlet":"Hamlet",
            "Henry IV":"Henry IV Part 1",
            "Henry IV Part 2":"Henry IV Part 2",
            "Henry V":"Henry V",
            "Henry VIII":"Henry VIII",
            "Henry VI Part 1":"Henry VI Part 1",
            "Henry VI Part 2":"Henry VI Part 2",
            "Henry VI Part 3":"Henry VI Part 3",
            "Julius Caesar":"Julius Caesar",
            "King John":"King John",
            "King Lear":"King Lear",
            "Loves Labours Lost":"Love's Labours Lost",
            "macbeth":"Macbeth",
            "Measure for measure":"Measure for Measure",
            "Merchant of Venice":"The Merchant of Venice",
            "Merry Wives of Windsor":"The Merry Wives of Windsor",
            "A Midsummer nights dream":"A Midsummer Night's Dream",
            "Much Ado about nothing":"Much Ado About Nothing",
            "Othello":"Othello",
            "Pericles":"Pericles",
            "Richard II":"Richard II",
            "Richard III":"Richard III",
            "Romeo and Juliet":"Romeo and Juliet",
            "Taming of the Shrew":"The Taming of the Shrew",
            "The Tempest":"The Tempest",
            "Timon of Athens":"Timon of Athens",
            "Titus Andronicus":"Titus Andronicus",
            "Troilus and Cressida":"Troilus and Cressida",
            "Twelfth Night":"Twelfth Night",
            "Two Gentlemen of Verona":"The Two Gentlemen of Verona",
            "A Winters Tale":"The Winter's Tale"}
            
            

#breaks up the whole document into individual lines
#this really would have been better done by making use of .split("{")
#but yolo
currentline = ""
linestrings = []
counter = 1
for line in f:
    if line.strip() == "{":
        currentline = "{"
    elif line.strip() == "}" or line.strip() == "},":
        currentline += line
        linestrings.append(currentline)
    else:
        currentline+=line
    counter +=1

#change this for each play
numMen = 0
numWomen = 0
numSD = 0
numUnknown = 0
men = ["king", "duke", "bertram", "lafeu", "parolles", "rinaldo", "clown"]
women = ["countess", "helena", "diana", "mariana"]

#convert into named tuples
#make sure that you fix the current irritating problem with stage directions and
#speakers/line numbers
shit = 0;
for line in linestrings:
    shit +=1
    line = line.split(':')
    #print line
    lineNumber = line[1].split('"')[1]
    if lineNumber == '':
        lineNumber = '0'
    #print "lineNumber is " + lineNumber
    speechNumber = line[2].split(",")[0]
    #print "speechNumber is " + speechNumber
    playName=allPlays[line[3].split(",")[0].split('"')[1]]
    #print "playName is " + playName
    textEntry = line[4].split('"')[1]
    #print "textEntry is " + textEntry
    lineId = line[5].split(",")[0]
    #print "lineId is " + lineId
    speaker = line[6].split(",")[0].split("}")[0].strip().lower().replace('"', '')
    if speaker == "stage directions":
        speakerGender = "none"
        numSD +=1
    elif speaker in men:
        speakerGender = "male"
        numMen +=1
    elif speaker in women:
        speakerGender = "female"
        numWomen += 1
    else:
        speakerGender = "unknown"
        if numUnknown < 20:
            print "speaker is: " + speaker + "    " + lineNumber
        numUnknown += 1
        
    #print "speaker is " + speaker
    l = Line(lineNumber, speechNumber, playName, textEntry, lineId, speaker, speakerGender)
    lines.append(l)


print "numMen is " + str(numMen)
print "numWomen is " + str(numWomen)
print "numSD is " + str(numSD)
print "numUnknown is " + str(numUnknown)

flines = ""
mlines = ""

for l in lines:
    if l.speaker_gender == "female":
        flines += l.text_entry
    elif l.speaker_gender == "male":
        mlines += l.text_entry

fblob = TextBlob(flines)
mblob = TextBlob(mlines)

print str(fblob.polarity) + "  female"
print str(mblob.polarity) + "  male"


#make the plays into pure text (totally ignore all the other information)
for line in linestrings:
    line = line.split(':')
    textEntry = line[4].split('"')[1]
    


#save the namedtuple as the playname file
pickle.dump(lines, open("AllsWellThatEndsWell.p", "wb"))
x = pickle.load(open("AllsWellThatEndsWell.p", 'rb'))

meow = ""

print len(x)


i = x[0]
print i.text_entry

#print meow[14]

print len(lines)

print "counter is " + str(counter)
print len(linestrings)
