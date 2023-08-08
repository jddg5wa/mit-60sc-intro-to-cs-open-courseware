from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
# 
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO... 
    word = ''
    wordLength = HAND_SIZE

    print ("Computer choosing word...")
    while (word == '' and wordLength > 0):
    	permutations = get_perms(hand, wordLength) 
    	for x in range(len(permutations)):
    		if is_valid_word(permutations[x], hand, word_list): 
    			print (permutations[x]) 
    			return permutations[x]
    	wordLength -= 1






#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    totalScore = 0
    wordScore = 0
    playedHand = hand.copy()

    while((len)(playedHand) > 0):
    	print ("--------------------------------------------------------------------")
    	print ("Current Hand: " + display_hand(playedHand))
    	word = comp_choose_word(playedHand, word_list)
    	print ("Computer chose '" + word.lower() + "'")
    	wordScore = get_word_score(word.lower(), HAND_SIZE)
    	totalScore+= wordScore
    	playedHand = update_hand(playedHand, word.lower())
    	print ( "Computer earned " + str(wordScore) + " points with '" + word + "'. Total: " + str(totalScore))
    	playedHand.clear()
    	print ("Game over. Total Score: " + str(totalScore))
    	return

#
# Problem #6C: Playing a game
#
#
def play_game_computer(word_list, previousHand):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.
 
    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO... 
    hand = {}
    gameCommand = ''
    handChosen = False
    playerChosen = False
 
    while (handChosen == False):
        print("--------------------------------------------------------------------")
        print ("'n' for a NEW hand")
        print ("'r' for the PREVIOUS hand")
        print ("'e' to EXIT the game")
        gameCommand = input("Type your command: ")

        if gameCommand.lower() == 'n':
            hand = deal_hand(HAND_SIZE)
            handChosen = True
        elif gameCommand.lower() == 'r' and len(previousHand) != 0:
            hand = previousHand
            handChosen = True
        elif gameCommand.lower() == 'r' and len(previousHand) == 0:
            print ("No previous hand to play, dealing new hand.")
            hand = deal_hand(HAND_SIZE)
            handChosen = True
        elif gameCommand.lower() == 'e':
        	sys.exit()

    while (playerChosen == False):
        print("--------------------------------------------------------------------")
        print ("'u' for HUMAN player")
        print ("'c' for COMPUTER player")
        gameCommand = input("Type your command: ")
        if gameCommand == 'c':
        	comp_play_hand(hand, word_list)
        	playerChosen = True
        elif gameCommand == 'u':
            play_hand(hand, word_list)
            playerChosen = True

    play_game_computer(word_list, hand)

        
#
# Build data structures used for entire session and play game
#


if __name__ == '__main__':
    word_list = load_words()
    play_game_computer(word_list, {})

    
