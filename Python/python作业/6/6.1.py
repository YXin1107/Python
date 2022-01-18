# 随机密码生成
# ASCII码:48-57为阿拉伯数字 65-90为26个大写字母 97-122为26个小写字母
import random
ch = list(range(48, 58))+list(range(65, 91))+list(range(97, 123))


def code():
    mi = ""
    for i in range(8):
        n = random.randint(0, 61)
        mi = mi + chr(ch[n])
    return mi


def main():
    for i in range(1, 11):
        print("the {} code is {}".format(i, code()))


main()
