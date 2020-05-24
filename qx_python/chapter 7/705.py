__author__ = 'Damon'
# coding=utf-8
def chengfabiao():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        # print("%d" % row)
        print("")
        row += 1
# 打印小星星逐行加一个
for i in range(9):
    print(i*"*")