# -*- coding:utf-8 -*-
# Author:Damon Guo
import sys
# 变量被使用次数
x = []
y = x
print(sys.getrefcount(x))

