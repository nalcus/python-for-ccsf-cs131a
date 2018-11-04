# asgmnt-11-files.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Write a program that displays a word six letters long randomly chosen from
#  the dictionary /users/abrick/resources/english. Due 11/4."

# Review files specified on the command line

# this program to use the file "american-english-insane-ascii" which is
# what /users/abrick/resources/english points to. the file MUST be located
# in the local running directory where the program is launched from.
# however, IF there is a command-line argument, the program will attempt
# to use the first argument as the filename.

import sys, random

# default filename
file = "american-english-insane-ascii"

print ('This program will attempt to read a dictonary file and then print out a')
print ('random word that is six characters long from that dictionary')

# if the user provided a command line argument, use it as the filename instead
if len(sys.argv)>1:
    file=sys.argv[1]

# try to open the dictionary file
try:
    print ('attemping to open: \"'+file+'\"')
    wrapper = open (file)
except FileNotFoundError:
    print ('File not found' )
except PermissionError:
    print ('File is not readable' )
except IsADirectoryError:
    print ('File is a directory' )
# Report a successful open
else:
    print ('File read OK!')
    # count the number of lines total
    num_lines = sum(1 for line in wrapper)
    #set the file reader back to the beginning
    wrapper.seek(0)
    #pick a random offset
    count = 0
    eof_count = 0
    offset=random.randint(0,num_lines)
    # loop through the file
    for line in wrapper:
        # skip ahead to the random offset
        if count>=offset:
            # if the line we reach is 6 characters long, print it and break
            # out of the for loop
            if len(line)==6:
                print(line)
                break
        count=count+1
        # if we reach the EOF without finding a six character line,
        # go back to the beginning
        if count>=num_lines:
            # just to be sure, let's count the number of times we reach the
            # end of the file
            eof_count=eof_count+1
            # if we have wrapped around the file MORE THAN ONCE, then we can be
            # sure that there is no 6 letter word, and we should stop This
            # fruitless search, lest we be ensnared in an infinite loop!
            if eof_count>1:
                print ('The file has been searched completely, and no 6 letter word was found!')
                break
            count=0
            wrapper.seek(0)
    # be sure and close up that file, now ;)
    wrapper.close()
