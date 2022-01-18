# 天天向上续2
def daydayup(up):
    dup = 1
    td = 365
    for i in range(1, td+1):
        if i % 11 in range(4, 8):
            dup = dup * (1 + up)
        elif i % 11 != 0:
            dup = dup * 1
        else:
            dup = dup * (1 - up)
    return dup


def daydayup2(up2):
    dup = 1
    td = 365
    scale1 = [4, 5, 6, 7, 11, 12, 13, 14]
    for i in range(1, td+1):
        if i % 15 in scale1:
            dup = dup * (1 + up2)
        elif i % 15 != 0:
            dup = dup * 1
        else:
            dup = dup * (1 - up2)
    return dup


x = eval(input("请输入学习增长率:"))
print("10天休息1天,能力值为:{:.2f}".format(daydayup(x)))
print("15天休息1天,能力值为:{:.2f}".format(daydayup2(x)))
