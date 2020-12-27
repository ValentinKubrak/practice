# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Valentin Kubrak
# Collaborators : -
# Time spent    : two evenings

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):
    word_length = len(word)
    first_component = 0
    for i in word:
        first_component += SCRABBLE_LETTER_VALUES[i.lower()]
    #Scoring according to the formula
    second_component = (7 * int(word_length)) - (3 * (n - word_length))
    #Choosing which component is bigger
    if second_component>1:
        return first_component * second_component
    else:
        return first_component


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')
    print()                    


def deal_hand(n):
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    #modification:
    hand['*'] = hand.get('*', 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand


def update_hand(hand, word):
    #creating a copy
    new_hand = hand.copy()
    for i in word:
        if i.lower() not in new_hand:
            pass
        #Subtracting the number of letters in the hand
        elif new_hand[i.lower()] > 1:
            k = int(new_hand[i.lower()]) - 1
            new_hand[i.lower()] = k
        elif new_hand[i.lower()] == 1:
            del new_hand[i.lower()]
    return new_hand


def is_valid_word(word, hand, word_list):
    #Replace * with a vowel until a word appears in the list
    if "*" in word:
        for vowel in VOWELS:
            if word.replace("*", vowel) in word_list:
                return True
        else:
            return False
    #if the word does not contain *
    elif word in word_list:
        for i in word:
            if (i not in hand.keys()) or word.count(i) > hand[i]:
                return False
        else:
            return True
    else:
        return False


def calculate_handlen(hand):
    letters = 0
    for i in hand:
        #adding the number of letters
        letters += hand[i]
    return letters    


def play_hand(hand, word_list):
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while len(hand) >= 1:
        # Display the hand
        print('Current Hand: ', end='')
        display_hand(hand)
        # Ask user for input
        user_word = input('Enter word, or “!!” to indicate that you are finished: ')
        # If the input is two exclamation points:
        if user_word == '!!':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_word, hand, word_list):
                # Tell the user how many points the word earned,
                score+=get_word_score(user_word, calculate_handlen(hand))
                # and the updated total score
                print('"'+user_word+'"','earned',get_word_score(user_word, calculate_handlen(hand)),"points. Total:", score, "points")
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                 print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_word)
    # Game is over (user entered '!!' or ran out of letters),
    if user_word == '!!':
    # so tell user the total score
        print("Total score for this hand: ", score, "points\n--------")
    elif len(hand) == 0:
        print('Ran out of letters. Total score:', score, 'points\n--------') 
    # Return the total score as result of function
    return score


def substitute_hand(hand, letter):
    #all letters
    letters = VOWELS + CONSONANTS
    new_hand = hand.copy()
    #deduction of letters that are already in hand
    for i in new_hand.keys():
        letters = letters.replace(i, '')
    if letter in new_hand.keys():
        for i in new_hand.keys():
            #replace the selected letter with a random one
            if letter == i:
                new_hand[random.choice(letters)] = new_hand.pop(i)
                break
    else:
        return False
    return new_hand
       
    
def play_game(word_list):
    while True:
        try:
            hands = int(input('Enter total number of hands: '))
            if hands <= 0:
                print('You entered invalid number of hands, try again')
                continue
        except ValueError:
            print('You entered invalid number of hands, try again')
            continue
        break
    total_score = 0
    limit = 0
    #the function works until the hands run out
    while limit < hands:
        #creating random hand
        hand = deal_hand(HAND_SIZE)
        print('Current Hand: ', end='')
        display_hand(hand)
        #check for correctness of input
        while True:
            substituting = input('Would you like to substitute a letter? ')
            if substituting == 'yes' or substituting == 'no':
                break
            else:
                print('You entered invalid answer')
                continue
        if substituting == 'yes':
            #input subtituting letter and check for correctness of input
            while True:
                letter = input('Which letter would you like to replace: ')
                if substitute_hand(hand,letter):
                    new_hand = substitute_hand(hand,letter)
                    break
                else:
                    print('You entered invalid answer')
                    continue
        elif substituting == 'no':
            new_hand = hand
        #counting points
        total_score += play_hand(new_hand, word_list)
        #replaing and check for correctness of input
        while True:
            replaing = input("Would you like to replay the hand? You will not to get extra points! ")
            if replaing == 'yes' or replaing == 'no':
                break
            else:
                print('You entered invalid answer')
                continue
        #If replaing - yes , the last value of the hand is taken
        if replaing == 'yes':
            play_hand(new_hand, word_list)
        #else: the function starts again
        else:
            hands = hands - 1
            continue
        #if the user has selected replaing
        hands = hands - 1
    print('Total score over all hands:',total_score)


if __name__ == '__main__':
    print("Welcome in game")
    word_list = load_words()
    play_game(word_list)