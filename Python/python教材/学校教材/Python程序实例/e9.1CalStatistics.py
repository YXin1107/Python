# e9.1CalStatistics
from math import *


def getNum():  # 获取用户输入
    nums = []
    iNumStr = input('请输入数字(直接输入回车退出):')
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input('请输入数字(直接输入回车退出):')
    return nums


def mean(numbers):  # 计算平均值(数字)
    s = 0.0
    for i in numbers:
        s += i
    s_averge = s/len(numbers)
    return s_averge


def dev(numbers, mean):  # 计算方差(数字,平均值)
    sdev = 0.0
    for i in numbers:
        sdev += (i-mean)**2
    sdev_1 = sqrt(sdev/(len(numbers)-1))
    return sdev_1


def median(numbers):  # 计算中位数(数字)
    sorted(numbers)
    l = len(numbers)
    if l % 2 == 0:
        med = (numbers[l//2] + numbers[l//2-1])/2  # 注意!此处使用//,表示整数相除
    else:
        med = numbers[l//2]
    return med


n = getNum()  # 主体函数(n = 用户输入)
m = mean(n)  # 获取平均值
x = dev(n, m)  # 获取方差
y = median(n)  # 获取中位数
print("平均值:{},方差:{:.2},中位数:{}".format(m, x, y))
