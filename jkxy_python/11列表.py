__author__ = 'Damon'
#coding=utf-8
# 列表中同样有元组、字符串操作的方法
a_list = [
    'a','b','xx','c','d','e'
]
b_list = [
    '1','2'
]
a_list.append('q')
print(a_list)
a_list.remove('xx')
print(a_list * 3)
print(a_list + b_list)
print('a' in a_list)
print('a' not in a_list)
print(a_list[0:3])