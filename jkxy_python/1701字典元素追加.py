__author__ = 'Damon'
# coding=utf-8
shengxiao_ = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
xingzuo = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
dates = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22))

shengxiao_dict = {'猴':0,'鸡':0,'狗':0,'猪':0,'鼠':0,'牛':0,'虎':0,'兔':0,'龙':0,'蛇':0,'马':0,'羊':0}
xingzuo_dict = {
    '摩羯座': 0,'水瓶座': 0,'双鱼座': 0, '白羊座': 0, '金牛座': 0, '双子座': 0, '巨蟹座': 0, '狮子座': 0, '处女座': 0, '天秤座': 0, '天蝎座': 0, '射手座': 0
}
count = 0
while True:
    count +=1
    if count ==5:
        break
    y = int(input("请输入您出生的年:"))
    m = int(input("请输入您出生的月:"))
    d = int(input("请输入您出生的日:"))
    n = 0
    while dates[n] < (m, d):
        if m == 12 and d >= 22:
            break
        n = n + 1
    print(xingzuo[n])
    xingzuo_dict[xingzuo[n]] += 1
    shengxiao_dict[shengxiao_[y % 12]] +=1
    # 遍历各星座出现的次数
    for i in xingzuo_dict.keys():
        print("%s出现的次数是 %d" % (i,xingzuo_dict[i]))
    for i in shengxiao_dict.keys():
        print("%s出现的次数是 %d" % (i, shengxiao_dict[i]))