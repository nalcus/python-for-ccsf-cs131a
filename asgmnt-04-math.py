# asgmnt-04-math.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Write a program to determine what fraction of global population has
# permanent representation on the United Nations Security Council. Make sure to
# cite the sources of the numbers you use."

from fractions import Fraction

print ("The five countries that hold a permanent seat at the united nations")
print ("and their populations are as follows:\n")

world = 7550262101
china = 1409517397
us = 324459463
russia = 146989754
uk = 66181585
france = 64979548
fivenations = china+us+russia+uk+france
popfract = Fraction(fivenations,world)

print ("china ",china)
print ("united states ", us)
print ("russia ", russia)
print ("uk ", uk)
print ("france ", france)
print ("total of five nations ", fivenations)
print ("\nThe world population is ",world)
print ("therefore, the fraction of the five nations to world population")
print ("is ", popfract)

print ("\nreferences:")
print ("https://en.wikipedia.org/wiki/Permanent_members_of_the_United_Nations_Security_Council")
print ("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")
