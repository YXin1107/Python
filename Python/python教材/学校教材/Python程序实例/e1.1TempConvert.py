# e1.1TempConvert.py
"""
C摄氏温度 F华氏温度
换算方法：
C = (F - 32)/1.8
F = C*1.8 + 32
"""

Temp = input("输入带有符号的温度: ")
if Temp[-1] in ['F', 'f']:
    C = (eval(Temp[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif Temp[-1] in ['C', 'c']:
    F = (eval(Temp[0:-1])*1.8) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
