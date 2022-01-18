# 天天向上续1
def daydayup(up):
    dup = 1
    td = 365
    for i in range(1, td+1):
        if i % 7 in range(1, 4):
            dup = dup * 1
        else:
            dup = dup * (1 + up)
    return dup


x = eval(input("请输入学习增长率:"))
print("连续学习365天后能力值为:{:.2f}".format(daydayup(x)))
