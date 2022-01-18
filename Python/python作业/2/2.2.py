# 人民币和美元汇率兑换
# 1美元=6人民币
# d-美元 r-人民币

money = input('输入带有符号的数字(d为美元,r为人民币):')
if money[-1] in 'd':
    R = eval(money[0:-1]) * 6
    print("转换后的金额为{:.2f}".format(R))
elif money[-1] in 'r':
    D = eval(money[0:-1]) / 6
    print("转换后的金额为{:.2f}".format(D))
else:
    print("格式错误")
