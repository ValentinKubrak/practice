# Problem Set 2, hangman.py
# Name: Valentin Kubrak
# Collaborators: -
# Time spent: less than 24h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
letters_guessed = []

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i in letters_guessed:
            pass
        else:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    global x
    unknown_secret_words = []
    for i in secret_word:
        if i in letters_guessed:
            unknown_secret_words.append(i)
        else:
            unknown_secret_words.append('_ ')
    x = ''.join(unknown_secret_words)
    return x



def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    for i in letters_guessed:
        all_letters = all_letters.replace(i,'')
    return all_letters
    
    

def hangman(secret_word):
    warnings = 3
    guesses = 6
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word), 'letters long.\nYou have',warnings, 'warnings left.\n______________')
    while True:
        print('You have', guesses, 'guesses left.\nAvailable letters :' + get_available_letters(letters_guessed))
        letter = input('Please guess a letter : ')
        if letter.isalpha() == False or letter != letter.lower() or len(letter) > 1:
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                if guesses <= 0:
                    print('______________\nSorry, you ran out of guesses. The word was', secret_word)
                    break
                print(
                    "Oops! That is not a valid letter. You have no warnings left \nso you lose one guess:" + get_guessed_word(secret_word, letters_guessed), '\n______________')
            else:
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left ',get_guessed_word(secret_word, letters_guessed), '\n______________')
            continue
        elif letter in letters_guessed:
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                if guesses <= 0:
                    print('______________\nSorry, you ran out of guesses. The word was', secret_word)
                    break
                print(
                    "Oops! You've already guessed that letter. You have no warnings left \nso you lose one guess:" + get_guessed_word(secret_word, letters_guessed), '\n______________')
            else:
                print("Oops! You've already guessed that letter."' You have', warnings, 'warnings left ',get_guessed_word(secret_word, letters_guessed), '\n______________')
            continue
        letters_guessed.append(letter)
        if letter in secret_word:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed), '\n______________')
        else:
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed),
                  '\n______________')
        if guesses <= 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            return
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won! Your total score for this game is:", guesses * len(secret_word_set))
            return




def match_with_gaps(my_word, other_word):
    my_word = ' '.join(my_word)
    my_word = my_word.split()
    other_word = ' '.join(other_word)
    other_word = other_word.split()
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(0,len(my_word)):
            if my_word.count(my_word[i]) < other_word.count(other_word[i]):
                return False
            elif my_word[i] == other_word[i]:
                pass
            elif my_word[i] != other_word[i]:
                if my_word[i] == '_':
                    pass
                else:
                    return False
    return True



def show_possible_matches(my_word):
    possible_matches_list = []
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            possible_matches_list.append(i)
        else:
            pass
    print('Possible word matches are: ', end=' ')
    for i in possible_matches_list:
        print(i,end=' ')
    print('\n_________________')




def hangman_with_hints(secret_word):
    secret_word_set = set(secret_word)
    warnings = 3
    guesses = 6
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word), 'letters long.\nYou have',warnings, 'warnings left.\n_________________')
    while True:
        print('\nYou have', guesses, 'guesses left.\nAvailable letters : ' + get_available_letters(letters_guessed))
        letter = input('Please guess a letter : ')
        if letter == '*':
              show_possible_matches(x)
              continue
        elif letter.isalpha() == False or letter != letter.lower() or len(letter) > 1:
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                if guesses <= 0:
                    print('_________________\nSorry, you ran out of guesses. The word was', secret_word)
                    break
                print("Oops! That is not a valid letter. You have no warnings left \nso you lose one guess:" + get_guessed_word(secret_word, letters_guessed), '\n_________________')
            else:
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left ',get_guessed_word(secret_word, letters_guessed), '\n_________________')
            continue
        elif letter in letters_guessed:
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                if guesses <= 0:
                    print('_________________\nSorry, you ran out of guesses. The word was', secret_word)
                    break
                print(
                    "Oops! You've already guessed that letter. You have no warnings left \nso you lose one guess:" + get_guessed_word(secret_word, letters_guessed), '\n_________________')
            else:
                print("Oops! You've already guessed that letter."' You have', warnings, 'warnings left ',get_guessed_word(secret_word, letters_guessed), '\n_________________')
            continue
        letters_guessed.append(letter)
        if letter in secret_word:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed), '\n_________________')
        else:
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed),
                  '\n_________________')
        if guesses <= 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            return
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won! Your total score for this game is:", guesses * len(secret_word_set))
            return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    secret_word_set = set(secret_word)