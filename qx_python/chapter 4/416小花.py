__author__ = 'Damon'
#coding=utf-8
import turtle
def tree(branchLen, t,r):
    if branchLen > 20:
        t.color('brown')
        t.pensize(r)
        t.forward(branchLen)
        # 画树的主干
        t.right(20)
        # 右边的树枝
        tree(branchLen - 8,t,r - 0.1 * r)
        # 右分支调用相关的函数
        t.color('brown')
        t.left(30)
        tree(branchLen - 5,t,r - 0.1*r)
        t.right(10)
        # 关于角度，注意最后一定是回到垂直就90度，才会成为一棵树
        t.color('brown')
        t.backward(branchLen)
        # 每一次落笔的时候，都要将颜色矫正，因为是一个回溯的过程
        # 末端可能已经修改过笔的颜色
    elif branchLen > 10:
        t.color('green')
        t.pensize(r)
        t.forward(branchLen)
        t.right(10)
        tree(branchLen - 2, t,r - 0.1*r)
        # 函数的branchlen表示对应的长度，每一次迭代循环的差值越大，树枝越密集
        # 函数的r表示对应的树枝的粗细，减去一个变量，每次迭代减去一个差值会越变越细
        t.left(20)
        tree(branchLen - 3, t,r - 0.1 *r)
        t.right(10)
        t.backward(branchLen)
    else:
        t.color('pink')
        t.pensize(1)
        t.circle(4)
        t.color('green')

def main():
    b = turtle.Turtle()
    b.left(90)
    b.speed(0)
    b.fillcolor('pink')
    b.up()
    # 抬笔
    b.backward(100)
    b.down()
    # 落笔
    # 总而言之，是将笔移到图版的下部分，而不是中部分
    b.color('brown')
    tree(30,b,3)
    b.ht()  # 隐藏turtle

main()
# turtle.screensize(410,500,'pink')
