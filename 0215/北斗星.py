# -*- coding:utf-8 -*-
# Author:Damon Guo

from turtle import*
x = 360/10
y = 120
for i in  range(10):
    if i % 2 == 0:
        color("yellow")
    else:
        color("skyblue")
    begin_fill()
    forward(y)
    left(x)
    forward(y)
    left(180-x)
    forward(y)
    left(x)
    forward(y)
    left(180-x)
    end_fill()
    left(x)
done()
