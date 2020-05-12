__author__ = 'Damon'
#coding=utf-8
import turtle
t = turtle.Pen()
# 新建窗体
window = turtle.Screen()
window.setup(800,600)
window.bgcolor('white')
# 封装同心圆
def draw_circle(x,y,color,r):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
t.penup()
draw_circle(0,-200,'red',200)
draw_circle(0,-150,'white',150)
draw_circle(0,-100,'red',100)
draw_circle(0,-50,'blue',50)
# 画五角星，5个角只有最上面那个角的位置好在圆上确定下来所以我们事先把画笔调到（0，50），其他的角顶点需要三角函数运算
t.goto(0,50)
t.color('white')
t.setheading(-72)
t.begin_fill()
for i in range(5):
    t.forward(36)
    t.left(72)
    t.forward(36)
    t.right(144)
t.end_fill()
t.hideturtle()

