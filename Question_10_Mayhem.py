"""
300 total properties
150 for Speedikleen (North)
150 for Quikpolish (South)

"Today both cleaning agencies call in and let you know there has been a workers 
strike. speedikleen has shut for the day and cannot clean any properties, 
quikpolish has managed to do half the properties it was contracted to do. 
Your inspection manager leaves you a voicemail and says he’s inspected 
3 properties, all on the same side of the river and none have been cleaned. 
What are the odds that he is on the north side of the river?"


The logic here is to find the number of three unclean properties inspected in
a row, where individually on the north and south side, then find the proportion
of repeats where on the north side and calculate a probability from the total
times found on the north or south.

"""

import random as rand

runs = 10000 # total repeats

North_counter = 0 # these counters start at 0 since no hat-trick of unclean
South_counter = 0 # properties have yet been found

for i in range(runs): # begins the repeats, where more repeats yields higher
                      # accuracy on the final probability
    
    North_South_random = rand.randint(0,1) # North = 0 , South = 1
                                           # essentially decides which side
                                           # the inspector is on
                                           
    if North_South_random == 0: # if the random = 0 then there is a 100% rate
        North_counter += 1      # of finding 3 unclean properties on the north
        continue                # thus skipping this run and adding to 
                                # north_counter
                                
    else:                       # if not in the north, we are in the south
        
        container = []          # list of unclean and clean properties
                                     
        for j in range(75):         # filling with clean (=1) and unclean (=0)
                                    # on the south side, where 75 due to
            container.append(0)     # appending two rooms at once for a total
            container.append(1)     # of 150 rooms


        for n in range(3):      # looking at 3 random properties

            random_number = rand.randint(0,len(container)-1) # randomly chooses
                                                             # a south side
                                                             # property
        
            if container[random_number] == 1: # if a clean room is found then
                break                         # we do not add this to the
                                              # counter, and we break

            elif container[random_number] == 0: # elif an unclean room is found
                
                container.pop(random_number) # remove the inspected unclean
                                             # property from the pool of 
                                             # properties to give the correct
                                             # probabilty of finding another
                                             # unclean property
                                             
                if n == 2:             # if this for loops manages to get to 
                    South_counter += 1 # the third property as unclean with the
                                       # two prior being unclean as well, then 
                                       # add to South_counter
                    

print("North counter = ", North_counter)
print("South counter = ", South_counter)
print("Final probability = ", (North_counter) / (North_counter + South_counter)
      )
