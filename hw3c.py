from string import *

def subStringMatchExact(target, key):
    tup = ()
    for x in range(0, len(target)):
        if find(target, key, x) == x:
            tup += (x,)
    return tup

def constrainedMatchPair(firstMatch, secondMatch, length):
    tup = ()
    for x in firstMatch:
        for y in secondMatch:
            if x + length + 1 = y:
                tup += (x,)
    return tup

print subStringMatchExact("aabaa","aa")
print subStringMatchExact("aaaa","aa")
