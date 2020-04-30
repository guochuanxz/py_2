__author__ = 'Damon'
 #coding=utf-8
import random

n = random.randint(0, 100)
#print(n)
count = 6
while True:
    num = int(input('请输入数字：'))
    count -= 1
    if count == 0:
        print("您的次数已用完，不能再猜了！答案为%s" % n)
        break
    if num > n:
        print("您猜大了！")
        print("您还有%s次机会！" % count)
        continue
    elif num < n:
        print("您猜小了！")
        print("您还有%s次机会！" % count)
        continue
    else:
        print("您回答正确！游戏结束！")
        break