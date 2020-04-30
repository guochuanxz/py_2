# -*- coding:utf-8 -*-
# Author:Damon Guo
# for循环可以循环一个区间或者一个列表
for i in range(0,10):
    print(i)

# print(list(range(0,5)))
color_list=['yellow','blue','red']
num_list=['1','2','3']
# color_list={'one':'yellow','two':'blue','three':'red'}
# print(color_list[2])
for i in color_list:
    print("外层循环"+i)
    for j in num_list:
        print("内层循环"+j)