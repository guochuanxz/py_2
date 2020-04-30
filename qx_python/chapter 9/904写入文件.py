# -*- coding:utf-8 -*-
# Author:Damon Guo

# open第二个参数不填默认是r
file = open("D:/python_1/qx_python/chapter 9/test.txt","w")
file.write("这是python程序执行时写入到文件的内容，比如日志")
# 关闭文件，返回值是空
print(file.close())
# if not bool(file.close()):
#     print("写入成功")