# 몸체를 그린다.
def draw_body():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

# 지붕을 그린다.
def draw_roof():
    t.forward(100)
    t.right(-120)
    t.forward(100)
    t.right(-120)
    t.forward(100)
    t.right(-120)

import turtle
t = turtle.Pen()

# 몸체를 그린다.
draw_body()

# 방향을 저장한다.
t.right(90)

# 지붕을 그린다.
draw_roof()
