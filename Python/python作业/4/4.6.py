# 4.6 羊车门问题(蒙特卡罗方法)
import random
DARTS = 10000
first_choice_n = 0  # 初始化不改选择的次数
change_choice_n = 0  # 初始化更改选择的次数
for i in range(DARTS):
    car = random.randint(1, 3)
    guess = random.randint(1, 3)
    if car == guess:
        first_choice_n += 1
    else:
        change_choice_n += 1
a = first_choice_n / DARTS
b = change_choice_n / DARTS
print("不改变的概率:{:.2f}\n改变的概率:{:.2f}".format(a, b))
