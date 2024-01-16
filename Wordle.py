# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
401 Group 6 Mitch Brammer, Chris Fowler, Abe Lamoreaux, Rachel Yorke
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
import tkinter as tk

# Startup code
gw = WordleGWindow()
the_word = random.choice(FIVE_LETTER_WORDS).upper()
current_row = 0

def wordle():    
    gw.add_enter_listener(enter_action)

def enter_action(entered_word):
    # for col in range(N_COLS):
    #     entered_word += gw.get_square_letter(0, col)

    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, entered_word[col])
    global the_word, current_row
    word = the_word.upper()
    entered_word = entered_word.upper()

    if entered_word.lower() in FIVE_LETTER_WORDS:
        #Color Functionality
        for col, letter in enumerate(entered_word):
            if letter == word[col]:
                gw.set_square_color(current_row, col, '#66BB66')
                gw.set_key_color(letter, '#66BB66')
            elif letter in word:
                gw.set_square_color(current_row, col, '#CCBB66')
                gw.set_key_color(letter, '#CCBB66')
            else:
                gw.set_square_color(current_row, col, '#999999')
                gw.set_key_color(letter, '#999999')
                
        gw.show_message("Valid Try")


        

        #Check if the word is correct - (Not working yet)
        if entered_word == word:
            gw.show_message("Congratulations! You guessed the word.")

    

    #Backspace functionality - (Not working Yet)
    elif entered_word == "":
        gw.show_message("")
        if current_row > 0 and current_row < N_ROWS:
            current_row -= 1
            gw.set_current_row(current_row)
            gw.set_col(N_COLS - 1)
    
    else:
        gw.show_message("Not a valid word")
        current_row -= 1


    current_row += 1
    gw.set_current_row(current_row)
    gw.set_the_word(random.choice(FIVE_LETTER_WORDS).upper())

if __name__ == "__main__":
    wordle()
    root = tk.Tk()
    root.mainloop()
