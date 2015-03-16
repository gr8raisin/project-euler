import time

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def main():
   start_time = time.time()
   i=1
   primeCount=0
   while True:
      i+=1
      if is_prime(i):
         if primeCount < 10001:
            primeCount+=1
            if primeCount > 10000:
                print("Prime count: ",primeCount,"| Value: ",i)
         else:
            break
   print("Execution time: ",(time.time() - start_time)/60," minutes.")

if __name__ == "__main__": main()
