# 🧩 Problem Set 3

## Introduction

This problem set, "Wordgames," is designed to challenge you in implementing the 6.00 wordgame using Python. The game is similar to Scrabble or Text Twist, where players are dealt a hand of random letters and must construct words from them to earn scores. Each valid word is scored based on the letters it contains and its length. The rules are well-defined, and the game is highly enjoyable.

**Please note that the descriptions provided here are not exhaustive** and are intended to give you an overview of the tasks at hand. To get a full understanding of the problem and successfully complete this problem set, **carefully read and follow the complete project instructions** provided in the respective Python files (ps3a.py and ps3b.py).

## Problem 1: Word Scores

The first task is to implement the `get_word_score` function, which calculates the score for a given word according to the game's scoring rules. The score for a word is the sum of the points for the letters in the word, multiplied by the length of the word. Additionally, if all the letters from the player's hand are used in the first go, a bonus of 50 points is awarded.

## Problem 2: Dealing with Hands

In this part, you will work with hands represented as dictionaries, where keys are lowercase letters, and values are the number of occurrences of each letter. The goal is to implement the `update_hand` function that takes a word and a hand and returns a new hand after using up the letters to spell the word.

## Problem 3: Valid Words

The next step is to implement the `is_valid_word` function, which checks if a word is valid according to the game's rules. A valid word should be in the word list and composed entirely of letters from the current hand.

## Problem 4: Playing a Hand

In Part A, you will implement the `play_hand` function, which allows a human player to play the game interactively. The hand will be displayed, and the player can input words until the hand is exhausted or they decide to end the game.

## Problem 5: Playing a Game

The `play_game` function in Part B allows the user to play an arbitrary number of hands. The user can choose to play a new hand, replay the last hand, or exit the game. Additionally, the user can choose to play the game as a human player or let the computer play using the `comp_play_hand` function.

## Problem 6: Computer Word Choose

In Part B, you will create functions to allow the computer to choose a word intelligently. The computer will use permutations to find all possible valid words that can be created from the current hand and select the best one based on score.

## Problem 7: Computer's Turn to Play a Hand

Similar to Part A's `play_hand` function, you will implement the `comp_play_hand` function, which allows the computer to play the game through completion. The computer will choose words intelligently and display the score and remaining letters after each turn.

## Problem 8: U & Ur Computer

Finally, you will modify the `play_game` function to give the user the option to play as either a human or let the computer play the game using the `comp_play_hand` function.

Remember that the provided descriptions are not exhaustive, and **to get a full understanding of the problem**, carefully read and follow the complete project instructions provided in the respective Python files (ps3a.py and ps3b.py). Enjoy the challenge, and have fun building the 6.00 wordgame!

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).