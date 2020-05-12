__author__ = 'Damon'
#coding=utf-8
# 引入海归库给海龟库起别名
import turtle
t = turtle.Pen()

t.pensize(5)
# 画第一个圆
t.color('black')
t.circle(50)
# 画第二个圆
t.color('blue')
t.penup()
t.goto(-110,0)
t.pendown()
t.circle(50)
# 画第三个圆
t.color('red')
t.penup()
t.goto(110,0)
t.pendown()
t.circle(50)
# 画第四个圆
t.color('yellow')
t.penup()
t.goto(-55,-50)
t.pendown()
t.circle(50)
# 画第五个圆
t.color('green')
t.penup()
t.goto(55,-50)
t.pendown()
t.circle(50)
t.hideturtle()


