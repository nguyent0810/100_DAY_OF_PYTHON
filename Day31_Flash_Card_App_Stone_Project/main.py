from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

data_file_path = "data/french_words.csv"

try:
    data = pandas.read_csv(f"data/word_to_learn.csv")
except:
    original_data = pandas.read_csv(data_file_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = ""
# Read the csv file
def next_card():
    global current_card, flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    #known_button.config(state="disabled")
    #unknow_button.config(state="disabled")
    flip_timmer = window.after(3000, flip_card)
def flip_card():
        canvas.itemconfig(card_image, image=card_back_image)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        #known_button.config(state="active")
        #unknow_button.config(state="active")
def is_known():
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv(f"data/word_to_learn.csv", index=False)
        next_card()
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)   
flip_timmer = window.after(3000, flip_card)   
# UI
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknow_button = Button(image=cross_image, bg=BACKGROUND_COLOR, command=next_card, highlightthickness=0, borderwidth=0)
unknow_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, bg=BACKGROUND_COLOR, command=is_known, highlightthickness=0, borderwidth=0)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()