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


def play_ghost():
    """ play ghost game """

    _PLAYERS = ['Player1', 'Player2']

    def _prompt_for_one_more_letter(input_word, player_idx):
        print "Word record now as: ", input_word
        player = _PLAYERS[play_idx]
        
        while True:
            letter = raw_input(player + ' is appending one letter >')
            if (len(letter) > 0):
                    break
        
        return input_word + letter[0]


    def _check_lose_rule(input_word):
        if (len(input_word) > 3) and (input_word in wordlist):
            return True
        else:
            for word in wordlist:
                if word.startswith(input_word):
                    return False

            return True

    

    # initial contiditon
    input_word = ""
    play_idx = 0
    continue_play = True

    while (continue_play):
        input_word = _prompt_for_one_more_letter(input_word, play_idx)
        if (_check_lose_rule(input_word) == True):
            print _PLAYERS[play_idx] + ' has lost the game.'
            if (raw_input("continue with another game? y or n >") == 'y'):
                continue_play = True
                input_word = ""
                play_idx = 0
            else:
                continue_play = False
        else:
            play_idx = (play_idx + 1)%(len(_PLAYERS))


