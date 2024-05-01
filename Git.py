import turtle
wn = turtle.Screen()
blue = turtle.Turtle()

def curve():
    for i in range(200):
        blue.right(1)
        blue.forward(1)

def heart():
    blue.fillcolor('orange')
    blue.begin_fill()
    blue.left(120)
    blue.forward(113)
    curve()
    blue.left(180)
    curve()
    blue.forward(112)
    blue.end_fill()

heart()
blue.ht()
turtle.done()
