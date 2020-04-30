# -*- coding:utf-8 -*-
# Author:Damon Guo
import copy
class Animal:
    def __init__(self,name,color,num_of_leg):
        # self本对象的属性，编程习惯通常写的和参数一致
        self.name = name
        self.color = color
        self.num_of_legs = num_of_leg
rabbit = Animal("兔子","white",4)
print(rabbit.name)

tubage = copy.copy(rabbit)

print(tubage.color)