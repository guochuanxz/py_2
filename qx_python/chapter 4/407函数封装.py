__author__ = 'Damon'
#coding=utf-8
import turtle as t

def drawCircle(color,x,y,size):
    t.pensize(5)
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(size)

drawCircle('black',0,0,50)
drawCircle('blue',-110,0,50)
drawCircle('red',110,0,50)
drawCircle('yellow',-55,-50,50)
drawCircle('green',55,-50,50)