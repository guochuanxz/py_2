# open()打开文件
# read()输入
# readline()移动一行
# seek()文件内移动
# write()输出
# close()关闭
# 可写w
# file1 = open("name.txt","w")
# file1.write("Damon郭川")
# file1.close
# 读文件
file2 = open("name.txt")
print(file2.read())
file2.close()

#在原文件基础上增加
file3 = open('name.txt','a')
file3.write("\n诸葛孔明")
file3.close()
