#Password Generator Project
import random
from tkinter import *
from tkinter import font
FONT_NAME = "Courier"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_generator(number, list_choice):
    rd_string = ""
    for l in range(0, number):
        rd_string += random.choice(list_choice)
    return rd_string
def generate_eazy_pass():
    # #Eazy Level - Order not randomised:
    # #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    nr_letters = int(nr_letters_entry.get())
    nr_symbols = int(nr_symbols_entry.get())
    nr_numbers = int(nr_numbers_entry.get())
    rd_letters = random_generator(nr_letters, letters)
    rd_symbols = random_generator(nr_symbols, symbols)
    rd_numbers = random_generator(nr_numbers, numbers)

    eazy_pass = rd_letters + rd_symbols + rd_numbers
    return eazy_pass

def press_generator_button():
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    eazy_pass = generate_eazy_pass()
    sample_pass = random.sample(eazy_pass,len(eazy_pass))
    hard_pass = ''.join(sample_pass)
    random_password.delete(0, END)
    random_password.insert(0, hard_pass)
    #random_password.config(text=f"{hard_pass}")

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

Label(text="Welcome to the PyPassword Generator!", font=(FONT_NAME, 24, "bold")).grid(column=0, row=0, columnspan=2)
Label(text="How many letters would you like in your password?", justify="left", font=(FONT_NAME, 18, "bold")).grid(sticky = W, column=0, row=1)
nr_letters_entry = Spinbox(from_=0, to=10, width=5)
nr_letters_entry.grid(column=1, row=1)
Label(text="How many symbols would you like?", justify="left", font=(FONT_NAME, 18, "bold")).grid(sticky = W, column=0, row=2)
nr_symbols_entry = Spinbox(from_=0, to=10, width=5)
nr_symbols_entry.grid(column=1, row=2)
Label(text="How many numbers would you like?", justify="left", font=(FONT_NAME, 18, "bold")).grid(sticky = W, column=0, row=3)
nr_numbers_entry = Spinbox(from_=0, to=10, width=5)
nr_numbers_entry.grid(column=1, row=3)

generator_button = Button(text="Generator", command=press_generator_button, font=(FONT_NAME, 24, "bold"), fg="white", bg="green")
generator_button.grid(column=0, row=4, columnspan=2)
random_password = Entry(text="", font=(FONT_NAME, 24, "bold"), justify='center')
random_password.grid(column=0, row=5, columnspan=2)

window.mainloop()


