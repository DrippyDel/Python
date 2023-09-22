import turtle

tur = turtle.Turtle()
tur.color("purple")
tur.speed(1)

def makeShape(numSides):
    for i in range(numSides):
        tur.forward(100)
        tur.right(360.0/numSides)

makeShape(3)
makeShape(4)
turtle.done()
