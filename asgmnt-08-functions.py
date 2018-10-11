# asgmnt-08-functions.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Write a program that reports the number, mean, median, mode, and midpoint of
# numeric command line arguments, using functions that determine these statistics."

# NOTE: since we are using command line arguments, but we have not yet learned
# about exception handling, i'm writing this in a way that does not check for
# proper numeric values and will throw an error if we do not give it proper
# input.

import sys

# i'm going to create a list of numbers from the command line because
# i want my functions to be ambiguous of the command line and therefore
# reusable in other situations
numlist = list()
index = 1 # skip the first argument 'asgmnt-08-functions.py'
while index < len(sys.argv):
    numlist.append(float(sys.argv[index]))
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
# i prefer the way str() formats my output over %f
print("mean is: "+str(mean(numlist)))
print("median is: "+ str(median(numlist)))
print("mode is: "+ str(mode(numlist)))
print("midpoint is: "+ str(midpoint(numlist)))
