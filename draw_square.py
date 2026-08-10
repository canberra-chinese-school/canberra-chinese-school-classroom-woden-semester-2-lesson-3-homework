# To test this file, use one of the following websites, or your local python compiler/IDE
# "https://pythonsandbox.com/turtle"
# "https://trinket.io/turtle"
# "https://stepindev.com/en/py-playground"

import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.speed(5)
t.pensize(1)
t.pencolor("black")
screen.bgcolor("lightblue")

for i in range(4):
    t.forward(100)
    t.left(90)

