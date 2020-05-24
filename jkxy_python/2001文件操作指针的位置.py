__author__ = 'Damon'
#coding=utf-8
file = open('demo.txt')
file2 = open('demo.txt')
# print(file.tell())
# 指针移到第5个字符后，指针前的文件内容被读取
# print(file.read(5))
# 说出指针位置
# print(file.tell())
# 挪动指针的位置 参数一便宜位置  参数二   0代表从文件开始偏移 1表示从当前位置偏移  2从文件结尾
file2.seek(0,0)
# print(file2.tell())
print(file2.read())
