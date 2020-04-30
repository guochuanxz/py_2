# -*- coding:utf-8 -*-
# Author:Damon Guo

# 计算学生总数的函数
# 全局变量
cls2 = 2
def stus():
    # 局部变量优先
    cls1 = 50
    print("一班有%s"%cls1)
    # 如果函数体内加global就会改变全局变量
    # global cls2
    # cls2 = 5
    cls2 =45
    print("二班有%s"%cls2)
    cls3 = 56
    print("三班有%s"%cls3)
    return cls1 + cls2 + cls3


# 函数体内的变量只能归函数使用，出了函数体变量就不再存在了

print(stus())
print(cls2)