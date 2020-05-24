__author__ = 'Damon'
#coding=utf-8
# 方法体外变量
name = 'zhangsan'
# 函数内的变量要和函数外的变量通用加 global变为全局变量
def test():
    a ='lisi'
    global name
    name = 'lisei'
    print(name)
test()
print(name)