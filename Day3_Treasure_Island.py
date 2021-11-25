from tkinter import *
from tkinter.messagebox import *
from tkinter import font
import tkinter
window = Tk()
window.title("Treasure Island")
window.config(pady=20, padx=20)
logo = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
def press_red():
    showinfo("Game Over", "You entered a burning house.")
    window.destroy()
def press_blue():
    showinfo("Game Over", "You entered a room of beasts")
    window.destroy()
def press_green():
    showinfo("You Win!!!", "You found the treasure")
    window.destroy()
def press_swim():
    showinfo("Game Over", "You're killed by an anaconda.")
    window.destroy()
def press_wait():
    question['text'] = "You arrive at the island unharmed. \nThere is a house with 3 doors. \nOne red, one yellow and one blue. \nWhich colour do you choose?"
    btn_1.config(text="red", command=press_red, background="red")
    btn_2.config(text="blue", command=press_blue, background="blue")
    btn_3 = Button(window,text="green", command=press_green, font=("Courier"), background="green")
    btn_3.grid(column=3, row=3)

def press_left():
    question['text'] = "You come to a lake. \nThere is an island in the middle of the lake. \nType 'wait' to wait for a boat. \nType 'swim' to swim across."
    question.config(justify="left")
    btn_1.config(text="swim", command=press_swim)
    btn_2.config(text="wait", command=press_wait)
def press_right():
    showinfo("Game Over", "You're facing the poison snake.")
    window.destroy()
Label(window,text="Welcome to Treasure Island", font=("Courier", 24, "bold")).grid(column=0, row=0, columnspan=4)
Label(window,text="Your mission is to find the treasure", font=("Courier", 18, "bold")).grid(column=0,row=1, columnspan=4)
Label(window,text=logo,justify="left", font=("Courier")).grid(column=0, row=2, columnspan=4)
question = Label(window, text="You're at a cross road. Where do you want to go?",font=("Courier"))
question.grid(column=0, row=3)
btn_1 = Button(window,text="Left", command=press_left, font=("Courier"))
btn_1.grid(column=1, row=3)
btn_2 = Button(window,text="Right", command=press_right, font=("Courier"))
btn_2.grid(column=2, row=3)

window.mainloop()
