__author__ = 'Damon'
#coding=utf-8
file = open('name.txt')
#只读一行一般不用
# print(file.readline())
# 多行遍历
for i in file.readlines():
    print(i)
    print('___________________')