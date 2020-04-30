# -*- coding:utf-8 -*-
# Author:Damon Guo
# 字典又称作map 映射,键值对。字典不要和列表一样加或者乘
favourite_sports = {
    'Tom':'ping pong',
    'David':'bskball',
    'Damon':'ftball'
}
print(favourite_sports['Tom'])
# 删除元素
del favourite_sports['Tom']
print(favourite_sports)
#更改元素
favourite_sports['Damon'] = 'Rugby'
print(favourite_sports)

name = 'Damon'
age =12
# msg = "My name is %s , I'm %s yeas old!"
print("My name is %s , I'm %s yeas old!" % (name,age))
