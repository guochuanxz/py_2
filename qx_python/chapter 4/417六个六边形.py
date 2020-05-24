__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
t.clear()
t.penup()
t.pensize(2)
t.color("blue")
t.goto(0,0)
t.setheading(0)
t.pendown()
def drawSix():
     for i in range(6):
        for j in range(6):
            t.forward(100)
            t.left(60)
        t.left(60)
drawSix()
t.hideturtle()

