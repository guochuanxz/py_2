# -*- coding:utf-8 -*-
# Author:Damon Guo
names = ["A","E","B","C","D",["1a","1b"]]
# names.sort()
names_1 = names.copy()

print(names)
print(names_1)

names[1] = "汉字"
names[-1][0] = "DAMON"
print(names)
print(names_1)
