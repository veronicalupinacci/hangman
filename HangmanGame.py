"""

Hangman game
The program uses tkinter for the GUI.
The user will know how long is the word, has to guess letters of the word (max 4 mistakes)
and then gets 3 chances to guess the word. To play again, the user can press restart.

"""

__author__ = "Veronica Lupinacci"
__version__ = "7/15/2023"

from tkinter import *
import random


def play(): #part of the game used to guess a letter
    global tries, lettersinput, guessed, rightcount, wrong #global values
    global feedback_message
    
    x = e.get() #get input

    
    if len(x) > 1 or not x.isalpha(): #check if input is a letter
        feedback_message.config(text="Please enter only one character, it has to be a letter.")
        return

    feedback_message.config(text=" ")
    x = x.lower() #change input to lowercase
    lettersinput += x + " " #add input to lettersinput
    e.delete(0, "end") #clear entry box

    if x in chosen: #check if input is in the word, if yes then add to guessed 
        feedback_message.config(text="You guessed right!\n")
        guessed += x + " "
    else: #if input not in the word, add to wrong and increment tries
        feedback_message.config(text="Oh no! wrong guess.\n")
        wrong += x + " "
        tries += 1

    message2.config(text="Letters guessed so far: " + str(lettersinput) + "\nRight: " + str(guessed) + "   Wrong: " + str(wrong) + "\n") #tell user what tjhey got wrong and right

    if tries > 4: #check if user got too many wrong
        feedback_message.config(text="GAME OVER.\nToo many tries, the word was: " + chosen)
    else:
        e.focus_set() #ensure that the entry field is the active widget

def guess_word(): #part of the game used to guess the word
    global tries, letterswrong, wordsinput, guessed, rightcount, wrong #global values

    x = e.get() #get input
    wordsinput += x + " " #add input to wordsinput
    e.delete(0, "end") #clear entry box

    if x == chosen: #check if the word guessed is right
        feedback_message.config(text="YOU WON!\nCongratulations, you guessed the word.") #tell the user they won
    else:
        feedback_message.config(text="Oh no! wrong guess.\n") #tell the user they guessed wrong
        tries += 1 #increment tries
        wrongwords += x + " " #add input to wrong

        message2.config(text="Wrong words: " + str(wrongwords) + "Letters guessed so far: " + str(lettersinput) + "\nRight: " + str(guessed) + "   Wrong: " + str(wrong) + "\n")

    if tries > 3: #check if user got too many wrong
        feedback_message.config(text="GAME OVER.\nToo many tries, the word was: " + chosen)
    else:
        e.focus_set() #ensure that the entry field is the active widget

def replay(): #to play the game again
    global tries, lettersinput, letterswrong, guessed, wrong, chosen #global values


    chosen = random.choice(words)
    guessed = ""
    wrong = ""
    letterswrong = ""
    wordsinput = ""
    tries = 0
    lenChosen = str(len(chosen))

    feedback_message.config(text="Guess a letter or the entire word.")
    message1.config(text="The word has " + lenChosen + " letters")
    message2.config(text="Letters guessed so far: " + str(lettersinput) + "\nRight: " + str(guessed) + "   Wrong: " + str(wrong) + "\n")
    e.focus_set() #ensure that the entry field is the active widget
    
words = ["hello", "morning", "day", "toy", "night", "baby", "sun", "bedroom", "pencil", "happy"]
chosen = random.choice(words)

guessed = ""
wrong = ""
wrongwords = ""
lettersinput = ""
wordsinput = ""
tries = 0
lenChosen = str(len(chosen))

root = Tk()
root.geometry("300x250")
root.title("Hangman game")

welcome = Label(root, text="\n  Welcome to the hangman game!\n")
welcome.grid(row=0, column=0, columnspan=2)


message1 = Label(root, text="The word has " + lenChosen + " letters")
message1.grid(row=1, column=0, columnspan=2)

feedback_message = Label(root, text="Guess a letter.")
feedback_message.grid(row=2, column=0, columnspan=2)

e = Entry(root, width=20)
e.grid(row=3, column=0, columnspan=2)
e.focus_set()

enterButton = Button(root, state=NORMAL, text="Enter", command=play)
enterButton.grid(row=4, column=0)

message2 = Label(root, text="Letters guessed so far: " + str(wordsinput) + "\nRight: " + str(guessed) + "   Wrong: " + str(wrong) + "\n")
message2.grid(row=5, column=0, columnspan=2)

guessWordButton = Button(root, state=DISABLED, text = "Guess word")
guessWordButton.grid(row=4, column=1)

replayButton = Button(root, text="Restart", command=replay)
replayButton.grid(row=6, column=0, columnspan=2)

root.mainloop()



