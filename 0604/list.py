# -*- coding:utf-8 -*-
# Author:Damon Guo
# 什么是列表（数组）、下标（索引）
wizard_list = [
    'snake','lion','duck'
]
print(wizard_list[0],wizard_list[1],wizard_list[2])
# 如何向列表中追加元素
# wizard_list.append('chicken')
# wizard_list.append('dog')
# wizard_list.append('cat')
print(wizard_list)
# 删除数组中的元素
del wizard_list[0]
# 数组可以做乘法运算，元素数量
print(wizard_list * 5)
#数组之间的相加
stu_list = ['a','b','c']
print(stu_list + wizard_list)
num_list = [1,3,6,5]
print(num_list[0] * 4)

# 什么是元组，特殊的列表,但是元组一旦创建就无法进行更改
count_list =(1,3,546,65)
# print(type(count_list))

print(count_list)



