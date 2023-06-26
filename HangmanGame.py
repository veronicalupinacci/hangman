"""
Hangman game
The user will know how long is the word,
has to guess letters of the word
and then gets one chance to guess the word.
"""

__author__ = "Veronica"
__version__ = "6/26/2023"

import random

words = ["hello", "morning", "day", "toy", "night", "baby", "sun", "bedroom", "pencil", "highlighter"] #list of possdible words
chosen = random.choice(words) #pick a random word

guessed = "" #string for right letters
wrong = "" #string for wrong letters
wordsinput = "" #string for all letters already input
rightcount = 0 #counter for guessed letters


print("The word has", len(chosen), "letters") #tell the user how many characters has the word


while rightcount < len(chosen): #while loop until all letters in the word are guessed
    print("Guess a letter") #get user input
    x = input()
    
    if x in chosen: #check if the user guessed right
        print ("Good job! You guessed right.\n")
        guessed += x + " "#add word to guessed string
        wordsinput+= x + " " #add word to input string
        rightcount+=1 #increment counter
        print ("Letters guessed so far:", wordsinput, "\nRight:", guessed, "   Wrong:", wrong, "\n") #output message to tell the user guessed, wrong and all input letters 

    else: #if the user is wrong
        print ("Oh no! wrong guess.\n")
        wrong += x + " "#add word to wrong string

        print ("Letters guessed so far:", wordsinput, "\nRight:", guessed, "   Wrong:", wrong, "\n") #output message to tell the user guessed, wrong and all input letters 

   
#output message to tell the user that all words were guessed and what are those.
#Then tell the user to guess the full word
print ("All letters of the letters are guessed! \nLetters:", guessed, "\n\nNow guess the word (NOTE the letters could appear more than once) : ")
x = input()

if x == chosen: #if guessed right, tell the user they won
    print("You won!")
    
else: #if guessed wrong, tell the user they lost
    print ("Oh no! wrong guess. Game over.")

    
