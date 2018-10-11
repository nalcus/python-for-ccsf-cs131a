# asgmnt-06-containers-ii.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Write a program that prints out the command line arguments it receives, in
# alphabetical order and without duplicates."

import sys

# although it's not as pretty for a human reader, using nested functions like
# this to fire of complex action in a single line really shows off the capability
# of python. aside from the comments, this program is two lines long, and one of
# them is an import. Take that, c++!
print(*sorted(set(sys.argv)), sep="\n")
