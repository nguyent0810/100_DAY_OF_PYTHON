from tkinter import *
from hangman_art import logo
FONT_NAME = "Courier"
class Hangman_Machine:
    def __init__(self, word, main):
        self.my_images = []
        self.my_images.append(PhotoImage(file="states_picture/state_0.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_1.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_2.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_3.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_4.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_5.png"))
        self.my_images.append(PhotoImage(file="states_picture/state_6.png"))
        self.my_images_number = 0
        self.display = []
        self.word = word
        self.lives = 6
        self.state_img = ""
        self.end_of_game = False
        self.word_length = len(word)
        self.response = ""
        for _ in range(self.word_length):
            self.display += "_"
    
        Label(text=logo, font=(FONT_NAME, 24, "bold"), justify="left").grid(column=0, row=0, columnspan=2)
        self.canvas = Canvas(width=200, height=224, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, rowspan=6)
        self.image_one_canvas = self.canvas.create_image(100, 112, image=self.my_images[self.my_images_number])
        Label(text="WORD LENGTH", font=(FONT_NAME, 18, "bold")).grid(column=1, row=1)
        self.display_label = Label(text=self.display, font=(FONT_NAME, 18, "bold"))
        self.display_label.grid(column=1, row=2)
        Label(text="GUESS A LETTER", font=(FONT_NAME, 18, "bold")).grid(column=1, row=3)
        self.guess_entry = Entry()
        self.guess_entry.grid(column=1, row=4)
        self.submit_button = Button(text="Submit", command=self.start_guess, font=(FONT_NAME, 18, "bold"))
        self.submit_button.grid(column=1, row=5)
        self.respone_label = Label(text=self.response, font=(FONT_NAME, 18, "bold"))
        self.respone_label.grid(column=1, row=6)


    def game_start(self, user_guess):
        self.guess = user_guess
        if self.guess in self.display:
            self.response = f"You've already guessed {self.guess}"
        for position in range(self.word_length):
            letter = self.word[position]
            if letter == self.guess:
                self.display[position] = letter

        if self.guess not in self.word:
            self.response = f"You guessed {self.guess}, that's not in the word. You lose a life."
            self.lives -= 1
            self.my_images_number += 1
            if self.lives == 0:
                self.response = "You lose."
        #self.display = f"{' '.join(self.display)}"

        if "_" not in self.display:
            self.response = "You win"
        
    def start_guess(self):
        user_guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, END)
        self.game_start(user_guess)
        self.respone_label.config(text=self.response)
        self.display_label.config(text=self.display)
        self.canvas.itemconfig(self.image_one_canvas, image=self.my_images[self.my_images_number])