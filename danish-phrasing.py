'''A Python dictionary for a simple Danish phrasing system.

Phrases are made using only consonant keys to avoid
conflicts with words.'''

# TODO: The keys -T and -S don't do anything right now.
#       They should be grouped with -Z and S- or maybe
#       made into a group of their own.

# Known issue: the code doesn't know about past participles
#              or where they should be used. After "har"
#              is the most obvious place to use them.

LONGEST_KEY = 1

part_text='''\
H|v|har|havde|have
HR|n|denne||
K|v|kan|kunne|kunne
KH|v|går|gik|gå
KHR|k|og||
KP|n|han||
KPH|n|ham||
KPHR----------------------
KPR|p|på||
KPW|k|og||
KPWH|k|{,} og||
KPWHR---------------------
KPWR----------------------
KW|n|hun||
KWH|n|hende||
KWHR|n|mig||
KWR|n|jeg||
P|a|nu||
PH|v|må|måtte|måtte
PHR|v|bør|burde|
PW|n|I||
PWH-----------------------
PWHR|n|os||
PWR-----------------------
R|v|er|var|være
T|v|vil{+:k}|ville|ville
TH|k|at||
TK|n|det||
TKH|n|den||
TKHR|n|dette||
TKP|v|ser|så|se
TKPH|p|til||
TKPHR|p|i||
TKPR|n|de||
TKPW|n|man||
TKPWH|n|af||
TKPWHR--------------------
TKPWR|n|men||
TKR|n|der||
TKW|n|dem||
TKWH---------------------
TKWHR|n|denne||
TKWR---------------------
TP------------------------
TPH|p|i||
TPHR|v|siger|sagde|sige
TPR|p|fra||
TR|v|synes|syntes|synes
TW|n|du||
TWH|n|dig||
TWHR|k|{,} at||
TWR|v|ved|vidste|vide
W|b|ikke||
WH|v|skal|skulle|
WHR|n|jer||
WR|n|vi||
-- pre-initials
S|k|det||
ZS|k|den||
ZS|k|og||'''
past_starters=['T']

parts_translations={}
parts_past_tenses={}
parts_of_speech={}
parts_infinitives={}
for line in part_text.splitlines():
    if not line: continue
    if '-' in line: continue
    parts=line.split('|')
    if(len(parts)!=5):
        print(parts)
        raise ValueError
    parts_of_speech[parts[0]]=parts[1]#v
    parts_translations[parts[0]]=parts[2]#er
    parts_past_tenses[parts[0]]=(parts[3]#var
                                 or parts[2])#er
    parts_infinitives[parts[0]]=(parts[4]#være
                                 or parts[3]#var
                                 or parts[2])#er

#TSLGPBFR
#ZSTKPWHR

half_layout_reverse_text = '''F H
R R
P P
B W
L T
G K
T Z
S S'''

half_layout_reverse = {}
half_layout_reverse_keys = []
for i in half_layout_reverse_text.splitlines():
    pair = i.split()
    half_layout_reverse [pair[0]] = pair[1]
    half_layout_reverse_keys.append(pair[0])

def reverse_right_half (stroke):
    new_stroke = ''
    for i in stroke:
        if i in half_layout_reverse_keys:
            # This changes the keys and also reverses
            #  the order they appear in.
            new_stroke = half_layout_reverse [i] + new_stroke
    for i in 'SZ KT WP RH'.split():
        new_stroke = new_stroke.replace(i, ''.join(tuple(reversed(i))))
    return new_stroke

def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    if '-' not in key[0]:
        raise KeyError
    stroke = key[0]
    if 'Z' in stroke:
        stroke = 'Z'+stroke[:-1]
    start, end = tuple(stroke.split('-'))
    end = reverse_right_half(end)
    if start==end: raise KeyError # punctuation stroke
    other=''
    if start.startswith('Z'):
        other+='Z'
        start=start[1:]
    if start.startswith('S'):
        other='S'+other
        start=start[1:]
    if (start not in parts_translations
        or end not in parts_translations):
        print(start, end)
        raise KeyError # Just in case
    prestart=''
    if (other):
        print(other)
        if (other in parts_translations):
            prestart=parts_translations[other]
        else:raise KeyError # Unknown prestart
    first = parts_translations [start]
    last  = parts_translations [end]
    if 'D' in stroke:
        first= parts_past_tenses [start]
        last = parts_past_tenses [end]
    if (parts_of_speech [start]=='v'
        and parts_of_speech [end]=='v'):
        last = parts_infinitives [end]
    if prestart:
        return prestart + ' ' + first + ' ' + last
    return first + ' ' + last

if __name__=='__main__':
    for i in 'KW-G TR-FD SWR-R'.split():
        print(i+':', lookup ([i]))
