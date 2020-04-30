import turtle
# -*- coding:utf-8 -*-
# Author:Damon Guo
# 如何引入模块

# 创建一个画布
t = turtle.Pen()
# 乌龟指向默认是右90度方向,left向左再加参数度数【数学中的角度数】
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
# 左转90°
# t.left(90)
# 向前走50px
# t.forward(50)
# reset清除画布内容，海龟指向复位而clear只是清除画布内容指向依旧存在原来的位置
# t.clear()
t.reset()
