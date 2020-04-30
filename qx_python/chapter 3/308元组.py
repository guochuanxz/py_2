# -*- coding:utf-8 -*-
# Author:Damon Guo
# 元组,像一个用括号（）表示的一个列表,区别在于  -元组声明之后就不可以更改，更改会报错- 同学们根据实际需求选择应用
damon_flibs = (1,2,43,65,43)
# damon_flibs[2] = 23
print(damon_flibs[2])

############################################################

#字典 讲解映射和键值对   key  value

favorite_sport ={
    'ChenFeiyu':'Football',
    'JiangYuchen':'Basktball',
    'LuZiliang':'Pingpong'
}

print(favorite_sport['ChenFeiyu'])
# 删除字典中的元素
del favorite_sport['ChenFeiyu']
# 更改字典中的元素
favorite_sport['JiangYuchen'] = 'PingPong'
print(favorite_sport)