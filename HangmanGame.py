"""
Hangman game
The user will know how long is the word,
has to guess letters of the word
and then gets one chance to guess the word.
"""

__author__ = "Veronica Lupinacci"
__version__ = "6/27/2023"

import random

def only_char(x): #function to check if the input is a character only, part of the alphabet and change it to lowercase
    
    while x.isalpha() != True or len(x) > 1:
        print ("Please enter only one character, it has to be a letter.")
        x = input()

    return x.lower()

words = ["hello", "morning", "day", "toy", "night", "baby", "sun", "bedroom", "pencil", "happy"] #list of possdible words
chosen = random.choice(words) #pick a random word

guessed = "" #string for right letters
wrong = "" #string for wrong letters
wordsinput = "" #string for all letters already input
rightcount = 0 #counter for guessed letters
tries = 0 #counter for tries, counts only wrong entries


print("The word has", len(chosen), "letters") #tell the user how many characters has the word


while rightcount < len(chosen) and tries <= 4 : #while loop until all letters in the word are guessed
    print("Guess a letter") #get user input
    x = input()
    checked_input = only_char(x) #save in a new variable the result of the only_char function

    wordsinput = wordsinput + checked_input + " " #add word to input string

    if checked_input in chosen: #check if the user guessed right
        print ("Good job! You guessed right.\n")
        guessed += checked_input + " "#add word to guessed string
        rightcount+=1 #increment counter

    else: #if the user is wrong
        print ("Oh no! wrong guess.\n")
        tries += 1 #increment tries counter
        wrong += checked_input + " "#add word to wrong string

    print ("Letters guessed so far:", wordsinput, "\nRight:", guessed, "   Wrong:", wrong, "\n") #output message to tell the user guessed, wrong and allinput letters

if tries > 4 : #check if the while loop was exited because the user lost 
    print("GAME OVER \nToo many tries, the word was:", chosen)
else: #else, continue the game
    tries = 0 #reset tries counter
    check = False #variable to check if the answer is right or wrong

    #output message to tell the user that all words were guessed and what are those.
    #Then tell the user to guess the full word
    print ("All letters of the word are guessed! \nLetters:", guessed, "\n\nNow guess the word (NOTE the letters could appear more than once) : ")
    x = input()
        
    while check == False and tries <= 3 : #start while lop
        if x == chosen: #check if input equals to chosen word
            check = True #set check variable to True
            
        else: #if guessed wrong, tell the user they lost
            check = False
            tries += 1 #increment tries counter
            print ("Oh no! Guess again")
            x = input()
    #check if user won or lost
    if check == True: 
        print("YOU WON!")
    else:
        print("GAME OVER.\nToo many tries, the word was:", chosen)

#end message
print("Thank you for playing!")

        
