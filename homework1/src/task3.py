# see if number possitive, negative or a 0
def pos_neg_zero(myNumber):
    if myNumber == 0:
       return "zero"
    elif myNumber > 0:
        return "positive"
    else:
        return "negative"

print(pos_neg_zero(2))


# first 10 prime numbers
primeNums = []
num = 2

def is_prime(n):
    if n < 2:       #prime numbers MUST start at 2, if not return fallse to move on the next number
        return False
    
    for i in range(2, n):  # in the range from 2 to the n-1
        if n % i == 0:  # if remainder returs as 0, then its not a prime. n MUST be divisible  ONLY by itself and a 1 
            return False
            
    return True # when all number got cycled through, then it must be a prime number

while len(primeNums) < 10:  #array contains less than 10 ellements
    if is_prime(num):       # when a number returns true append it to the array list
        primeNums.append(num)
    num += 1      # move on to the next number


print(primeNums)



# sum of numbers between 1 to 100
sumMax = 100
totalSum = 0

while sumMax != 0:    # when sumMax = 0 then exit loop
    totalSum += sumMax 
    sumMax -= 1

print(totalSum)