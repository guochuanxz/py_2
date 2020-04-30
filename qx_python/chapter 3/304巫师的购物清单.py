# -*- coding:utf-8 -*-
# Author:Damon Guo

wizard_list = "snake,frog,cat,dog,lion,tiger"
# print(wizard_list)
# 很显然字符串的操作不能随意的显示具体的某一项，这时列表的作用来了。回想scratch学习音符列表的作用
# 列表中的每一项称为元素
# 理解区间包含关系
damon_list = ["snake","frog","cat","dog","lion","tiger"]
print(damon_list[0])
print(damon_list[1:3])
print(damon_list[1:])
print(damon_list[:3])
# 讲索引位置（下标）

# 列表中可以放什么？
number_list = [1,4,45,23,21]
string_list = ["snake","frog","cat","dog","lion","tiger"]
number_and_string_list = ["snake","frog","cat","dog","lion","tiger",12,21,32,43,23]
# 还可以这么写
list_list = [["snake","frog","cat","dog","lion","tiger"],[12,21,32,43,23]]
# 如何取出值
print(list_list[1][0])



