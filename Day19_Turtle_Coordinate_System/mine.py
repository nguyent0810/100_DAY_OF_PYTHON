from turtle import Turtle, Screen
import turtle as tu
import random
from tkinter import *
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
user_bet = tu.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_range = -230
y_range = -60
turtles = []
is_race_on = False

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x_range, y_range)  
    y_range += 30
    turtles.append(new_turtle)
    print(turtles[0].pencolor())

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Result",f"You've won! The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo("Result",f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

