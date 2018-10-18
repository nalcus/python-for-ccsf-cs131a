# asgmnt-09-exceptions.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Extend the last program so that non-numeric arguments are regarded as integers
#  with value equivalent to their length in characters. Due 10/21."

import sys

# hey, let's make sure the user actually gives us some data to play with
if len(sys.argv) < 2:
    sys.exit("No command line arguments to process")

# if the user DOES enter non-numeric arguments, let's keep track of that fact
# for funzies
strings_supplied = False

# quick n' dirty try/except
numlist = list()
index = 1 # skip the first argument 'asgmnt-09-exceptions.py'
while index < len(sys.argv):
    nextnum=0
    try:
        nextnum=float(sys.argv[index]) # if it's a number we're all good
    except:
        nextnum=len(sys.argv[index]) # otherwise treat it like a string
        strings_supplied = True
    numlist.append(nextnum)
    index +=1

# the mean is the sum of a set divided by the count
def mean(nums):
    total=0
    count=0
    for num in nums:
        total+=num
        count+=1
    return(total/count)

# the median is the number that has the middle index of the set
def median(nums):
    sorted_nums=sorted(nums)
    return(sorted_nums[int(len(sorted_nums)/2)])

# the mode is the number that occurs most frequently in the set
def mode(nums):
    freq_nums=dict()
    for num in nums:
      freq_nums[num]=nums.count(num)
    return (max(nums,key=freq_nums.get))

# the midpoint is the number that occurs between the minimum and maximum numbers
# of the set
def midpoint(nums):
    return((min(nums)+max(nums))/2.0)

# print the results to the user:
print("Here are some math functions applied to the list of numbers supplied:")
if (strings_supplied):
    print("NOTE: Any non-numeric input has been converted to an integer based its length")

# i prefer the way str() formats my output over %f
print("mean is: "+str(mean(numlist)))
print("median is: "+ str(median(numlist)))
print("mode is: "+ str(mode(numlist)))
print("midpoint is: "+ str(midpoint(numlist)))
