__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
# 定义画笔速度
t.speed(1)

# 新建900X600像素的窗口,引入海龟库的Screen类
window = turtle.Screen()
window.bgcolor("red")
window.setup(900,600)

# 封装五角星的画法
'''
xy为移动指定点degree星星旋转角度size星星大小
'''

def drawFiveStar(x,y,degree,size):
    t.setpos(x,y)
    t.pendown()
    t.setheading(degree)
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()
t.penup()
drawFiveStar(-390,180,0,72)
drawFiveStar(-170,260,330,15)
drawFiveStar(-120,170,30,15)
drawFiveStar(-120,100,0,15)
drawFiveStar(-170,60,330,15)
# 隐藏海龟小箭头
t.hideturtle()