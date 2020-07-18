import turtle
import math

t = turtle.Turtle("turtle")

def triangle(length,n):
    if n == 0:
        for i in range(3):
            t.forward(length)
            t.left(120)
    else:
        for i in range(3):
            triangle(length/2,n-1)
            t.forward(length)
            t.left(120)

triangle(400,3)
