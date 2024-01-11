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

def wordle():    
    gw.add_enter_listener(enter_action)

def enter_action():
    entered_word = ''
    for col in range(N_COLS):
        entered_word += gw.get_square_letter(0, col)

    for col in range(N_COLS):
        gw.set_square_letter(0, col, entered_word[col])
        
    word = the_word.upper()
    entered_word = entered_word.upper()

    if entered_word.lower() in FIVE_LETTER_WORDS:
        for col, letter in enumerate(entered_word):
            if letter == word[col]:
                gw.set_square_color(0, col, '#66BB66')
        gw.show_message("Correct Guess!")
    else:
        gw.show_message("Not in word list")

# Start-up code
if __name__ == "__main__":
    wordle()
    root = tk.Tk()  # Create a Tkinter root window
    root.mainloop()  # Start the Tkinter event loop
