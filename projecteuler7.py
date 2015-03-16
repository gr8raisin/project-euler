#################################################################################################################
## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.        ##
## What is the 10,001st prime number?                                                                          ##
#################################################################################################################

import time

def is_prime(n): # This number checks if any given input integer is prime or not
    if n == 2 or n == 3: # Edge case for 2 and 3
        return True # Always return true
    if n % 2 == 0 or n % 3 == 0: # If the number is evenly divisible by 2 or 3
        return False # It's not prime
	
	# Don't have to divide the input by every number from 1 to itself (for efficiency)
	# Start with i=5, till (square root of input + 1) in steps of 6
    
	for i in range(5, int(n ** 0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0: # If the input is evenly divisible by i or (i+2)
            return False # It's not prime
    return True # If it gets through the entire thing till here, the number is prime

def main():
   start_time = time.time() # Get the start time
   i=1 # Start with i=1
   primeCount=0 # primeCount will give be the variable that contains the indices of every prime number found
   while True: # Infinite loop
      i+=1 # Increment i by 1
      if is_prime(i): # Check is i is prime
         if primeCount < 10001: # If primeCount is still less than 10,001 (need the 10,001st prime number)
            primeCount+=1 # Increment primeCount by 1
            if primeCount > 10000: # Once primeCount has exceeded 10,000
                print("Prime count: ",primeCount,"| Value: ",i) # Print the 10,001st prime number
         else:
            break # Exit the loop
   print("Execution time: ",(time.time() - start_time)/60," minutes.") # Report the time taken to do this

if __name__ == "__main__": main()