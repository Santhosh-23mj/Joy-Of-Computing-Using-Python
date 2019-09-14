#!/usr/bin/python3

"""
This program simply shows the use of
Turtle library
"""

import turtle

turtle.bgcolor("black")
tur = turtle.Turtle()
tur.color("white")

for i in range(4):
    tur.forward(100)
    tur.right(90)
for i in range(5):
    tur.forward(100)
    tur.right(144)
    
turtle.done()