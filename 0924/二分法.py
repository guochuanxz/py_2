# -*- coding:utf-8 -*-
# Author:Damon Guo

import random

n = random.randint(0,100)
# print(num)
count = 6
num = int(input("请输出您猜测的数字："))
# print(answer)
while count >=0 :
    count -= 1
    if count == 0 :
        print("您的次数已经用完了，答案为%s"% num )
        break
    if num > n:
        print("您猜大了，您还有%s次机会！" % count )
        continue
    elif num <n :
        print("您猜小了，您还有%s次机会！" % count )
        continue
    else :
        print("回答正确！答案为%s"% num )


