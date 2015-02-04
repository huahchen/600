from math import *
n = raw_input("Enter an integer n: ")
print "n = ",n
primes = []
sum = 0
test = 2
isPrime = True
while test <= float(n):
    for item in primes:
        if test%item == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(test)
        sum += log(test)
    test += 1
    isPrime = True
print "sum of logs = ",sum
ratio = sum / float(n)
print "ratio = ",ratio
