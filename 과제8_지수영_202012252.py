import turtle
import random

t = turtle.Pen("turtle")
t.pensize(10)
s = turtle.Screen()
s.onscreenclick(t.goto)

colors = ["orange", "green", "blue", "black"]

def circle():
    length = 1
    t.penup()
    t.backward(100)
    t.speed(0)
    t.width(1)
    t.pendown()
    while length < 50:
        t.pencolor(colors[length%4])
        t.circle(length,45)
        length += 1
        if length > 50:
            t.pencolor("black")
    t.pencolor("black")


def pensize():
    pen = int(input("pensize: "))
    t.pensize(pen)

def square():
    t.pensize(1)
    length = int(input("정사각형 한 변의 길이: "))
    for i in range(4):
        t.begin_fill()
        t.color(random.choice(colors))
        t.forward(length)
        t.left(90)
        t.end_fill()
    t.right(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.color("red")
    t.write("사각형", font=("굴림체", 10, "bold"))
    t.color("black")
    t.pensize(10)
    t.left(90)
    
s.onkey(t.penup, "Up")
s.onkey(t.pendown, "Down")
s.onkey(t.undo, "-")
s.onkey(circle, "c")
s.onkey(pensize, "p")
s.onkey(square, "s")
s.listen()
