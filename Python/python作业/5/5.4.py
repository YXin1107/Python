# 实现multi()函数
def multi(*b):
    a = 1
    for i in b:
        if isinstance(i, float) or isinstance(i, complex) or isinstance(i, int):
            a *= i
        else:
            print('输入格式错误')
    print(a)


multi(2, 87, 1)
