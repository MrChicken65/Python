#Module 1 Assignment INFO 1020
#Please use this template and fill in code after each comment

#Import the turtle module (see page 19, section 1.5 of text 4th ed.)

import turtle

t = turtle.Turtle()

#Have the turtle draw something interesting.
#The turtle must use a loop to repeat some aspect of the drawing.
#Use at least two different shapes.  You _can_ use the drawPolygon() 
#and drawCircle() functions from the book.
#If you aren't sure what to draw, do Programming Exercise 1.1 in the book.

triSize = 100

def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

def drawTriangle(myTurtle):
    for i in range(3):
        myTurtle.forward(triSize)
        myTurtle.right(120)

t.pos()

t.speed(10)

t.left(90)
drawTriangle(t)
t.right(60)
drawTriangle(t)
t.right(60)
drawTriangle(t)
t.forward(triSize)
t.right(60)
drawTriangle(t)
t.forward(triSize)
t.right(60)
drawTriangle(t)
t.left(60)
drawTriangle(t)
t.right(180)
drawTriangle(t)
t.right(60)
drawTriangle(t)
t.left(60)
t.forward(triSize)
drawTriangle(t)
t.right(60)
drawTriangle(t)
t.right(60)
t.forward(triSize)
for i in range(2):
    drawTriangle(t)
    t.left(60)
drawTriangle(t)
t.right(120)
t.forward(triSize)
for i in range(2):
    drawTriangle(t)
    t.left(60)
drawTriangle(t)
t.forward(triSize)
t.left(60)
for i in range(2):
    drawTriangle(t)
    t.right(60)
drawTriangle(t)
t.left(60)
t.forward(triSize)
t.right(60)
drawTriangle(t)

t.left(120)
t.penup()
t.forward(200)
t.pendown()
drawTriangle(t)
t.penup()
t.forward(200)
t.pendown()
drawPolygon(t, 100, 8)



# This line is just because I'm using VScode and it will close automatically
turtle.exitonclick()









#When finished, submit both this .py file and a png screenshot of your drawing.
