__author__ = 'Damon'
#coding=utf-8
list=["a","b","c","d"]
a = iter(list)
print(next(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())
# 自己做生成器用来迭代
def floatRange(start,end,step):
    x = start
    while x < end:
        yield x
        x = x + step
for i in floatRange(1,5,0.5):
    print(i)

