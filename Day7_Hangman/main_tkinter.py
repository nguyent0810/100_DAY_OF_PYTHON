import random
from tkinter import *
from hangman_words_list import word_list
from hangman_machine import Hangman_Machine

FONT_NAME = "Courier"
chosen_word = random.choice(word_list)

window = Tk()
window.title("The Hangman Game")
window.config(padx=20, pady=20)

hangman_machine = Hangman_Machine(chosen_word, window)




window.mainloop()