# -*- coding:utf-8 -*-
# Author:Damon Guo
# 条件语句
# 认识if else elif ,各个条件符号
age = 13
if age >= 20:
    print("You are too old!")
elif age ==13:
    print("You are so young and clever!")
else:
    print("You are so young!")
# 或者or    并且and
num1 = 10
num2 = 8
if num1 >=12 and num2 <=5 :
    c = num2 * num1
elif num1 < 12 or num2 >5:
    c = num1 - num2
print("c值为：%s" % (c))
# 知道什么是空值
myvar = None
# print(type(myvar))
