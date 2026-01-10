from turtle import *

#set pen width and turns sets color white
width(10)
color ("white")

#change color and go forward
def Stripe (c):
    color(c)
    forward(180)

#rotates so it can begin new stripe
def Rotate (r):
    r (90)
    forward(10)
    r (90)

#makes the initial stripes
repeat 5:
    Rotate (left)
    Stripe ("blue")
    Rotate (right)
    Stripe ("white")

#rotates the pen 180 and makes it prepared for the square
right (180)
forward(180)
left (90)
forward (10)

#makes the square
color ("blue")
turtle.begin_fill()
repeat 4:
    forward (45)
    left (90)
turtle.end_fill()

#cross
left(90)
penup()
forward(25)
width (10)
color("white")
pendown()
right(90)
#first cross, then halfway backward
forward(50)
backward(25)
#second cross
left(90)
forward(25)
backward(50)

#moves the pen back
penup()
left(90)
forward(30)
right (90)
#outline
pendown()
color("black")
def outline (b):
    forward(b)
    right (90)
    forward (95)
    right(90)

#make the outlines
outline (190)
outline (200)

#aesthetics
forward (10)
penup()




