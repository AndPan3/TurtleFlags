#please note that these arent the real proportions

from turtle import*
#defines how you make a stripe
def stripe (s):
    #beginfill marks the start of everything that neds to be filled
    begin_fill()
    #repeats two sides of the stripe twice
    forward(s)
    right(90)
    forward(67)
    right(90)
    forward(s)
    right(90)
    forward(67)
    right(90)
    #makes the pen ready for next stripe
    forward(s)
    #endfill fills everything that the pen drew from beginfill
    end_fill()

#makes the stripes
color("blue")
stripe(30)
color("white")
stripe(33)
color("red")
stripe(37)


#optional: Outline
color("black")
#makes the pen ready for outline
right(90)
for i in range(2):
    #the width needs addition af all width of stripe
    forward(67)
    right(90)
    forward(100)
    right(90)

    
