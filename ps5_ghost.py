# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def is_word(word):
    """
    Returns False if word is 3 letters or shorter
    Returns True if word is found in wordlist
    Returns False if word is not found in wordlist
    """
    if len(word) < 4:
        return False
    else:
        for x in wordlist:
            if word == x:
                return True
        return False

def is_valid_prefix(word):
    for x in wordlist:
        for y in range(0, len(word)):
            if len(x) < len(word):
                break
            if word[y] != x[y]:
                break
            if y == len(word) - 1:
                return True
    return False

def ghost():
    print "Welcome to Ghost!"
    gameEnd = False
    player = 2
    word = ""
    
    while gameEnd == False:
        player = (player % 2) + 1
        print "Player " + str(player) + "'s turn."
        print "Current word fragment: '" + word + "'"
        letter = raw_input("Please enter a letter: ")
        word = word + string.lower(letter)
        if is_word(word):
            gameEnd = True
            print "Player" + str(player) + " loses because" + word + "is a word!"
            print "Player" + str((player % 2) + 1) + " wins!"
            break
        if is_valid_prefix(word) == False:
            gameEnd = True
            print "Player" + str(player) + " loses because no word begins with " 
                + word + "!"
            print "Player" + str((player % 2) + 1) + " wins!"
            break

# TESTS
ghost()
#print is_valid_prefix("worz",wordlist)
