# 4.2 统计不同字符个数
chr = input("请输入一行字符(中英文字符、数字、空格和其他字符):")
a, b, c, d = 0, 0, 0, 0
for i in chr:
    if "0" <= i <= "9":  # 判断数字
        a += 1
    elif i == " ":  # 判断空格
        b += 1
    elif "a" <= i <= "z" or "A" <= i <= "Z":  # 判断英文字符
        c += 1
    else:  # 判断其他字符 会把中文加到这里来
        d += 1
print("数字有{}个\n空格有{}个\n英文字符有{}个\n其他字符有{}个".format(a, b, c, d))
