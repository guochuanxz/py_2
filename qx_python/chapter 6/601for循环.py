# -*- coding:utf-8 -*-
# Author:Damon Guo
# i计数器range(开始【取得到初识值】、结束【取不到最后】、步进【默认1】)
# 参照0124
for i in range(0,10,2):
    print("loop : ",i)

# 循环打印5次
for i in range(0,5):
    print("hello ",i)


# 打印damon老师的列表
damon_list = ["snake","frog","cat","dog","lion","tiger"]

for i in damon_list:
    print(i)
# 打印damon老师的元组
damon_flibs = (1,2,43,65,43)
for i in damon_flibs:
    print(i)
# 打印damon老师的字典,只能打印键，如何打印值？
# 有了键就能打印值
favorite_sport ={
    'ChenFeiyu':'Football',
    'JiangYuchen':'Basktball',
    'LuZiliang':'Pingpong'
}
for i in favorite_sport:
    print(i,favorite_sport[i])