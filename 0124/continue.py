# -*- coding:utf-8 -*-
# Author:Damon Guo
for i in range (0,10):
    # 循环体
    if i <3:
        print("loop :",i)
        continue
    else:
        print("ooooooo:",i)
    print("hehe")
    # 循环体结束，按语法循环体内会循环执行，print（“hehe”）会执行10次，break停止循环，continue跳出当前循环，执行下一次循环