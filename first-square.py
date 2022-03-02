import turtle
from turtle import *

# def square(side):
#     for i in range(4):
#         forward(side)
#         right(90)

# square(100)

def flower(length, fcolor):
    while True:
        # bgcolor("yellow")
        color(fcolor)
        lt(75)
        fd(length)
        lt(230)
        fd(length)

flower(50, "red")