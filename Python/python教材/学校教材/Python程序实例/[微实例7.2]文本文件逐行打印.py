# [微实例7.2]文本文件逐行打印
import os
os.chdir('C:/Users/Yxin1/Desktop')
fname = input("输入要打开的文件:")
fo = open(fname, 'r')
for line in fo.readlines():
    print(line)
fo.close()
