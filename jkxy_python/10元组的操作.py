__author__ = 'Damon'
#coding=utf-8
# 按小于等于日期对应星座做成两个元组
xingzuo  = ('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
dates = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
m = int(input("请输入您出生的月:"))
d = int(input("请输入您出生的日:"))
# filter(lambda x : x 条件 ，需过滤的元组)
date = filter(lambda x : x <= (m,d),dates)
print(list(date))
# exit()
# 利用滤镜函数过滤出日期小于等于设定值的所有符合的元组元素。取大于数组长度的后一个元素，下标即是数组长度
# print("您的星座是%s！" % xingzuo[len(list(date)) % 12])

