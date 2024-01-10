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

def wordle():
    word = random.choice(FIVE_LETTER_WORDS)
    
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word[col])

    gw.add_enter_listener(enter_action)

def enter_action(s):
    entered_word = s.upper()  # Convert to uppercase
    word = gw.get_word()  # Retrieve the word from the graphics window
    
    if entered_word in FIVE_LETTER_WORDS:
        for col, letter in enumerate(entered_word):
            if letter == word[col]:
                gw.set_square_color(0, col, "#66BB66")  # CORRECT_COLOR
            else:
                # Handle other colors accordingly
                pass  # Placeholder, you need to define the logic for other colors
        gw.show_message("Correct Guess!")
    else:
        gw.show_message("Not in word list")

        # Inside enter_action after coloring the boxes
        for letter in entered_word:
            gw.set_key_color(letter, "#66BB66")  # Update key color for entered letters

# Start-up code
if __name__ == "__main__":
    wordle()
    root = tk.Tk()  # Create a Tkinter root window
    root.mainloop()  # Start the Tkinter event loop
