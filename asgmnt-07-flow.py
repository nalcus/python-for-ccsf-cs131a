# asgmnt-07-flow.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Extend last week's program so that it also reports the number of times each
# argument occurred."

import sys

# create a sorted set from the command line arguments collection
setarg=sorted(set(sys.argv))

# count the number of times each argument in setarg appears in the
# command line collection and put those counts in a new set
freqarg=[sys.argv.count(arg) for arg in setarg]

# print the sorted set of arguments along with the frequency
print ("Here is an alphabetical list of the command line arguments submitted along \nwith the frequency they occur:")
index=0
while index < len(setarg):
    print("%s:%i" % (setarg[index],freqarg[index]))
    index +=1
