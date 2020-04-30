# -*- coding:utf-8 -*-
# Author:Damon Guo

from turtle import*

color("red","yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()