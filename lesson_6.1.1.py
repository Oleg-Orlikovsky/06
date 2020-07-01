from turtle import Turtle, Screen
import time

CURSOR_SIZE = 20

def running():
    for turtle in screen.turtles():
        turtle.fillcolor('red')

    screen.ontimer(running, 7.0)

screen = Screen()

pen1 = Turtle(shape='circle')
pen1.shapesize(80 / CURSOR_SIZE)
pen1.color('red')
pen1.penup()
pen1.sety(90)
pen1 = time.sleep(2.0)

def running():
    for turtle in screen.turtles():
        turtle.fillcolor('yellow')

    screen.ontimer(running, 2.0)

pen2 = Turtle(shape='circle')
pen2.shapesize(80 / CURSOR_SIZE)
pen2.color('yellow',)
pen2.penup()
pen2.sety(0)
pen2 = time.sleep(2.0)

def running():
    for turtle in screen.turtles():
        turtle.fillcolor('green')

    screen.ontimer(running, 1.0)

pen3 = Turtle(shape='circle')
pen3.shapesize(80 / CURSOR_SIZE)
pen3.color('green')
pen3.penup()
pen3.sety(-90)
pen3 = time.sleep(1.0)

screen.mainloop()
