__author__ = 'Damon'
# coding=utf-8

a = [1, 3, 5, 7, 9]
b = 4
# 滤镜函数返回值是对象
print(list(filter(lambda x: x < b, a)))
print(len(list(filter(lambda x: x < b, a))))


def is_odd(n):
    return n % 2 == 1
print(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
def not_empty(s):
    return s and s.strip()


filter(not_empty, ['A', '', 'B', None, 'C', ' '])
# 结果: ['A', 'B', 'C']