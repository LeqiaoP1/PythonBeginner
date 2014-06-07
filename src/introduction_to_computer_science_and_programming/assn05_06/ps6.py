# Problem Set 6: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

BONUS = 50

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    sum_score = 0
    for letter in word:
        sum_score = sum_score + SCRABBLE_LETTER_VALUES.get(letter,0)

    if len(word) == n:
        sum_score = sum_score + 50

    return sum_score



def get_words_to_points(word_dict):
    """
        Return a dict that maps every word in word_list to its point value.
    """
    ret_dict = word_dict.copy()
    for word in word_dict.keys():
        sum_score = 0
        for letter in word:
            sum_score = sum_score + SCRABBLE_LETTER_VALUES.get(letter,0)


        ret_dict[word][1] = sum_score

    return ret_dict


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print "Current Hand: "
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line

    print

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()
    for letter in word:
        remaining = updated_hand.get(letter, 0) - 1
        if (remaining == 0):
            del updated_hand[letter]
        else:
            updated_hand[letter] = remaining
    
    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    letter_freq = get_frequency_dict(word)
    for letter in letter_freq.keys():
        if ( letter_freq[letter] > hand.get(letter,0) ):
            return False

    if (word in word_list):
        return True
    else:
        return False



def pick_best_word(hand, word_point_dict):
    """
        Return the highest scoring word from points_dict that can be made with the
        given hand.
        Return '.' if no words can be made with the given hand.
    """
    best_word = '.'
    highest_score = 0

    # loop over each word in input dictionary
    for word in word_point_dict.keys():
        # check the word in hand
        word_in_hand = True
        letter_freq = get_frequency_dict(word)
        for letter in letter_freq.keys():
            if ( letter_freq[letter] > hand.get(letter,0) ):
                word_in_hand = False
                continue

        if word_in_hand:
            score = word_point_dict[word][1]

            if len(word) == HAND_SIZE:
                score = score + BONUS

            if highest_score < score:
                highest_score = score  
                best_word = word_point_dict[word][0]
        
    return (best_word, highest_score)
       


def rearrange_dict(word_list):
    d = {}
    for word in word_list:
        d[''.join(sorted(word))] = [word, 0]

    return d


def pick_best_word_faster(hand, rearranged_dict):
    """ Note:
        rearanged_dict: 'sorted_letters':['orig_word', score]
    """
    # get all non-empty subsets frm the letters in hand
    subs = []
    for letter in hand.keys():
        subs.append( list(letter * rep for rep in range(hand[letter]+1)) )
        
    # all possible combinations from hand
    possible_words = []
    for c in itertools.product(*subs):
        if ''.join(c):
            possible_words.append(''.join(c))

    # check over possible words
    best_word = '.'
    highest_score = 0

    for word in possible_words:
        sorted_w = ''.join(sorted(word))
        if sorted_w in rearranged_dict.keys():
            score = rearranged_dict[sorted_w][1]

            if len(sorted_w) == HAND_SIZE:
                score = score + BONUS

            if highest_score < score:
                highest_score = score  
                best_word = rearranged_dict[sorted_w][0]
                
    return (best_word, highest_score)


def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
     points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
        
    end_time = time.time()
    return (end_time - start_time) * k 


#
# Problem #4: Playing a hand
#
def play_hand(hand, word_point_dict, time_limit):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    print "play_hand is started ... "
    final_score = 0
    remained_hand = hand.copy()
    time_remaining = time_limit
    
    while remained_hand and (time_remaining > 0):
        display_hand(remained_hand)
        start_time = time.time()
        #user_input = raw_input("Enter word to score or a '.' to indicate finishing game >")
        #new_input, new_score = pick_best_word(remained_hand, word_point_dict)
        new_input, new_score = pick_best_word_faster(remained_hand, word_point_dict)
        end_time = time.time()
        spent_time = end_time - start_time
        print "It took %.2fs to provide an answer: '%s'" %(spent_time, new_input)
        time_remaining = time_remaining - spent_time
        
        if (new_input != '.'): # continue with another word
            if (time_remaining < 0):
                print "!Timeout (limit %.2fs). Game finished!" %time_limit
                break
            else:
                print "There is %0.2fs remaining for this game." %time_remaining
                #if (is_valid_word(user_input, remained_hand, word_list)):
                #    new_score = get_word_score(user_input, HAND_SIZE)
                final_score = final_score + new_score
                remained_hand = update_hand(remained_hand, new_input)        
                print '** Well done! Earn score: ', new_score
                print '** Now the total score updated to: ', final_score  
                #else:
                #   print '!Invalid word from user input!'
                    
        else: # user stop the game
            break
   
    print "final score is: ", final_score
     


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_point_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    
    #play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    while True:
        time_limit = float(raw_input("Enter time limit,in seconds, for players: "))
        if (time_limit > 0):
            break
    
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_point_dict, time_limit)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_point_dict, time_limit)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    arranged_word_list = rearrange_dict(word_list)
    #word_point_dict = get_words_to_points(word_list)
    word_point_dict = get_words_to_points(arranged_word_list)
    play_game(word_point_dict)
    

