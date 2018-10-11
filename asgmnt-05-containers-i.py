# asgmnt-05-containers-i.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Write a program that prints out its own command line arguments in reverse
# order from last to first."

import sys
index=0
while index < len(sys.argv):
    print(sys.argv[-(index+1)])
    index = index + 1
