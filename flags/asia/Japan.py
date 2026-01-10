
from turtle import*

#sets the red color and makes and fills the circle
color("#BC002D")
begin_fill()
for i in range(36):
    forward(10)
    right(10)
end_fill()

#prepares for the outline
color("white")
left(90)
forward(38)
right(90)
forward(144)
right(90)

#outline
color("black")
for i in range(2):
    forward(192)
    right(90)
    forward(288)
    right(90)
    
