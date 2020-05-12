__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()

def drawPolygon(angle,step):
    t.pendown()
    t.pensize(3)
    degree = 180-(angle-2)*180/angle
    for i in range(angle):
        t.forward(step)
        t.left(degree)
    t.penup()
    t.hideturtle()
t.penup()
t.setpos(100,100)
drawPolygon(3,50)
t.goto(-100,100)
drawPolygon(4,50)
t.goto(-100,-100)
drawPolygon(5,50)
t.goto(100,-100)
drawPolygon(150,3)

