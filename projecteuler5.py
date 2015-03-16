#################################################################################################################
## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  ##
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?           ##
#################################################################################################################

import time
testArray=list(range(1,21)) # Array containing numbers 1-20
counter=0 # Counter variable initialized to 0
i=2 # Variable i initialized to 2 (because all numbers are divisible by 1)
start_time = time.time() # Get the start time (execution)
while counter != 20: # Till the counter reaches 20
   for j in range(0,len(testArray)): # Looping through the array of numbers 1-20
      if i%testArray[j]==0: # Check if array element at index j is evenly divisible by i
         counter+=1 # If it is, increment the counter variable
      else: # If any element is not evenly divisible by i
         counter=0 # Reset counter to 0
   i+=1 # Next integer
print("Answer: ",i-1) # When counter reaches 20, print the answer
print("Execution time: ",(time.time() - start_time)/60," minutes.") # Report the time taken for all this to happen
