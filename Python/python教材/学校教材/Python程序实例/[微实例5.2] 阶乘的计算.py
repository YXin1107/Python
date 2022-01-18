# [微实例5.2] 阶乘的计算
def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n-1)


num = input("please enter a number:")
print(func(int(num)))
