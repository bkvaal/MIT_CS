# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens> (AND BOB KVAAL)
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 8

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

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
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO...
    word_score = 0
    for letter in word:
        score = SCRABBLE_LETTER_VALUES[letter]
        word_score += score
        ## print letter, score
    length = len(word)
    word_score *= length
    if length > n: word_score = 0  #check for bad data
    elif length == n: word_score += 50
    return word_score
        
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
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

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

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    

    for letter in word:
        hand[letter] -= 1
        if hand[letter] == 0:
            hand.pop(letter)
##        print 'HAND2', hand
    return hand    


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
    # TO DO...
    list_match = True
    hand_match = True
    if word_list.count(word) == 0:  #see if word is in word_list
        list_match = False

    hand2 = hand.copy()             #hand2 is version used here so as to not change hand
    try:
        for letter in word:
##            print word, letter, hand2
            if hand2[letter] > 0:   #see if hand2 has all letters in word
                hand2[letter] -= 1
            else:
                hand_match = False
    except: hand_match = False   
##    return list_match, hand_match     # this statement shows results of both tests
    return (list_match and hand_match)  # use this statement to comply with exact specs

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """

# TO DO ...
    score = 0
    total_score = 0
    t = False
    while t == False:
        display_hand(hand)
        user_word = raw_input("please enter your word (or '.' to quit) : ")
        if user_word != '.':
            t = is_valid_word(user_word, hand, word_list)
            if t:
                score = get_word_score(user_word,HAND_SIZE)
                total_score += score
                print user_word, 'is valid, score is ', score
                
                update_hand(hand, user_word)
                if hand:
##                    print 'Remaining hand is '
##                    display_hand(hand)
                    t = False
                else:
                    print 'Total Score was', total_score
                    return total_score
   
            else: print 'Sorry, invalid word, please try again'  
        else:
            print 'Your total score was ', total_score
            return total_score

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO...

    total_score = 0
    while True:
        command = raw_input("please type 'n' for new, 'r' for replay or 'e' for exit: ") 
        if command == 'e':
            if total_score:
                print 'total score for this game was ', total_score
            return                    
        elif command == 'n':
            hand = deal_hand(HAND_SIZE)
            repeat_hand = hand.copy()
##            print ' in n, HAND, REPEAT_HAND', hand, repeat_hand
            play_hand(hand, word_list)
        elif command == 'r':
            hand = repeat_hand.copy()
            play_hand(hand, word_list)
        else: break
        
        
##        print score, total_score
##        total_score += score
##        print 'Total score was ', total_score
                            
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    
    word_list = load_words()

# TESTING SUITES
##    print 'Now beginning test of functions'
### Test word_score 
##    benchmark = ('now', 1, 0, 'now', 2, 0, 'now', 3, 68, 'now', 4, 18, 'now', 5, 18, 'now', 6, 18, 'now', 7, 18, 'is', 1, 0, 'is', 2, 54, 'is', 3, 4, 'is', 4, 4, 'is', 5, 4, 'is', 6, 4, 'is', 7, 4, '', 1, 0, '', 2, 0, '', 3, 0, '', 4, 0, '', 5, 0, '', 6, 0, '', 7, 0, 'time', 1, 0, 'time', 2, 0, 'time', 3, 0, 'time', 4, 74, 'time', 5, 24, 'time', 6, 24, 'time', 7, 24, 'country', 1, 0, 'country', 2, 0, 'country', 3, 0, 'country', 4, 0, 'country', 5, 0, 'country', 6, 0, 'country', 7, 134, 'venezuela', 1, 0, 'venezuela', 2, 0, 'venezuela', 3, 0, 'venezuela', 4, 0, 'venezuela', 5, 0, 'venezuela', 6, 0, 'venezuela', 7, 0)
##    
##    test_word_score = ()
##    for word in ('now', 'is', '', 'time', 'country', 'venezuela'):
##        for n in range (1,8):          
##            s = get_word_score(word,n)
##            test_word_score += (word,n,s)
####            print word, n, test_word_score
####    print 'Benchmark ', benchmark
##       
##    if test_word_score == benchmark:
##        print 'Successful test of word_score'
##    else: print "Test of word_score failed"       
##    play_game(word_list)
##
##      
### Test update_hand
##    words = ('most', 'ok', 'men', 'country', 'columbia','name', 'name', 'able', 'produce')
##    hands = ({'t':1,'u':1,'v':2,'o':1,'m':4,'s':1},{'u':2, 'b':3, 'k':1, 's':3, 't':1, 'o':1, 'd':3},
##             {'n':2, 'a':3, 'e':2, 'm':3}, {'y':1, 'r':2, 't':1, 'n':3, 'u':1, 'o':2, 'c':1},
##             {'c':1,'l':2,'m':1, 'i':2, 'o':2, 'u':1, 'b':1, 'a':1},{'t':1,'u':1,'v':2,'o':1,'m':4,'s':1},{'u':2, 'b':3, 'k':1, 's':3, 't':1, 'o':1, 'd':3},
##             {'n':2, 'a':3, 'e':2, 'm':3}, {'y':1, 'r':2, 't':1, 'n':3, 'u':1, 'o':2, 'c':1},
##             {'c':1,'l':2,'m':1, 'i':2, 'o':2, 'u':1, 'b':1, 'a':1})
####    print 'hands before update_hand'
####    print hands
##    all_hands = {}
##    baseline = {'a': 3, 'b': 3, 'e': 1, 'd': 3, 'i': 1, 'm': 2, 'l': 1, 'o': 1, 'n': 2, 's': 3, 'r': 1, 'u': 2, 't': 1, 'v': 2}
##    {'a': 3, 'b': 3, 'e': 1, 'd': 3, 'i': 1, 'm': 2, 'l': 1, 'o': 1, 'n': 2, 's': 3, 'r': 1, 'u': 2, 't': 1, 'v': 2}
##    for i in range (0,5):
####        print 'Original word and hand', words[i], hands[i]
####        word = words[i]
##        this_hand = hands[i].copy()   # copy so not to change hands
####        print 'This Hand ', this_hand
##        new_hand = update_hand(this_hand,words[i])
##        all_hands.update(new_hand)   
####        print 'Hand After processing', new_hand
####        print
####    print 'Baseline             ', baseline
####    print 'All Hands            ', all_hands
##    if all_hands == baseline:
##        print 'Successful test of update_hand'
####        print 'hands after update_hands'
####        print hands  
##    else: print 'update_hand test failed'    
##            
##
### Test is_valid_word
####    print word_list
##    fails = []
##    goods = []
##    
##    for i in range (0,9):  #run tests for sets of words and hands
##        word = words[i]
##        this_hand = hands[i]        
##        t = is_valid_word(word, this_hand, word_list) ##change to match single variable return
##   
####        if t[0] and t[1]:   #t[0] is word_list, t[1] is hand
####            goods.append((word, t[0], t[1]))
####        else:
####            fails.append((word, t[0], t[1]))
##
##        if t: goods.append(word)
##        else: fails.append(word)
##        
##
####    print 'good words are:  ', goods
####    print 'failed words are:', fails       
##
####    word = 'name' #test additional word
####    t = is_valid_word(word ,hands[2], word_list)
####    if t[0] and t[1]:
####        goods.append(word)          
####    else:
####        fails.append(word)
####    t = is_valid_word(word, hands[2], word_list) #try same word second time
####    if t[0] and t[1]:
####        goods.append(word)          
####    else:
####        fails.append(word)
##
####    if goods == [('most', True, True), ('men', True, True), ('country', True, True)] and\
####        fails == [('ok', False, True), ('columbia', False, True), ('name', True, False), ('name', True, False), ('able', True, False), ('produce', True, False)]:
####    print goods, fails     
##    if goods == ['most', 'men', 'country'] and fails == ['ok', 'columbia', 'name', 'name', 'able', 'produce']:
##        print 'Successful test of is_valid_word'     
##    else: print  'is_valid_word failed test'    
##
##### Test play_hand
####    for i in range (0,5):
####        word = words[i]
####        this_hand = hands[i]
####        test = play_hand(this_hand, word_list)
####        if test: print 'Valid word, matches letters in your hand'

# Test play_game
    play_game(word_list)



            
