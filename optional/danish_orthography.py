'''Self-building dictionary implementing Danish orthography.
This is a workaround until a Danish system can be working on its own.
It requires the python dictionaries plugin to work.'''

#
#  Copyright (C) 2017 Lars Rune Præstmark
# This file is part of the HjejleOrdbog Danish stenography dictionary collection.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#


LONGEST_KEY = 2
RELOAD_DICTIONARY_STROKE='TKPWHRES'
DICT_FILENAMES=['PATH/TO/FILE'] # Change this to wherever you store the any Danish dictionaries

mainList={}

def getDict():
    '''Read the dictionary file, for now I'm only reading one file.
This is called at the start and when the user requests reloading it.
You must either restart Plover or manually use RELOAD_DICTIONARY_STROKE
if the dictionary changes when you're using it.
Otherwise the lookup function will not see the changes.'''
    global mainList
    for fname in DICT_FILENAMES:
        with open(fname)as dictFile:
            for i in dictFile:
                if('": "')in i:
                    j=i.split('": "')
                    iKey=j[0][1:]
                    iTrans=j[1]
                    while(iTrans[-1].isspace()):
                        iTrans=j[1][:-1]
                    if(iTrans[-1]==','):
                        iTrans=iTrans[:-1]
                    if(iTrans[-1]=='"'):
                        iTrans=iTrans[:-1]
                    if(iKey.endswith('/-B')): #The dictionary defines
                        mainList[iKey[:-3]]=iTrans # how to add the -e suffix
                    else: # we add the suffix without applying English
                        mainList[iKey]=iTrans+'e' # orthography rules.

getDict() # Setup the dictionary

def hasFinal(stroke, suffix):
    '''Check if a stroke contains a particular key after the vowel part.'''
    for i in 'AO*EU-':
        if(i in stroke): return(suffix in stroke.split(i)[1])

def removeFinal(stroke, suffix):
    '''Return a stroke minus a final consonant'''
    for i in 'AO*EU-':
        if(i in stroke):
            parts=stroke.split(i)
            return(parts[0]+i+(parts[1].replace(suffix,'')))

def lookup(key):
    '''Main lookup function:
Applies suffix folding and simple orhography rules for Danish.
'''
    assert len(key) <= LONGEST_KEY
    
    if(len(key)==2): # The second stroke must be a suffix stroke
        if((key[1][0]=='-') and (len(key[1]==2))):
            if(key[1]=='-R'):
                return(mainDict[key[0]]+'r')
            if(key[1]=='-T'):
                return(mainDict[key[0]]+'t')
            if(key[1]=='-Z'):
                return(mainDict[key[0]]+'n')
        raise keyError #Can't handle other endings
    if(key[-1]==RELOAD_DICTIONARY_STROKE):
        getDict()
    if('B' in key[-1]): # The -e suffix is used as a base,
        # ------------  # which we can add other suffixes to.
        # ------------  # This is the form we store words in.
        keyForNow=key[-1].replace('B','')
        if(keyForNow.endswith('-')):keyForNow=keyForNow[-1]
        keyPrefix=''
        if(len(key)>1):
            keyPrefix='/'.join(key[:-1])
        keyForNow=keyPrefix+keyForNow
        if(keyForNow in mainList):
           return(mainList[keyForNow])
    if(hasFinal(key[-1],'R')): # -er is used for plurals, proffesions
        keyForNow=removeFinal(key[-1],'R') # and present tense,
        if(keyForNow.endswith('-')):keyForNow=keyForNow[-1]
        keyPrefix=''
        if(len(key)>1):
            keyPrefix='/'.join(key[:-1])
        keyForNow=keyPrefix+keyForNow
        if(keyForNow in mainList):
           return(mainList[keyForNow]+'r')
    if(hasFinal(key[-1],'T')): # -et is used for past participles, neuter
        keyForNow=removeFinal(key[-1],'T') # adjectives and neuter "the".
        if(keyForNow.endswith('-')):keyForNow=keyForNow[-1]
        keyPrefix=''
        if(len(key)>1):
            keyPrefix='/'.join(key[:-1])
        keyForNow=keyPrefix+keyForNow
        if(keyForNow in mainList):
           return(mainList[keyForNow]+'n')
    if(hasFinal(key[-1],'Z')): # -en is mainly used as a common-gender "the".
        keyForNow=removeFinal(key[-1],'Z')
        if(keyForNow.endswith('-')):keyForNow=keyForNow[-1]
        keyPrefix=''
        if(len(key)>1):
            keyPrefix='/'.join(key[:-1])
        keyForNow=keyPrefix+keyForNow
        if(keyForNow in mainList):
           return(mainList[keyForNow]+'n')

    raise KeyError
