from turtle import*

color("red")

#initial square and fill

begin_fill()
for i in range (4):
    forward(160)
    right(90)
end_fill()

#moves so cross can start
penup()
forward(95)
right (90)
forward(30)

color("white")
#defines how a cross is made
def cross (f):
    begin_fill()
    for i in range (2):
        forward(f)
        right(90)
        forward(30)
        right(90)
    end_fill()

#makes both crosses
cross(100)
forward(65)
right(90)
backward(35)
cross(100)
        
