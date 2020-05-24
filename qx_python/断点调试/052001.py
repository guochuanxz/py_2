__author__ = 'Damon'
#coding=utf-8
# F7进入函数步进   F8会把函数当成一行语句不进入函数体
name = 'Luna'
def say_hello():
    name = "Damon"
    print("hello %s" %name)
print("hello %s" %name)
say_hello()