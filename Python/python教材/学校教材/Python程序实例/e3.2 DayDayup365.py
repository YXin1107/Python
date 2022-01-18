# e3.2 DayDayup365
'''
一年365天，如果好好学习时能力值相比前一天提高5%，当放任时相比前一天下降5%，效果相差多少？
'''
import math
dayup = math.pow((1.0 + 0.005), 365)
daydown = math.pow((1.0 - 0.005), 365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
