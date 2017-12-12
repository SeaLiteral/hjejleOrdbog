'''Fingerspelling table builder.
Reads the fingerspelling dictionary and generates a table
listing how to write each letter.
The table is output to standard output.
It should be run from the directory containing the dictionary
unless edited to point elswhere or to get input to find it.
'''
 #
#  Copyright (C) 2017 Lars Rune (SeaLiteral) Præstmark
 # This file is part of the HjejleOrdbog Danish stenography dictionary collection.
#  This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
# 
 # This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
 #
#  You should have received a copy of the GNU General Public License
 # along with this program. If not, see <http://www.gnu.org/licenses/>.
#

FINGERSPELLING_DICT='dansk-bogstaver.json' # The fingerspelling dictionary

def makeDanish(stroke):
    '''Translates a stroke from the English layout into the Danish one.'''
    position=0
    result=''
    for key in 'S T K P W:V H R A O * E:Æ U:Å - F:V R P B:E L G:K T D S Z:N'.split():
        eng=''
        dan=''
        if(':' in key):
            parts=key.split(':')
            eng=parts[0]
            dan=parts[1]
        else:
            eng=key
            dan=key
        if(position>=(len(stroke))):
           return(result)
        if(stroke[position]==eng):
            result+=dan
            position+=1
    return(result)

def makeTable(text):
    '''Builds the table based on a fingerspelling Dictionary.
The table will have three columns, one for the letters, one for the strokes
written according to the English layout, and one for the stroke according to
the Danish layout. The table is returned to the caller.'''
    MIN_COLWIDTH=8 # How wide must each column be at a minimum
    headers=['Letter', 'Keys (English layout)', 'Keys (Danish layout)']
    cellWidths=[max(MIN_COLWIDTH,len(cell)) for cell in headers]
    headers=[name.ljust( max(MIN_COLWIDTH,len(name)) ) for name in headers]# Add spaces to give all columns the same width.
    headLine='|'+ '|'.join(headers) +'|'
    result=headLine+'\n|'+('|'.join([' '+('-'*(len(i)-2))+' ' for i in headers]))+'|\n' # Headers and dash-line
    for line in text.splitlines():
        lParts=line.split('": "') #Not the proper way to parse a dictionary, but it works for this purpose.
        if(len(lParts)==2):
            stroke=lParts[0][1:]
            word=lParts[1][:-1]
            if(lParts[1].endswith(',')):
                word=lParts[1][:-2]
            if(word.startswith('{>}')): word=word[3:]
            if(word.startswith('{&') and word.endswith('}')): # This is very specific to fingerspelling,
                word=word[2:-1]                               # But it should handle multi-letters.
            stroke2=makeDanish(stroke)
            result+='|'+word.ljust(cellWidths[0])+'|'+stroke.ljust(cellWidths[1])+'|'+stroke2.ljust(cellWidths[2])+'|\n'
    return(result)

if(__name__=='__main__'):
    with open(FINGERSPELLING_DICT) as dictFile:
        text=dictFile.read()
    print(makeTable(text))
