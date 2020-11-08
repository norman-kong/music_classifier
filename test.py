from music21 import converter, environment

filepath = 'data/chpn_op66.mid'


# fixing musescore path on my machine
'''
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/Applications/MuseScore 3.app/Contents/MacOS/mscore'
us['musicxmlPath'] = '/Applications/MuseScore 3.app/Contents/MacOS/mscore'
for key in sorted(us.keys()):
    print(key, "is",  us[key])
'''

#def map_notes():
    
score = converter.parseFile(filepath) # Returns Stream object
score.show('text')

