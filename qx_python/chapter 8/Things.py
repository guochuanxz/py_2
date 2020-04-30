# -*- coding:utf-8 -*-
# Author:Damon Guo
# 继承
class Things:
    def gradepa_func(self):
        pass
class Animate(Things):
    pass
class Inanimate(Things):
    pass
class Animals(Animate):
    def breath(self):
        pass
    def eat_food(self):
        pass
    def drink(self):
        pass
class Mammals(Animals):
    def father(self):
        print("我是猪父类的方法")
    pass
class Pig(Mammals):
    def pig_function_eat(self):
        print("我是猪类吃的方法")
    def pig_function_sleep(self):
        print("我是猪类睡觉的方法")
class Sidewalks(Inanimate):
    pass
# 创建猪类的一个对象，实例化
tom = Pig()
tom.pig_function_eat()
tom.father()
def this_is_a_normal_func():
    print("我是普通的函数")

# this_is_a_normal_func()