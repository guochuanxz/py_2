__author__ = 'Damon'
#coding=utf-8
# 常见的错误不可以直接抛给用户，在可能会出现错误的地方用  try捕获异常并处理
# 语法错误、超出序列数、数值类型错误等等不能直接显示给用户
# year = int(input("请输入年："))
try:
    year = int(input("请输入年："))
except  ValueError:
    print("请输入数字！")
finally:
    print("年：%d" % year)
    print("下面的代码不管程序是否抛出异常我都会执行")
