# e6.1 Calpi
from random import random
from math import sqrt
from time import process_time
DARTS = 10000  # 抛点个数
hits = 0  # 在圆内的抛点个数
process_time()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)  # 四分之一圆
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("Pi的值是{}.".format(pi))
print("运行时间是:{:5.5}s".format(process_time()))
