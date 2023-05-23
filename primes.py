import math
#checks if the given number is prime, and if so appends it to the list
def primeCheck(num:int,primes: list):
    if (num % 2 != 0 and num % 3 != 0):
        #previusly discovered prime divisibility check
        for x in primes:
            if (num % x == 0):
                return
        primes.append(num)
#finds all prime numbers in specific range
def findPrimeNums(lowerBound: int, upperBound: int) -> list:
    primes = []
    step = 1
    #+1 because range is not inclusive of it's upperbound
    for num in range(lowerBound, upperBound+1,step):
        if(num == 2 or num == 3):
            primes.append(num)
        else:
            primeCheck(num,primes)
        step = int(math.sqrt(num))
    print(primes)
    return primes

#guards the script from running when being imported
#this part after the if will only trigger if this script is being executed directly
if __name__ == "__main__":
    print("This program finds the prime numbers in the specified range starting at 2")
    #hard coded lowerbound, since previosuly discovered primes are use to validate new prime candiates
    lb = 2

    #input safeguard loop for upper bound
    while True:
        try:
            up = int(input(
                "Please enter a number(integer value of 2 or greater) for the upper bound: "))
            if (up < lb):
                print("upper bound should be an integer value greater than lower bound")
                raise Exception(
                    "upper bound should be an integer value greater than lower bound")
            break
        except:
            print("Not a valid option!")
            
    findPrimeNums(lb,up)

