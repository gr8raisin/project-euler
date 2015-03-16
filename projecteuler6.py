import time
numList=list(range(1,101))
tempList=[]

def sumOfSquares(inList):
   sumSquares=0
   for i in range(0,len(inList)):
      tempList.append(pow(inList[i],2))
   for i in range(0,len(tempList)):
      sumSquares+=tempList[i]
   return sumSquares

def squareOfSum(inList):
   squareSum=justSum=0
   for i in range(0,len(inList)):
      justSum+=inList[i]
   squareSum=pow(justSum,2)
   return squareSum

def main():
   start_time = time.time()
   sumSquares = sumOfSquares(numList)
   print("Sum of Squares: ",sumSquares)
   squareSum = squareOfSum(numList)
   print("Square of Sum: ",squareSum)
   diff = squareSum - sumSquares
   print("Difference: ",diff)
   print("Execution time: ",(time.time() - start_time)/60," minutes.")

if __name__ == "__main__": main()
