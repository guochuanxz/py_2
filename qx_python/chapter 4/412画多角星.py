__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
# 知识点：圆周角和圆心角的关系2
# 圆周角为多角星的角度，画笔右旋转180-圆周角
#有bug尚未解决   奇数没问题  6  10  14  18
def drawNstar(n,size):
    t.pendown()
    if n % 2 == 0 :
        for i in range(n):
            t.forward(size)
            t.right(180 - 180 * 2 / n)
    else:
        for i in range(n):
            t.forward(size)
            t.right(180 - 180 / n)

    t.penup()
t.penup()
drawNstar(14,100)


