from turtle import*
#defines how to make a stripe
def stripe(c):
    color(c)
    begin_fill()
    for i in range(2):
        forward(600)
        right(90)
        forward(100)
        right(90)
    end_fill()
    right(90)
    forward(100)
    left(90)
#makes the stripes
stripe("#FF0000")
stripe("#0000D6")
stripe("#FFB100")
