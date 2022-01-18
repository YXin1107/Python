# [微实例3.2]凯撒密码(改版,中英文都行)
'''
对信息中每一个英文字符循环替换为字母表序列中该字符后面第三个字符
对应关系如下:
原文:ABCDEFGHIJKLMNOPQRSTUVWXYZ
密文:DEFGHIJKLMNOPQRSTUVWXYZABC
原文字符P,密文字符C,满足如下条件:
C = (P + 3) mod 26
解密方法:
P = (C - 3) mod 26
'''
code = input("请输入明文:")
for p in code:
    if ord('a') <= ord(p) <= ord('z'):
        c = (ord('a') + (ord(p) - ord('a') + 3) % 26)
        print(chr(c), end='')

    else:
        # 中文转Unicode编码
        re = code.encode("unicode_escape")
        print(re)
        break
