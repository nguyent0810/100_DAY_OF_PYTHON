from turtle import Turtle
from data import colors, y_positions
 

class Turtles:
    def __init__(self):
        self.turtles = []
        self.number_of_turtle = 0

    def list_turtles(self, number_of_turtle):
        for index in range(0, number_of_turtle):
            self.turtle = Turtle("turtle")
            self.turtle.color(colors[index])
            self.turtle.penup()
            self.turtle.goto(-230, y_positions[index])
            self.turtles.append(self.turtle)
        return self.turtles
    