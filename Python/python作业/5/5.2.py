# 实现isOdd()函数
def isOdd():
    num = input("请输入一个整数:")
    try:
        num = eval(num)
        if num % 2:
            return True
        else:
            return False
    except NameError:
        print('输入格式错误')


isOdd()
