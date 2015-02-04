from string import *

def subStringMatchExact(target, key):
    tup = ()
    for x in range(0, len(target)):
        if find(target, key, x) == x:
            tup += (x,)
    return tup

print subStringMatchExact("aabaa","aa")
print subStringMatchExact("aaaa","aa")
