primes = []
test = 2
count = 0
while len(primes) < 1000:
    for item in primes:
        if test%item == 0:
            count += 1
    if count == 0:
        primes.append(test)
    count = 0
    test += 1
print primes[-1]
