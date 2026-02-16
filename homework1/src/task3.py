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
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
            
    return True

while len(primeNums) < 10:
    if is_prime(num):
        primeNums.append(num)
    num += 1


print(primeNums)



# sum of numbers between 1 to 100
sumMax = 100
totalSum = 0

while sumMax != 0:
    totalSum += sumMax
    sumMax -= 1

print(totalSum)