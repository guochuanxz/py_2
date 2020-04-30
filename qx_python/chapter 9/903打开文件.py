# -*- coding:utf-8 -*-
# Author:Damon Guo
# open第二个参数不填默认是r
file = open("D:/python_1/qx_python/chapter 9/test.txt")
txt = file.read()

file_target = open("D:/python_1/qx_python/chapter 9/目标文件.txt","w")
file_target.write(txt)
# 关闭文件，返回值是空
print(file.close())
print(txt)