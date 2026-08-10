# To test this file, use one of the following websites, or your local python compiler/IDE
# "https://pythonsandbox.com/turtle"
# "https://trinket.io/turtle"
# "https://stepindev.com/en/py-playground"


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

colours = ["blue", "red", "green", "pink"]
# you can add more colours, like
# "teal", "aqua", "lime", "chocolate", "orange"

for i in range(60):

    my_colour = random.choice(colours)
    t.pencolor(my_colour)
    
    t.forward(20)
    t.left(30)
    t.forward(70)
    t.left(121)



