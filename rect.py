Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t.turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    t.turtle.Pen()
NameError: name 't' is not defined
>>> t=turtle.Pen()
>>> t.right(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.shape("turtle")
>>> 