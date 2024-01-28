# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
401 Group 6 - Mitch Brammer, Chris Fowler, Abe Lamoreaux, Rachel Yorke
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, COLORBLIND_CORRECT_COLOR
import tkinter as tk

# Radio popup to select difficulty
def show_radio_options():
    root = tk.Tk()
    root.withdraw()
    result_var = tk.IntVar()
    colorblind_var = tk.IntVar()

    # When user clicks ok, ends popup
    def on_ok():
        result_var.set(var.get())
        colorblind_var.set(cb_var.get())
        popup.destroy()

    popup = tk.Toplevel(root)
    popup.title("Options")
    popup.geometry("225x110")
    var = tk.IntVar()
    cb_var = tk.IntVar()
    options = [("Normal Mode", 1), ("Hard Mode", 2)]

    for text, value in options:
        tk.Radiobutton(popup, text=text, variable=var, value=value).pack(anchor="w")
    
    tk.Checkbutton(popup, text="Color Blind?", variable=cb_var).pack(anchor="w")

    # OK Button
    tk.Button(popup, text="OK", command=on_ok).pack()
    popup.wait_window()

    # Returns option selected
    return [result_var.get(), colorblind_var.get()]

# Checks that letters in correct_letter_list are used (in the correct spots)
def checkForLetters(entered_word, correct_letter_list, present_letter_list, requirementsMet):
    for col, _ in enumerate(entered_word):
        if (entered_word[col] != correct_letter_list[col] and correct_letter_list[col] != ''):
            requirementsMet = False
    
    # Ensures letters in present letter list are used and correct count of each letter
    for letter in present_letter_list:
        if (letter not in entered_word or (entered_word.count(letter) < (present_letter_list.count(letter) + correct_letter_list.count(letter)))):
            requirementsMet = False

    # Returns false if letters aren't in the correct position
    return requirementsMet

# Sets random 5 letter word and tracks current row in grid
word = random.choice(FIVE_LETTER_WORDS).upper()
current_row = 0

def wordle(mode):  
    # Blank strings to hold letters when correct ones are found (HARD MODE)
    correct_letter_list = ['', '', '', '', ''] 
    present_letter_list = [] 

    # Enter key funtion, passes the word the user entered
    def enter_action(entered_word):
        global word, current_row

        # NORMAL MODE
        if mode == 1:
            # Checks to see if its a word in the list
            if (entered_word.lower() in FIVE_LETTER_WORDS):
                # Creates copies of the word and users word (as lists)
                word_copy = list(word[:])
                entered_word_copy = list(entered_word[:])

                # CORRECT COLOR
                for col, letter in enumerate(entered_word_copy):
                    if (letter == word_copy[col]):
                        gw.set_square_color(current_row, col, correct_color)
                        gw.set_key_color(letter, correct_color)

                        # Replaces letter with * to track multiple instances of the same letters
                        word_copy[col] = '*'
                        entered_word_copy[col] = '*'
                
                for col, letter in enumerate(entered_word_copy):
                    # PRESENT COLOR
                    if (letter in word_copy and letter != '*'):
                        gw.set_square_color(current_row, col, PRESENT_COLOR)

                        if (gw.get_key_color(letter) != correct_color):
                            gw.set_key_color(letter, PRESENT_COLOR)

                        # Exits the loop after this code once one letter is changed (for multiple instances of the same letters)
                        exit_loop = False

                        # Finds a match in the word and replaces with * (for multiple instances of the same letters)
                        for col, char in enumerate(word_copy):
                            if (char == letter and exit_loop == False):
                                word_copy[word_copy.index(letter)] = '*'
                                exit_loop = True

                    # MISSING COLOR
                    elif (letter != '*'):
                        gw.set_square_color(current_row, col, MISSING_COLOR)
                        if (gw.get_key_color(letter) != correct_color and gw.get_key_color(letter) != PRESENT_COLOR):
                            gw.set_key_color(letter, MISSING_COLOR)
            
                # Correct
                if (entered_word == word):
                    gw.show_message("Congratulations! You guessed the word.")
                        
                # Incorrect
                else:
                    # Next guess
                    if (current_row < N_ROWS - 1):
                        current_row += 1
                        gw.set_current_row(current_row)

                    # No more guesses
                    else:
                        gw.show_message("Better luck next time! The word was: " + word.upper())

            # Invalid word - try again
            else:
                gw.show_message("Not a valid word")
                current_row -= 1
                current_row += 1
                gw.set_current_row(current_row)

        # HARD MODE
        elif mode == 2:
            # Correct letters have to be used in the correct spot (after they've been found)
            requirementsMet = True
            requirementsMet = checkForLetters(entered_word, correct_letter_list, present_letter_list, requirementsMet)

            # In word list and meets requirements
            if (entered_word.lower() in FIVE_LETTER_WORDS and requirementsMet == True):
                # Creates copies of the word and users word (in lists)
                word_copy = list(word[:])
                entered_word_copy = list(entered_word[:])

                # CORRECT COLOR
                for col, letter in enumerate(entered_word_copy):
                    if letter == word_copy[col]:
                        gw.set_square_color(current_row, col, correct_color)
                        gw.set_key_color(letter, correct_color)

                        # Adds letter to correct letter list and removes from present_letter list if applicable
                        correct_letter_list[col] = letter
                        if (letter in present_letter_list):
                            present_letter_list.remove(letter)

                        # Replaces letter with * to track multiple instances of the same letters
                        word_copy[col] = '*'
                        entered_word_copy[col] = '*'
                
                for col, letter in enumerate(entered_word_copy):
                    # PRESENT COLOR
                    if letter in word_copy and letter != '*':
                        gw.set_square_color(current_row, col, PRESENT_COLOR)
                        if (gw.get_key_color(letter) != correct_color):
                            gw.set_key_color(letter, PRESENT_COLOR)

                        # Adds letter to present list if not already in it
                        if (letter not in present_letter_list or (present_letter_list.count(letter) < (entered_word.count(letter) - correct_letter_list.count(letter)))):
                            present_letter_list.append(letter)

                        # Exits the loop after this code once one letter is changed (for multiple instances of the same letters)
                        exit_loop = False

                        # Finds a match in the word and replaces with * (for multiple instances of the same letters)
                        for col, char in enumerate(word_copy):
                            if (char == letter and exit_loop == False):
                                word_copy[word_copy.index(letter)] = '*'
                                exit_loop = True

                    # MISSING COLOR
                    elif letter != '*':
                        gw.set_square_color(current_row, col, MISSING_COLOR)
                        if (gw.get_key_color(letter) != correct_color and gw.get_key_color(letter) != PRESENT_COLOR):
                            gw.set_key_color(letter, MISSING_COLOR)
            
                # Correct
                if entered_word == word:
                    gw.show_message("Congratulations! You guessed the word.")
                        
                # Incorrect
                else:
                    # Next Guess
                    if current_row < N_ROWS - 1:
                        current_row += 1
                        gw.set_current_row(current_row)
                    
                    # No More Guesses
                    else:
                        gw.show_message("Better luck next time! The word was: " + word.upper())

            # Invalid word / Requirements not met
            else:
                gw.show_message("Not a valid word or not using known letters")
                current_row -= 1
                current_row += 1
                gw.set_current_row(current_row)
    
    # Initializes, focuses, adds enter function
    gw = WordleGWindow()
    gw._root.focus_force()
    gw.add_enter_listener(enter_action)
    gw._root.wait_window()

if __name__ == "__main__":
    correct_color = ''
    mode = show_radio_options()
    if mode[0] in {1, 2}:
        if mode[1] == 0:
            correct_color = CORRECT_COLOR
            wordle(mode[0])
        elif mode[1] == 1:
            correct_color = COLORBLIND_CORRECT_COLOR
            wordle(int(mode[0]))
    root = tk.Tk()
    
    # Hide the root window
    root.withdraw()
    root.mainloop()