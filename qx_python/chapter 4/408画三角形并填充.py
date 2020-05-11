__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
'''
t.color("dark blue")
t.pensize(2)
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()
'''


# 可以封装函数
def drawTriangle():
    t.color("dark blue")
    t.pensize(2)
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

drawTriangle()