# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "MIT6.0SC_PS02_P2_HangmanWords.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print (str(len(wordlist)) + " words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# displays results from player guess
def resultDisplay(wrongGuessLimit, rightGuessLimit, letter, word, preview, remainingLetters):
    print ("-------------------------------------------------------------------")
    print ("You have " + str(wrongGuessLimit) + " guess(es) left.")
    print ("Letters Remaining: " + convertList(remainingLetters))
    print (str(rightGuessLimit) + " letter(s) left:" + convertList(wordPreview(letter, word, preview)))
    print ("-------------------------------------------------------------------")


#Checks if guessed letter is in target word and returns index of letter in word. 
def checkGuess(letter, word):
    index = word.find(letter)
    return index

def wrongGuess():
    print ("You have incorrectly guessed a letter. Try again.")

def rightGuess():
    print ("You have correctly guessed a letter.")

# checks if you have won the game or not and displays appropriate response.
def gameover(x, y, word):
    if x == 0:
        print ("Sorry, you have lost the game and did not guess the word: " + word)

    elif y == 0:
        print ("You have won the game and correctly guessed the word: " + word)

# converts word into list of equal length with '_' instead of the letters
def wordPreview(letter, word, previewList):
    if len(previewList) == 0:
        for i in range(len(word)):
            previewList.append("_")

    if checkGuess(letter, word) != -1:
        for i,item in enumerate(word):
            if item == letter:
                previewList[i] = letter


    return previewList

#convert list of strings to a string with a space between each list item for easy reading.
def convertList(stringList):
    listString = ""
    for i in range(len(stringList)):
        listString += " "
        listString += stringList[i]

    return listString

# allows for player to input a guess
def playerGuess(guessedLetters):
    guess = input("Guess a letter: ")
    # print ("guess in function: " + guess)
    while (len(guess) >= 2 or guess in guessedLetters or len(guess) <= 0):
        if len(guess) >= 2:
            print ("Sorry you can only guess one letter at a time. Try again.")
            guess = input("Guess a letter: ")
        elif guess in guessedLetters:
            print ("Sorry you have already guessed the letter '" + guess + "'. Try again")
            guess = input("Guess a letter: ")
        elif len(guess) <= 0:   
            print ("Sorry you did not guess a letter. Try again.")
            guess = input("Guess a letter: ")

    return guess.lower()

    


def new_game():
    targetWord = choose_word(wordlist)
    wrongGuessLimit = 8
    rightGuessLimit = len(targetWord)

    targetWordPreview = []
    guessedLetters = ()
    remainingLetters = list(string.ascii_lowercase)

    # print ("Target word: " + targetWord)
    resultDisplay(wrongGuessLimit, rightGuessLimit, "", targetWord, targetWordPreview, remainingLetters)

    while (wrongGuessLimit > 0 and rightGuessLimit > 0):
        guess = playerGuess(guessedLetters)

        if checkGuess(guess, targetWord) != -1:
            rightGuess()
            for i,item in enumerate(targetWord):
                if item == guess:
                    rightGuessLimit -= 1
        else:
            wrongGuess()
            wrongGuessLimit -= 1     

        # print ("guess returned: " + guess)
        remainingLetters.remove(guess)    
        guessedLetters += (guess,)   
        resultDisplay(wrongGuessLimit, rightGuessLimit, guess, targetWord, targetWordPreview, remainingLetters)



    gameover(wrongGuessLimit, rightGuessLimit, targetWord)


startGame = input("Do you want to play hangman? (Y/N) ")

if startGame.lower() == "y" or startGame.lower() == "yes":
    new_game()