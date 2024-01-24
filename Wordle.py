# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
401 Group 6 Mitch Brammer, Chris Fowler, Abe Lamoreaux, Rachel Yorke
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
import tkinter as tk

# Startup code (Creates Wordle Window, randomly selects a 5 letter word from the word list file, and sets the current row of the grid to 0)
gw = WordleGWindow()
word = random.choice(FIVE_LETTER_WORDS).upper()
current_row = 0

# The Wordle function, which is called when the program starts running
def wordle():  
    # Adds a function that is called when the enter key is pushed  
    gw.add_enter_listener(enter_action)

# This code describes what will happen when the enter key is pushed. First, the parameter it receives is the word entered into the current row of the Wordle grid
def enter_action(entered_word):
    # Ensures that the_word and the current_row variables previously defined do not change 
    global word, current_row

    # Checks to see if the word entered by the user is in the list of valid words
    if entered_word.lower() in FIVE_LETTER_WORDS:
        word_copy = list(word[:])
        entered_word_copy = list(entered_word[:])
        # Color Functionality based on letters in the randomly selected word

        # Goes through the entered_word and checks for exact matches. Replaces correct letter with '*' if there are more than one of that letter in the entered word
        for col, letter in enumerate(entered_word_copy):
            if letter == word_copy[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)

                word_copy[col] = '*'
                entered_word_copy[col] = '*'
        for col, letter in enumerate(entered_word_copy):
            if letter in word_copy and letter != '*':
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                gw.set_key_color(letter, PRESENT_COLOR)

                for col, char in enumerate(word_copy):
                    if (char == letter):
                        word_copy[word_copy.index(letter)] = '*'
            elif letter != '*':
                gw.set_square_color(current_row, col, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)
    
        # Check if the word is correct. If it is, displays a message telling them they guessed the word.
        if entered_word == word:
            gw.show_message("Congratulations! You guessed the word.")
                
        # If the word isn't correct, says "Valid Try" and moves them down to the next row (carries over the word as well)
        else:
            # gw.show_message("Valid Try")
            if current_row < N_ROWS - 1:
                current_row += 1
                gw.set_current_row(current_row)
            else:
                gw.show_message("Better luck next time! The word was: " + word.upper())

    # If the word entered is not in the list of valid words, gives an error message and clears the row for them to try again
    else:
        gw.show_message("Not a valid word")
        current_row -= 1
        current_row += 1
        gw.set_current_row(current_row)
        gw.set_col(N_COLS - 1)

# If the script is the main program, it calls the wordle function and runs the GUI application using tk and then starts listening for user input using the keyboard
if __name__ == "__main__":
    wordle()
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    gw._root.focus_force()
    root.mainloop()