import turtle
import random


t = turtle.Pen()
t.shape("turtle")
t.shapesize(3,3)
t.up()
point = 0


def show(x,y):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    global point
    point +=1
    print(point)
    t.goto(x,y)

t.onclick(show)
