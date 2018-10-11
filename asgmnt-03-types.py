# asgmnt-03-types.py
# by nicholas alcus
# for CS131A at City College of San Francisco - http://www.ccsf.edu/

# "Every state in the U.S. has two senators no matter its population. Write a
# program that shows how much more powerful Idahoans are than Floridians in the
# Senate. Make sure to cite the sources of the numbers you use."

population_of_florida = 20984400
population_of_idaho = 1716943

print("The population of Florida is ", population_of_florida)
print("The population of Idaho is ", population_of_idaho)
print("reference: https: //en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population")

print("\nEach state has 2 senators no matter what the population.")
print("The voting power then, can be calculated is power = 2 / population.")

power_of_floridians=2/population_of_florida
power_of_idahoans =2/population_of_idaho

print("\nEach citizen of Florida represents {:.7%} of a Senator's voting power".format(power_of_floridians))
print("Each citizen of Idaho represents {:.7%} of a Senator's voting power".format(power_of_idahoans))

power_ratio=power_of_idahoans/power_of_floridians

print("\nTherefor, Idahoans have {:0.2f} times more power in elections than Floridians".format(power_ratio))
