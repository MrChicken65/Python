import turtle

t = turtle.Turtle()
#t2 = turtle.Turtle()

def drawSquare(myTurtle, sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def drawTriangle(myTurtle, sideLength):
    for i in range(3):
        myTurtle.forward(sideLength)
        myTurtle.right(120)

def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

t.left(90)
t.up()
t.forward(500)
t.down()
t.right(90)

drawPolygon(t, 15, 200)
'''
drawSquare(t, 100)

t.up()
t.forward(200)
t.down()

drawTriangle(t, 100)
'''
# This is to prevent it from closing out automatically on VScode
turtle.exitonclick()
