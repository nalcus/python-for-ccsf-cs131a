# asgmnt-07-flow.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Extend last week's program so that it also reports the number of times each
# argument occurred."

import sys

setarg=sorted(set(sys.argv))
freqarg=[sys.argv.count(freq) for freq in setarg]
index=0
while index < len(setarg):
    print(setarg[index]+":"+str(freqarg[index]))
    index +=1
