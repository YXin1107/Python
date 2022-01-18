# 生日悖论分析
# 感觉写的有问题
import random
p = 1


def birth(n):
    ls = []
    for i in range(n):
        a = random.randint(1, 366)
        ls.append(a)
    if len(ls) != len(set(ls)):  # 不相等说明有重复的
        global p
        for i in range(n):
            p = p*(366-i)  # 生日不相同的取法
    else:
        print("There is no same birth")
    return 1-p/366**n  # 新学的概论统计


print(birth(90))
