from string import *

def countSubStringMatch(target, key):
    count = 0
    for x in range(0, len(target)):
        if find(target, key, x) == x:
            count += 1
    return count

def countSubStringMatchRecursiveHelp(target, key, count):
    index = find(target, key)
    if index != -1:
        count += 1
        return countSubStringMatchRecursiveHelp(target[index + 1:len(target)], key, count)
    else:
        return count

def countSubStringMatchRecursive(target, key):
    return countSubStringMatchRecursiveHelp(target, key, 0)

print "iterative solution =", countSubStringMatch("aabaa", "aa")
print "recursive solution =", countSubStringMatchRecursive("aabaa", "aa")
