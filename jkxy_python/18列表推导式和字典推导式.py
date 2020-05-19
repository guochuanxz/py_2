__author__ = 'Damon'
# coding=utf-8
# 做一个10以内的偶数2次方列表
a_list = []
for i in range(2, 11):
    if i % 2 == 0:
        a_list.append(i ** 2)
print(a_list)
# 简便的写作方法
b_list = [i ** 2 for i in range(2, 11) if i % 2 == 0]
print(b_list)

a_dict = {
    i: i ** 2 for i in range(2, 11) if i % 2 == 0
}
print(a_dict)
