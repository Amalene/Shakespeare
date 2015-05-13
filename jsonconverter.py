import json
import jsonpickle
import cPickle as pickle
from collections import namedtuple

aline = namedtuple('Line', 'line_number speech_number play_name text_entry line_id speaker speaker_gender')
#a list of named tuples
lines = []

class Line:

    def __init__(self, line_number, speech_number, play_name, text_entry, line_id,
                 speaker):
        self.line_number = line_number
        self.speech_number = speech_number
        self.play_name = play_name
        self.text_entry = text_entry
        self.speaker = speaker
        self.speaker_gender = speaker_gender

f = open("WintersTale.js", "r+")

print f

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

playstring = ""

count = 0

for line in f:
    playstring += line
    if count < 5:
        print line
    count +=1


pythonversion = jsonpickle.decode(playstring)

newfile = open('WintersTale.pkl', 'r+')

pickle.dump(pythonversion, newfile)

newfile.seek(0)

kipper = pickle.load(newfile)

print kipper.keys()
