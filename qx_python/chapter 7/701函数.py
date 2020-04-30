# -*- coding:utf-8 -*-
# Author:Damon Guo
# 知道函数组成：名称、参数、函数体、【返回值】，举例买烟的故事.***难理解***
def demo_function(name,age):
    print("I'm %s,%s years old."%(name,age))
    return age
age = demo_function("Damon",18)

print(age)