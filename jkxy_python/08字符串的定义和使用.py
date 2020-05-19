__author__ = 'Damon'
#coding=utf-8
# 公元1年为鸡年   取12模1为生肖排列第二个序列号为1  所以我们重新排序
shengxiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
shengxiao_ = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 1990
print(shengxiao_[year % 12])
