from turtle import Screen
import turtle as tu
from tkinter import *
from tkinter import messagebox
import random

class Race:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.is_race_on = False

    def get_user_choice(self):
        user_bet = tu.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
        return user_bet
    
    def race_processor(self,turtles, user_bet):
        global is_race_on
        for turtle in turtles:
            if turtle.xcor() >= 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    messagebox.showinfo("Result",f"You've won! The {winning_color} turtle is the winner!")
                else:
                    messagebox.showinfo("Result",f"You've lost! The {winning_color} turtle is the winner!")
                self.is_race_on = False
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)