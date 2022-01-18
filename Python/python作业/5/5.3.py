# isNum()函数
def isNum():
    try:
        str = eval(input("请输入一个字符串:"))
        if isinstance(str, int) or isinstance(str, float) or isinstance(str, complex):
            return True
        else:
            return False
    except NameError:
        print("输入格式错误")


isNum()
