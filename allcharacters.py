import cPickle as pickle

open('allWomen.pkl', 'w')
open('allMen.pkl', 'w')
    
women = {}
men = {}


###Comedies
women["AllsWellThatEndsWell"] = ["countess", "helena", "diana", "mariana"]
men["AllsWellThatEndsWell"] = ["king", "duke", "bertram", "lafeu", "parolles", "rinaldo", "clown"]

women["AsYouLikeIt"] = ['rosalind', 'celia', 'phebe', 'audrey']
men['AsYouLikeIt'] = ['duke senior', 'duke frederick', 'amiens', 'jaques', 'le beau', 'charles',
               'oliver', 'jaques de boys', 'orlando', 'adam', 'dennis', 'touchstone',
               'sir oliver martext', 'corin', 'silvius', 'william', 'hymen']

women['ComedyOfErrors'] = ['aemilia', 'adriana', 'luciana']
men['ComedyOfErrors'] = ['solinus', 'aegeon', 'of ephesus', 'of syracuse', 'dromio of ephesus',
                           'balthasar', 'angelo', 'pinch']

women['Cymbeline'] = ['queen', 'imogen', 'helen']
men['Cymbeline'] = ['cymbeline', 'cloten', 'posthumus leonatus', 'belarius',
                    'guiderius', 'arviragus', 'philario', 'iachimo', 'caius lucius',
                    'pisanio', 'cornelius']

men['LovesLaboursLost'] = ['ferdinand', 'berowne', 'longaville', 'dumain',
                             'boyet,' 'marcade', 'don adriano', 'sir nathaniel',
                             'holofernes', 'dull', 'costard', 'moth']
women['LovesLaboursLost'] = ['rosaline', 'maria', 'katharine', 'jaquenetta']

men['Measure For Measure'] = ['vincentio', 'angelo', 'escalus', 'claudio', 'lucio',
                              'varrus', 'friar thomas', 'friar peter', 'elbow', 'froth',
                              'pompey', 'abhorson', 'barnardine']
women['Measure For Measure'] = ['isabella', 'mariana', 'juliet', 'francisca',
                                'mistress overdone']

men['MerryWivesOfWindsor'] = ['falstaff', 'fenton', 'shallow', 'slender',
                                 'ford', 'page', 'william page', 'sir hugh evans',
                                 'doctor caius', 'bardolph', 'pistol', 'nym',
                                 'robin', 'peter simple', 'john rugby', 'john',
                                 'robert']
women['MerryWivesOfWindsor'] = ['mistress ford', 'mistress page', 'anne page',
                                   'mistress quickly']

men['MerchantOfVenice'] = ['duke', 'morocco', 'arragon', 'antonio', 'bassanio',
                             'solanio', 'gratiano', 'salerio', 'lorenzo', 'shylock',
                             'tubal', 'launcelot', 'old gobbo', 'leonardo',
                             'balthasar', 'stephano']
women['MerchantOfVenice'] = ['portia', 'nerissa', 'jessica']

men['Midsummer Nights Dream'] = ['theseus', 'egeus', 'lysander', 'demetrius',
                                 'philostrate', 'quince', 'snug', 'bottom',
                                 'flute', 'snout', 'starveling', 'oberon',
                                 'puck', 'peaseblossom', 'cobweb', 'moth',
                                 'mustardseed']
women['Midsummer Nights Dream'] = ['titania', 'hippolyta', 'hermia', 'helena']

men['Much Ado About Nothing'] = ['don pedro', 'don john', 'claudio', 'benedick',
                                 'leonato', 'antonio', 'balthasar', 'conrade',
                                 'borachio', 'friar francis', 'dogberry',
                                 'verges']
women['Much Ado About Nothing'] = ['hero', 'beatrice', 'margaret', 'ursula']

men['Pericles'] = ['gower', 'antiochus', 'pericles', 'helicanus', 'escanes',
                   'simonides', 'cleon', 'lysimachus', 'cerimon', 'thaliard',
                   'philemon', 'leonine', 'boult']
women['Pericles'] = ['dionyza', 'thaisa', 'marina', 'lychorida', 'bawd,',
                     'diana']

men['Taming Of The Shrew'] = ['lord', 'sly', 'bartholomew', 'baptista',
                              'vincentio', 'lucentio', 'petruchio', 'gremio',
                              'hortensio', 'tranio', 'biondello', 'grumio',
                              'curtis', 'nathaniel']
women['Taming Of The Shrew'] = ['katarina', 'bianca']

men['The Tempest'] = ['alonso', 'sebastian', 'prospero', 'antonio', 'ferdinand',
                      'gonzalo', 'adrian', 'francisco', 'caliban', 'trinculo',
                      'stephano', 'ariel']
women['The Tempest'] = ['miranda', 'iris', 'ceres', 'juno']

men['Troilus and Cressida'] = ['priam', 'hector', 'troilus', 'paris', 'deiphobus',
                               'helenus', 'margarelon', 'aeneas', 'calchas',
                               'pandarus', 'agamemnon', 'menelaus', 'achilles',
                               'ajax', 'ulysses', 'nestor', 'diomedes', 'patroclus']
women['Troilus and Cressida'] = ['helen', 'andromache', 'cassandra', 'cressida']

men['Twelfth Night'] = ['duke orsino', 'sebastian', 'antonio', 'malvolio',
                        'valentine', 'curio', 'sir toby belch', 'sir andrew',
                        'fabian', 'feste']
women['Twelfth Night'] = ['olivia', 'viola', 'maria']

men['Two Gentlemen of Verona'] = ['duke', 'valentine', 'proteus', 'antonio',
                                  'thurio', 'eglamour', 'speed', 'launce',
                                  'panthino']
women['Two Gentlemen of Verona'] = ['julia', 'sylvia', 'lucetta']

men["The Winter's Tale"] = ['leontes', 'mamillus', 'camillo', 'antigonus', 'cleomenes',
                       'dion', 'polixenes', 'florizel', 'archidamus', 'shepherd',
                       'clown', 'autolycus']
women["The Winter's Tale"] = ['hermione', 'perdita', 'paulina', 'emilia', 'mopsa',
                         'dorcas']

### Histories

men['HenryIV'] = ['king henry iv', 'prince henry', 'prince john', 'westmoreland',
                   'blunt', 'northumberland', 'hotspur', 'mortimer', 'scroop',
                   'archibald', 'glendower', 'vernon', 'falstaff', 'michael',
                   'poins', 'gadshill', 'peto', 'bardolph', 'francis']
women['HenryIV'] = ['lady percy', 'lady mortimer', 'mistress quickly']

men['HenryV'] = ['chorus', 'king henry v', 'gloucester', 'bedford', 'exeter',
                  'york', 'salisbury', 'westmoreland', 'warwick', 'canterbury',
                  'ely', 'cambridge', 'scroop', 'sir thomas grey', 'erpingham',
                  'gower', 'macmorris', 'jamy', 'fluellen', 'bates', 'court',
                  'williams', 'pistol', 'bardolph', 'king of france', 'ramburnes',
                  'gradnpre', 'montjoy']
women['HenryV'] = ['isabel', 'katherine', 'alice']

men['HenryVIPart1'] = ['king henry vi', 'gloucester', 'bedford', 'beaufort',
                          'exeter', 'winchester', 'somerset', 'plantagenet',
                          'york', 'warwick', 'salisbury', 'suffolk', 'talbot',
                          'john talbot', 'mortimer', 'falstaff', 'lucy',
                          'bastard of orleans', 'edmund mortimer', 'glansdale',
                          'gargrave', 'woodville', 'vernon', 'bassett', 'charles',
                          'reignier', 'burgundy', 'alencon']
women['HenryVIPart1'] = ['margaret', 'countess', 'joan la pucelle']

men['HenryVIPart2'] = ['king henry vi', 'gloucester', 'cardinal', 'york',
                          'edward', 'richard', 'somerset', 'suffolk',
                          'buckingham', 'clifford', 'young clifford',
                          'salisbury', 'warwick', 'scales', 'say', 'stafford',
                          'stanley', 'vaux', 'iden', 'whitmore', 'hume',
                          'southwell', 'bolingbroke', 'horner', 'thump',
                          'simpcox', 'cade', 'bevis', 'holland', 'dick',
                          'smith', 'michael']
women['HenryVIPart2'] = ['queen margaret', 'duchess', 'margaret jourdain']

men['HenryVIPart3'] = ['king henry vi', 'edward', 'king lewis xi',
                          'somerset', 'exeter', 'oxford', 'northumberland',
                          'westmoreland', 'somerville', 'stanley',
                          'norfolk', 'montague', 'clifford', 'york',
                          'king edward iv', 'prince edward', 'rutland',
                          'clarence', 'gloucester', 'george', 'richard',
                          'warwick', 'pembroke', 'hastings', 'rivers']
women['HenryVIPart3'] = ['queen margaret', 'lady grey', 'queen elizabeth',
                            'lady bona']

men['HenryVIII'] = ['king henry viii', 'cardinal wolsey', 'cardinal campeius',
                     'capucius', 'cromwell', 'cranmer', 'norfolk',
                     'buckingham', 'suffolk', 'surrey', 'chamberlain',
                     'thomas more', 'gardiner', 'more', 'lincoln', 'sands',
                     'abergavenny', 'guildford', 'lovell', 'vaux', 'denny',
                     'griffith', 'butts', 'brandon']
women['HenryVIII'] = ['queen katharine', 'katharine', 'anne', 'queen anne',
                       'patience']

men['King John'] = ['king john', 'prince henry', 'henry', 'arthur', 'pembroke',
                    'essex', 'salisbury', 'bigot', 'hubert', 'bastard',
                    'king philip', 'faulconbridge', 'gurney', 'lewis',
                    'austria', 'limoges', 'cardinal pandulph', 'melun',
                    'chatillon']
women['King John'] = ['queen elinor', 'constance', 'blanch',
                      'lady faulconbridge']

men['Richard II'] = ['king richard ii', 'john of gaunt', 'langley',
                     'henry bolinbroke', 'king henry iv', 'aumerle',
                     'mowbray', 'norfolk', 'surrey', 'salisbury',
                     'berkeleh', 'bushy', 'bagot', 'green', 'northumberland',
                     'henry percy', 'hotspur', 'percy', 'ross',
                     'willoughby', 'fitzwater', 'carlisle', 'bishop',
                     'westminster', 'marshal' ,'scroop', 'exton', 'sir piers']
women['Richard II'] = ['queen', 'duchess', 'duchess of gloucester']

men['Richard III'] = ['king edward iv', 'edward', 'king edward v', 'york',
                        'wales', 'george', 'richard', 'clarence', 'gloucester',
                      'edward plantagenet', 'richmond', 'king henry vii',
                      'bourchier', 'canterbury', 'rotherham', 'morton',
                      'buckingham', 'norfolk', 'ratcliffe', 'catesby', 'rivers',
                      'dorset', 'lord grey', 'oxford', 'blunt', 'herbert',
                      'brandon', 'hastings', 'stanley', 'vaughan', 'tyrrel',
                      'brackenbury']
women['Richard III'] = ['queen elizabeth', 'elizabeth', 'queen margaret',
                        'margaret', 'duchess', 'duchess of york',
                        'lady margaret']

###Tragedies

men['AntonyAndCleopatra'] = ['mark antony', 'octavius caesar', 'lepidus',
                               'pompey', 'domitius enobarbus', 'ventidius',
                               'eros', 'demetrius', 'philo', 'scarus',
                               'decretas', 'canidius', 'agrippa', 'dolabella',
                               'proculeius', 'mecaenas', 'thyreus', 'gallus',
                               'taurus', 'euphronius', 'menas', 'menecrates',
                               'varrius', 'mardian', 'alexas', 'seleucus',
                               'diomedes', 'silius']
women['AntonyAndCleopatra'] = ['cleopatra', 'octavia', 'charmian']

men['Coriolanus'] = ['marcius', 'titus lartius', 'lartius', 'cominius',
                     'menenius', 'sicinius', 'brutus', 'young marcus',
                     'nicanor', 'aufidius', 'coriolanus']
women['Coriolanus'] = ['volumnia', 'virgilia', 'valeria']

men['Hamlet'] = ['claudius', 'hamlet', 'polonius', 'horatio', 'laertes',
                 'voltemand', 'cornelius', 'rosencrantz', 'guildenstern',
                 'osrick', 'marcellus', 'bernardo', 'francisco', 'reynaldo',
                 'fortinbras']
women['Hamlet'] = ['gertrude', 'ophelia']

men['JuliusCaesar'] = ['caesar', 'octavius', 'antony', 'lepidus', 'cicero',
                        'publius', 'brutus', 'cassius', 'casca',
                        'trebonius', 'libarius', 'cimber', 'cinna', 'flavius',
                        'marullus', 'artemidorus', 'cinna the poet', 'lucilius',
                        'titinius', 'messala', 'young cato', 'volumnius',
                        'varro', 'clitus', 'claudio', 'strato', 'lucius',
                        'dardanius', 'pindarus']
women['JuliusCaesar'] = ['calpurnia', 'portia']

men['King Lear'] = ['king lear', 'king of france', 'burgundy', 'cornwall',
                    'kent', 'albany', 'gloucester', 'edgar', 'edmund', 'curan',
                    'oswald']
women['King Lear'] = ['goneril', 'regan', 'cordelia']

men['Macbeth'] = ['duncan', 'malcolm', 'donalbain', 'macbeth', 'banquo',
                  'macduff', 'lennox', 'ross', 'menteith', 'angus', 'caithness',
                  'fleance', 'seyward', 'young seyward', 'seyton']
women['Macbeth'] = ['lady macbeth', 'lady macduff', 'hecate', 'first witch',
                    'second witch', 'third witch']

men['Othello'] = ['duke of venice', 'brabantio', 'gratanio', 'lodovico',
                  'othello', 'cassio', 'iago', 'roderigo', 'montano']
women['Othello'] = ['desdemona', 'emilia', 'bianca']

men['Romeo and Juliet'] = ['prince', 'paris', 'montague', 'capulet', 'romeo',
                           'mercutio', 'benvolio', 'tybalt', 'friar laurence',
                           'friar john', 'balthasar', 'abraham', 'sampson',
                           'gregory', 'peter']
women['Romeo and Juliet'] = ['lady montague', 'lady capulet', 'juliet', 'nurse']

men['Timon of Athens'] = ['lucius', 'lucullus', 'sempronius', 'ventidius',
                          'apemantus', 'alcibiades', 'flavius', 'flaminius',
                          'lucilius', 'servilius', 'hortensius', 'caphis',
                          'philotus', 'titus', 'poet', 'painter']
women['Timon of Athens'] = ['phrynia', 'timandra']

men['Titus Andronicus'] = ['saturnius', 'emperor', 'bassanius', 'titus andronicus',
                          'marcus andronicus', 'lucius', 'quintus', 'martius',
                          'marcius', 'mutius', 'young lucius', 'publius',
                          'aemilius', 'alarbus', 'demetrius', 'chiron', 'aaron']
women['Titus Andronicus'] = ['tamora', 'lavinia']

pickle.dump(women, open('allWomen.pkl', 'r+'))
pickle.dump(men, open('allMen.pkl', 'r+'))
