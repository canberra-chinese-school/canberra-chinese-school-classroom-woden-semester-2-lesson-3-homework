# Run this script, spot the difference between the shape this scripts generates and the shape we generated in class (see class_exercise.py).
# Which one looks better to you?
# Task: look at the code below, and try to explain how it works. Add some more colours in the change_colour function.
# You can also mess around with the numbers the for loop.
# Save your changes in this file and commit changes to submit your homework.

# To run this script:
# Since we use a new module called turtle, regular python compiler websites (like online-python.com) will not work.
# Please test your script in turtle supported online python environments, like
# "https://pythonsandbox.com/turtle"
# or "https://trinket.io/turtle"
# or "https://stepindev.com/en/py-playground"

import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.speed(0)  # 0 is fastest, otherwise, 
# the higher the number is, the faster it is
t.pensize(1)
t.pencolor("black")
screen.bgcolor("lightblue")

def change_colour(colour):
    if colour == "red":
        return "green"
    if colour == "green":
        return "yellow"
    if colour == "yellow":
        return "blue"
    if colour == "blue":
        return "red"

current_colour = "red"

for i in range(60):
    current_colour = change_colour(current_colour)
    t.pencolor(current_colour)
    t.forward(20)
    t.left(30)
    t.forward(70)
    t.left(121)
















