__author__ = 'Damon'
#coding=utf-8
xingzuo  = ('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座')
dates = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
m = int(input("请输入您出生的月:"))
d = int(input("请输入您出生的日:"))
for i in range(12):
    if dates[i] >=(m,d):
        print(xingzuo[i])
        break
    elif m == 12 and d >22:
        print(xingzuo[11])
        break
