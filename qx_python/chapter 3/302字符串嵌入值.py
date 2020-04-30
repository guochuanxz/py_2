# -*- coding:utf-8 -*-
# Author:Damon Guo

name = "Damon"
score = 100
grade = 6
# %s %d
msg = "我叫%s,我今年上%s年级，我考了 %s 分"

print(msg % (name,grade,score))
print(msg % (name,7,135))
