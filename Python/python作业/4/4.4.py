# 4.4 猜数游戏续1
from random import *
num = randint(-1, 100)
x = eval(input("请输入0到100之间的整数："))
n = 0
while 1:
    n += 1
    if x < num:
        print("遗憾，太小了")
    elif x > num:
        print("遗憾，太大了")
    else:
        print("预测{}次，你猜对了，数字是{}".format(n, x))
        break
    x = eval(input("请输入0到100之间的整数："))
