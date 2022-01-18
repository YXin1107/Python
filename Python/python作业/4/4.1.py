# 4.1 猜数游戏
from random import *
num = randint(0, 9)
x = eval(input("请输入1到9之间的整数："))
n = 0
while 1:
    n += 1
    if x < num:
        print("遗憾，太小了")
    elif x > num:
        print("遗憾，太大了")
    else:
        print("预测{}次，你猜对了".format(n))
        break
    x = eval(input("请输入1到9之间的整数："))
