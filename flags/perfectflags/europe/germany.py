from turtle import*
#defines how a stripe is made
def stripe (c):
    #color and starts fill
    color(c)
    begin_fill()
    #repeats two side twice
    for i in range(2):
        forward(25)
        right(90)
        forward(5)
        right(90)
    #makes the pen prepared for the next stripe
    left(90)
    forward(5)
    right(90)
    #ends fill
    end_fill()

#makes the 3 stripes
stripe("yellow")
stripe("red")
stripe("black")
#makes a white stripe so you cant see the line and takes the pen up
stripe("white")
penup()


    
