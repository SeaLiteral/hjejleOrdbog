# hjejleOrdbog
A Danish stenography dictionary

License: GPLv3 or later

It is divided in multiple files:
* *dansk.json* with words
* *dansk-bogstaver.json* contains letters for fingerspelling
* *dansk-sammensat.json* contains multi-word briefs

Also, it is still under construction, so many words are still missing, but here is some documentation:
# Layout
For speakers of Danish, this is what the layout would look like if it followed Danish spelling:

    S- T- P- H- * -V -P -L -T -D
    S- K- V- R- * -R -E -K -S -N
         A(r) O(r)   Æ Å

This doesn't mean A and O add consonants. I added them in brackets because the sounds I represent with those keys are the vowel sounds found in the words "rat" (pronounced /Rad/) and "flot" (pronounced /flɒd/), not the sounds that the vowels would make on their own. Danish spelling uses nine letters to represent what is actually twelve vowels, not counting vowel length, stød (a feature that might be realised as glottalization, pharyngealization or tone depending on the speaker's accent)or diphtongs. Length and stød are particularly nasty because they pretty much multiply the amount of vowels by three and we don't have space for 34 vowels on a 22 key keyboard: Danish has roughly the English set of consonant clusters replacing /w/ by /v/ (sometimes by /ʋ/, but that's allophonic variation) and allowing initial /kn/, except the consonant inventory is slightly smaller, particularly at the end of syllables.

As I currently switch to English Dictionaries a lot, the Dictionaries here are currenntly assuming that you use the American English stenotype layout which looks like this:
    S- T- P- H- * -F -P -L -T -D
    S- K- W- R- * -R -B -G -S -Z
         A O   E U

Okay, here's the IPA representation of what each key would do on its own:

    s t p h * v b l d ð
    s k v ʁ * ɘ e g s n
        a ɒ ɛ ɔ

# Vowels
As for vowel key combinations, here they are, and now I am just refering to what the keys are called on the US layout, I'm including random words that contain the vowel sounds):

* A: /a/ (sammen: SAPB)
* O: /ɒ/ (sov: SOV)
* E: /ɛ/ (sær: SER)
* U: /ɔ/ (gå: TKPWU)
* AE: /æ/ (gade: TKPWA*EBD)
* OE: /ø/ (gø: TKPWOE)
* AU: /o/ (god: TKPWAU)
* OU: /œ/ or /ɶ/(gør: TKPWOUR)
* AO: /u/ (ud: AOD)
* EU: /e/ (vil: WEU, the *l* is silent in my accent)
* AOE: /i/ (i: AOE)
* AOU: /y/ (by: PWAOU)
* AEU: (dipthong) /aɪ/ (segl: SAEUL) (this diphtong is usually, AOEU, but some words use it for disambiguation)
* OEU: (diphtong) /ɒɪ/ (støj: STOEU)
* AOEU: (dipthong) /aɪ/ (sejl: SAOEUL)

# Consonants
what each consonant does on its own, refer to the IPA table, but the following sounds are worth mentioning:

* -B: should add the /e/ suffix if that doesn't create ambiguity. Due to missing entries (and consonant ghosting, a feature Plover doesn't have), you may need to add this one to some words before adding other suffixes after it.
* -F: Is mostly used /v/ and its semivowel variant /ʋ/, but may sometimes represent /f/. I might also use it for /s/ like the English layout does.
* -R in addition to the /ɘ/ semivowel, it can represent a /ɘ/ syllable, which is a common suffix spelled "-er".
* -T: the /ed/ suffix, commonly spelt "et".
* -D: the /eðː/ suffix, commonly spelt "ede".

The consonant combinations work more or less like in English:
* TP-: /f/
* PH-: /m/
* TPH-: /n/
* KWR-: /j/
* SKWR- or SH-: /ɕ/, maybe /dʒ/ in some loanwords
* KW-: /kv/, just including it for completeness, Danish doesn't have a /w/
* -FP, -RB and -RBGS are not used like in English, since Danish doesn't allow those sounds in syllable codas.
* -PL: /m/
* -PB: /n/
* -PBG: /ŋ/

# Fingerspelling
Here is a table for the letters used in Danish (for capital letters add -P):

|Letter  |Keys (English layout)|Keys (Danish layout)|
| ------ | ------------------- | ------------------ |
|a       |A*                   |A*                  |
|b       |PW*                  |PV*                 |
|c       |KR*                  |KR*                 |
|d       |TK*                  |TK*                 |
|e       |*EU                  |*ÆÅ                 |
|f       |TP*                  |TP*                 |
|g       |TKPW*                |TKPV*               |
|h       |H*                   |H*                  |
|i       |AO*E                 |AO*Æ                |
|j       |KWR*                 |KVR*                |
|k       |K*                   |K*                  |
|l       |HR*                  |HR*                 |
|m       |PH*                  |PH*                 |
|n       |TPH*                 |TPH*                |
|o       |A*U                  |A*Å                 |
|p       |P*                   |P*                  |
|q       |KW*                  |KV*                 |
|r       |R*                   |R*                  |
|s       |S*                   |S*                  |
|t       |T*                   |T*                  |
|u       |AO*                  |AO*                 |
|v       |W*                   |V*                  |
|w       |SR*                  |SR*                 |
|x       |KP*                  |KP*                 |
|y       |AO*U                 |AO*Å                |
|z       |STKPW*               |STKPV*              |
|æ       |*E                   |*Æ                  |
|ø       |O*E                  |O*Æ                 |
|å       |*U                   |*Å                  |
|A       |A*P                  |A*P                 |
|B       |PW*P                 |PV*P                |
|C       |KR*P                 |KR*P                |
|D       |TK*P                 |TK*P                |
|E       |*EUP                 |*ÆÅP                |
|F       |TP*P                 |TP*P                |
|G       |TKPW*P               |TKPV*P              |
|H       |H*P                  |H*P                 |
|I       |AO*EP                |AO*ÆP               |
|J       |KWR*P                |KVR*P               |
|K       |K*P                  |K*P                 |
|L       |HR*P                 |HR*P                |
|M       |PH*P                 |PH*P                |
|N       |TPH*P                |TPH*P               |
|O       |A*UP                 |A*ÅP                |
|P       |P*P                  |P*P                 |
|Q       |KW*P                 |KV*P                |
|R       |R*P                  |R*P                 |
|S       |S*P                  |S*P                 |
|T       |T*P                  |T*P                 |
|U       |AO*P                 |AO*P                |
|V       |W*P                  |V*P                 |
|W       |SR*P                 |SR*P                |
|X       |KP*P                 |KP*P                |
|Y       |AO*UP                |AO*ÅP               |
|Z       |STKPW*P              |STKPV*P             |
|Æ       |*EP                  |*ÆP                 |
|Ø       |O*EP                 |O*ÆP                |
|Å       |*UP                  |*ÅP                 |

# Todo
* Add words
* Add briefs
* Documentation in Danish
