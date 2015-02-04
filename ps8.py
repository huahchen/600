# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subjects = {}
    for line in inputFile:
        subject_list = line.split(',')
        subject_list[-1] = subject_list[-1].strip('\n')
        subject_list[1] = int(subject_list[1])
        subject_list[-1] = int(subject_list[-1])
        subjects[subject_list[0]] = subject_list[1:]
    return subjects

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

subjects = loadSubjects(SUBJECT_FILENAME)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    schedule = {}
    subject_keys = subjects.keys()
    work = maxWork

    while len(subject_keys) != 0:
        #finds best class
        bestKey = subject_keys[0]
        for x in subject_keys:
            if comparator(subjects[x], subjects[bestKey]):
                if not x in schedule:
                    bestKey = x
        #tests if there is enough work available, if so adds to schedule
        if work >= subjects[bestKey][1]:
            schedule[bestKey] = subjects[bestKey]
            work = work - subjects[bestKey][1]
        #remove bestKey from subject_keys
        subject_keys.remove(bestKey)
    return schedule
            

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(maxTime):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    total_time = 0
    maxWork = 1
    while total_time < maxTime:
        start_time = time.time()
        bruteForceAdvisor(subjects, maxWork)
        end_time = time.time()
        total_time = end_time - start_time
        maxWork = maxWork + 1
    print maxWork

#bruteForceTime(30)

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    nameList = subjects.keys()
    tupleList = subjects.values()
    m = {}
    bestSubset, bestSubsetValue = \
            dpAdvisorHelper(tupleList, maxWork, len(nameList) - 1, m)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def dpAdvisorHelper(subjects, aW, i, m):
    s = subjects[i]
    try: return m[(i, aW)]
    except KeyError:
        if i == 0:
            if s[WORK] <= aW:
                m[(i, aW)] = [i], s[VALUE]
                return [i], s[VALUE]
            else:
                m[(i, aW)] = [], 0
                return [], 0
        without_i, without_iV = dpAdvisorHelper(subjects, aW, i-1, m)
        if s[WORK] > aW:
            m[(i, aW)] = without_i, without_iV
            return without_i, without_iV
        else:
            with_i, with_iV = dpAdvisorHelper(subjects, aW - s[WORK], i-1, m)
            with_i = with_i + [i]
            with_iV = with_iV + s[VALUE]
        if with_iV >= without_iV:
            bestV = with_iV
            bestSet = with_i
        else:
            bestV = without_iV
            bestSet = without_i
        m[(i, aW)] = bestSet, bestV
        return bestSet, bestV

def dpAdvisorHelperOld(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork, m):
    # Have I already computed this case?
    try: 
        #print i, subsetWork
        return m[(i, subsetWork)]
    except KeyError:
        # Hit the end of the list.
        if i >= len(subjects):
            if bestSubset == None or subsetValue > bestSubsetValue:
                # Found a new best.
                m[(i, subsetWork)] = subset[:], subsetValue
                #print subjects[i]
                print subset[:], subsetValue
                return subset[:], subsetValue
            else:
                # Keep the current best.
                m[(i, subsetWork)] = bestSubset, bestSubsetValue
                print "here"
                return bestSubset, bestSubsetValue
        else:
            s = subjects[i]
            bestSubsetValueWith = 0
            # Try including subjects[i] in the current working subset.
            bestSubsetWithout, bestSubsetValueWithout = dpAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue, subsetWork, m)
            if subsetWork + s[WORK] <= maxWork:
                subset.append(i)
                bestSubsetWith, bestSubsetValueWith = dpAdvisorHelper(subjects,
                        maxWork, i+1, bestSubset, bestSubsetValue, subset,
                        subsetValue + s[VALUE], subsetWork + s[WORK], m)
                print subjects[i], subsetWork + s[WORK], bestSubset, bestSubsetValue, subsetValue, s[VALUE]
                subset.pop()
            if bestSubsetValueWithout >= bestSubsetValueWith:
                bestSubset = bestSubsetWithout
                bestSubsetValue = bestSubsetValueWithout
            else:
                bestSubset = bestSubsetWith
                bestSubsetValue = bestSubsetValueWith
            m[(i, subsetWork)] = bestSubset, bestSubsetValue
            return bestSubset, bestSubsetValue

printSubjects(dpAdvisor(subjects, 30))

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    total_time = 0
    maxWork = 1
    while total_time < maxTime:
        start_time = time.time()
        dpAdvisor(subjects, maxWork)
        end_time = time.time()
        total_time = end_time - start_time
        maxWork = maxWork + 1
    print maxWork




# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
