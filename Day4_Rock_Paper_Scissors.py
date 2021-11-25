import random
from  tkinter import *
from tkinter import font
from tkinter.messagebox import *

FONT_NAME = "Courier"
user_choice = IntVar
comp_choice = IntVar
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
window = Tk()
window.title("Rock Paper Scissors Game")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)
def check_result(user_choice, comp_choice):
    if user_choice == comp_choice:
        result.config(text="It's a draw!")
    elif (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0):
        result.config(text="You lose!")
    else:
        result.config(text="You win!")

def press_rock():
    global user_choice_label, user_choice, comp_choice
    user_choice = 0
    comp_choice = random.randint(0,2)
    user_choice_label.config(text=f"{choices[user_choice]}", justify="left")
    comp_choice_label.config(text=f"{choices[comp_choice]}", justify="left")
    check_result(user_choice, comp_choice)
def press_paper():
    global user_choice_label, user_choice, comp_choice
    user_choice = 1
    comp_choice = random.randint(0,2)
    user_choice_label.config(text=f"{choices[user_choice]}", justify="left")
    comp_choice_label.config(text=f"{choices[comp_choice]}", justify="left")
    check_result(user_choice, comp_choice)
def press_scissors():
    global user_choice_label, user_choice, comp_choice
    user_choice = 2
    comp_choice = random.randint(0,2)
    user_choice_label.config(text=f"{choices[user_choice]}", justify="left")
    comp_choice_label.config(text=f"{choices[comp_choice]}", justify="left")
    check_result(user_choice, comp_choice)

Label(text="ROCK PAPER SCISSORS GAME", font=(FONT_NAME, 24, "bold")).grid(column=0, row=0, columnspan=3)
Label(text="What do you choose?", font=(FONT_NAME, 18, "bold")).grid(column=0, row=1, columnspan=3)

rock_button = Button(text="Rock", command=press_rock, font=(FONT_NAME, 12, "bold"))
rock_button.grid(column=0, row=2)
paper_button = Button(text="Paper", command=press_paper, font=(FONT_NAME, 12, "bold"))
paper_button.grid(column=1, row=2)
scissors_button = Button(text="Scissors", command=press_scissors, font=(FONT_NAME, 12, "bold"))
scissors_button.grid(column=2, row=2)


Label(text="User choice", font=(FONT_NAME, 12, "bold"), fg="blue").grid(column=0, row=3)
user_choice_label = Label(text="", font=FONT_NAME)
user_choice_label.grid(column=0, row=4)
Label(text="VS", font=(FONT_NAME, 50, "bold")).grid(column=1, row=3, rowspan=2)
Label(text="Computer choice", font=(FONT_NAME, 12, "bold"), fg="red").grid(column=2, row=3)
comp_choice_label = Label(text="", font=FONT_NAME)
comp_choice_label.grid(column=2, row=4)

result = Label(text="", font=(FONT_NAME, 24, "bold"))
result.grid(column=0, row=5, columnspan=3)



window.mainloop()


