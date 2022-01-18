# 4.7 异常处理改造实例1
while 1:
    try:  # 可处理小数的温度输入
        tem = input("请输入带符号的温度: ")
        if tem[-1] in ["f", "F"]:
            C = (eval(tem[:-1]) - 32)/1.8
            print('转换后的温度是{:.2f}C'.format(C))
            break  # 跳出循环
        elif tem[-1] in ['C', 'c']:
            F = 1.8 * (eval(tem[:-1])) + 32
            print('转换后的温度是{:.2f}F'.format(F))
            break  # 跳出循环
        else:
            print("输入格式错误")
    except:
        print("输入格式错误")
