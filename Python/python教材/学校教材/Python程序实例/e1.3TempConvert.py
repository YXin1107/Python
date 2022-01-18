# e1.3TempConvert.py
# 定义函数

def TempConvert(Temp):
    if Temp[-1] in ['F', 'f']:
        C = (eval(Temp[0:-1]) - 32)/1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif Temp[-1] in ['C', 'c']:
        F = (eval(Temp[0:-1])*1.8) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")


# 上述为定义的函数
Temp = input("输入带有符号的温度: ")
TempConvert(Temp)
