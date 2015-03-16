import time
testArray=list(range(1,21))
counter=0
i=2
start_time = time.time()
while counter != 20:
   for j in range(0,len(testArray)):
      if i%testArray[j]==0:
         counter+=1
      else:
         counter=0
   i+=1
print("Answer: ",i-1)
print("Execution time: ",(time.time() - start_time)/60," minutes.")
