# -*- coding:utf-8 -*-
# Author:Damon Guo
# 死循环
count = 0
while True:
    print(count)
    # count +=1
    count = count + 1
    if count ==100:
        break