from turtle import*

#defines how a stripe is made
def stripe (c):
    color(c)
    begin_fill()
    for i in range(2):
        forward (135)
        left(90)
        forward(10)
        left (90)
    end_fill()
    #makes the stripe ready for new rectangle
    left(90)
    forward(10)
    right(90)

#make the stripes
for i in range(5):
    stripe("white")
    stripe("#014488")

#square
begin_fill()
for i in range (4):
    forward(50)
    right(90)
end_fill()

#cross
#positiones for first cross and defines (says how to make cross)
forward(20)
right(90)
def cross (c):
    begin_fill()
    color(c)
    for i in range(2):
        forward(50)
        left(90)
        forward(10)
        left(90)
    end_fill()
#makes the crosses
cross("white")
#positiones for second cross
forward(30)
left(90)
backward(20)
#makes second cross
cross("white") 
