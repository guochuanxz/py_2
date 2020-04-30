# -*- coding:utf-8 -*-
# Author:Damon Guo
# Tom和Jerry都是画笔对象，都可以调用海龟库Pen（）类的方法
import turtle

tom = turtle.Pen()
jerry = turtle.Pen()
tom.forward(100)
tom.left(90)
tom.forward(100)
jerry.backward(100)
jerry.left(90)
jerry.forward(120)
