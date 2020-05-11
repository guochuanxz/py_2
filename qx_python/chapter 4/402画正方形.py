# -*- coding:utf-8 -*-
# Author:Damon Guo
import turtle

t = turtle.Pen()
'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
'''

def drawSquare():
    t.color("green")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
drawSquare()
#########################################
# 函数区别：哪个清除后复位哪个只是清除
# t.forward(150)
# t.left(90)
# t.forward(100)
# t.reset()
# t.clear()

