# asgmnt-10-exceptions.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Define a class, objects of which can make the same function calls as the last
#  program. It should have a useful string representation and the command line
#  invocation should still work. Due 10/28."

import sys

class Computations:

    numlist = list()
    strings_supplied = False

    def process_args(self):
        # hey, let's make sure the user actually gives us some data to play with
        if len(sys.argv) < 2:
            sys.exit("No command line arguments to process")

        # if the user DOES enter non-numeric arguments, let's keep track of that fact
        # for funzies
        strings_supplied = False

        index = 1 # skip the first argument 'asgmnt-10-exceptions.py'
        while index < len(sys.argv):
            nextnum=0
            try:
                nextnum=float(sys.argv[index]) # if it's a number we're all good
            except:
                nextnum=len(sys.argv[index]) # otherwise treat it like a string
                strings_supplied = True
            self.numlist.append(nextnum)
            index +=1

    # the mean is the sum of a set divided by the count
    def mean(self):
        total=0
        count=0
        for num in self.numlist:
            total+=num
            count+=1
        return(total/count)

    # the median is the number that has the middle index of the set
    def median(self):
        sorted_numlist=sorted(self.numlist)
        return(sorted_numlist[int(len(sorted_numlist)/2)])

    # the mode is the number that occurs most frequently in the set
    def mode(self):
        freq_numlist=dict()
        for num in self.numlist:
          freq_numlist[num]=self.numlist.count(num)
        return (max(self.numlist,key=freq_numlist.get))

    # the midpoint is the number that occurs between the minimum and maximum numbers
    # of the set
    def midpoint(self):
        return((min(self.numlist)+max(self.numlist))/2.0)

    def get_strings_supplied(self):
        return self.strings_supplied

    def __init__(self):
        print("Computation class is being initialized...")
        self.process_args()

    def __repr__(self):
        rep="("
        for num in self.numlist[:-1]:
            rep=rep+str(num)+", "
        rep=rep+str(self.numlist[-1])+")"
        return rep

# instance the class
c=Computations()

# print the results to the user:
print("This program applies a collection of mathematical functions to the command")
print("arguments supplied.")
if (c.get_strings_supplied()):
    print("NOTE: Any non-numeric input has been converted to an integer based its length")

print("The arguments supplied and processed are as follows:")
print(c)

print("Here are some math functions applied to the list of numbers supplied:")


# i prefer the way str() formats my output over %f
print("mean is: "+str(c.mean()))
print("median is: "+ str(c.median()))
print("mode is: "+ str(c.mode()))
print("midpoint is: "+ str(c.midpoint()))
