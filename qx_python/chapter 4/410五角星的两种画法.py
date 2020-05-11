__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
t.color('yellow')
#方法一
'''
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
'''
# 方法二
t.begin_fill()
for i in range(5):
    t.forward(63)
    t.left(72)
    t.forward(63)
    t.right(144)
t.end_fill()