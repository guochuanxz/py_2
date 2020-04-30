# -*- coding:utf-8 -*-
# Author:Damon Guo

class Animate:
    # 构造函数又称初始化函数，对象一生成就会就用此函数，可以试一下，self代表该实例对象
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("我是初始化函数（构造函数），对象一生成我就会被调用，我叫%s" % self.name)
    def eat(self):
        print("%s:在吃饭" % self.name)

dog = Animate("Tom",12)
cat = Animate("Jerry",122)
dog.eat()
cat.eat()