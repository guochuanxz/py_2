__author__ = 'Damon'
# coding=utf-8
# 一般for循环range参数 起始值 结束值（开区间），步长
for i in range(0, 5, 2):
    print(i)
# 特殊for循环
a_str = '申酉戌亥子丑寅卯辰巳午未'
for i in a_str:
    print(i)
a_list = ["a", 'b', 'c']
for i in a_list:
    print(i)
for year in range(1990, 2020):
    print("%s 年的生肖是%s " % (year, a_str[year % 12]))
