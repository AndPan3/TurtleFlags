
from turtle import*

def stripe (c):
    #begins fill
    begin_fill()
    color(c)
    #repeats 2 sides of a rectangle to make a whole rectangle
    for i in range(2):
        forward(60)
        right(90)
        forward(120)
        right(90)
    #ends the fill
    end_fill()
    #makes the pen ready for next rectangle
    forward(60)    
    
#makes the stripes    
# #008C45 for example is a hex value, it can determine the color
stripe("#008C45")
stripe("#F4F5F0")
stripe("#CD212A")

#optional: Outline
right(90)
color("black")
for i in range (2):
    forward(120)
    right(90)
    forward(180)
    right(90)
