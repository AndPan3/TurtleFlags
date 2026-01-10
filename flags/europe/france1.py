#please note that these arent the real proportions

from turtle import*
#defines how you make a stripe
def stripe (c):
    color(c)
    #beginfill marks the start of everything that neds to be filled
    begin_fill()
    #repeats two sides of the stripe twice
    for i in range(2):
        forward (15)
        right(90)
        forward(30)
        right(90)
    #makes the pen ready for next stripe
    forward(15)
    #endfill fills everything that the pen drew from beginfill
    end_fill()

#makes the stripes
stripe("blue")
stripe("white")
stripe("red")
#optional: Outline
color("black")
#makes the pen ready for outline
right(90)
for i in range(2):
    #the width needs to be 3x of one stripe
    forward(30)
    right(90)
    forward(45)
    right(90)

    
