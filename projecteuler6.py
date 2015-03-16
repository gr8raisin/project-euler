#################################################################################################################
## The sum of the squares of the first ten natural numbers is,                                                 ##
## 1^2 + 2^2 + ... + 10^2 = 385                                                                                ##
## The square of the sum of the first ten natural numbers is,                                                  ##
## (1 + 2 + ... + 10)^2 = 55^2 = 3025                                                                          ##
## Hence the difference between the sum of the squares of the first ten natural numbers and the square of the  ##
## sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred       ##
## natural numbers and the square of the sum.                                                                  ##
#################################################################################################################

import time
numList=list(range(1,101)) # Array containing numbers 1-100
tempList=[] # Empty array for use in sumOfSquares() function

def sumOfSquares(inList): # This function calculates the sum of squares of the numbers in any input array
   sumSquares=0 # Initialize sumSquares to zero
   for i in range(0,len(inList)): # Loop through the input array
      tempList.append(pow(inList[i],2)) # Append the square of every element in the input array to the empty array created globally
   for i in range(0,len(tempList)): # Loop through the array containing the squares of all the elements in the input array
      sumSquares+=tempList[i] # Sum them up and store the result in sumSquares
   return sumSquares # Return sumSquares to the calling function

def squareOfSum(inList): # This function calcuates the square of the sum of numbers in any input array
   squareSum=justSum=0 # Initialize these two variables to 0
   for i in range(0,len(inList)): # Loop through the input array
      justSum+=inList[i] # Sum up all elements and store the result in justSum
   squareSum=pow(justSum,2) # squareSum contains the square of the sum
   return squareSum # Return squareSum to the calling function

def main():
   start_time = time.time() # Get the start time
   sumSquares = sumOfSquares(numList) # Call the sumOfSquares function with the input array
   print("Sum of Squares: ",sumSquares) # Print the sum of squares of the elements in the input array
   squareSum = squareOfSum(numList) # Call the squareOfSum function with the input array
   print("Square of Sum: ",squareSum) # Print the square of the sum of elements in the input array
   diff = squareSum - sumSquares # Get the difference between squareSum and sumSquares
   print("Difference: ",diff) # Print the difference
   print("Execution time: ",(time.time() - start_time)/60," minutes.") # Report the time taken for all this to happen

if __name__ == "__main__": main()
