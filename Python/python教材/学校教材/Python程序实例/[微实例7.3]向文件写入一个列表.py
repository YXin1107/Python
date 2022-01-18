# [微实例7.3]向文件写入一个列表
import os
os.chdir('C:/Users/Yxin1/Desktop')
fname = input('请输入要写入的文件:')
fo = open(fname, 'w+')
ls = ['唐诗', '宋词', '元曲']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
